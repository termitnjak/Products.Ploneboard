#
# Tests the default workflow
#

from Testing import ZopeTestCase
from AccessControl.Permission import Permission
from Products.CMFPlone.tests import PloneTestCase

from Products.CMFCore.WorkflowCore import WorkflowException

from Products.CMFCore.utils import _checkPermission as checkPerm
from Products.CMFCore.permissions import AccessContentsInformation
from Products.CMFCore.permissions import View
from Products.CMFCore.permissions import ModifyPortalContent
from Products.CMFCore.permissions import AccessContentsInformation
from Products.CMFCore.permissions import ListFolderContents
from Products.CMFCalendar.EventPermissions import ChangeEvents
from Products.CMFPlone.utils import _createObjectByType

from Products.Ploneboard.Extensions import WorkflowScripts # Catch errors
from Products.Ploneboard.tests import PloneboardTestCase
from Products.Ploneboard import permissions

import transaction

default_user = PloneTestCase.default_user


class TestCommentWorkflow(PloneboardTestCase.PloneboardTestCase):

    def afterSetUp(self):
        self.workflow = self.portal.portal_workflow
        self.board = _createObjectByType('Ploneboard', self.folder, 'board')
        self.forum = _createObjectByType('PloneboardForum', self.board, 'forum')
        self.conv = self.forum.addConversation('conv1', 'conv1 body')

        self.portal.acl_users._doAddUser('member', 'secret', ['Member'], [])
        self.portal.acl_users._doAddUser('member2', 'secret', ['Member'], [])
        self.portal.acl_users._doAddUser('reviewer', 'secret', ['Reviewer'], [])
        self.portal.acl_users._doAddUser('manager', 'secret', ['Manager'], [])

    # Check allowed transitions

    def testAutoPublishMemberposting(self):
        comment = self.conv.objectValues()[0]

        self.login('member')
        self.failUnless(checkPerm(permissions.ApproveComment, self.forum))
        self.failUnless(checkPerm(permissions.ApproveComment, self.conv))
        self.failUnless(checkPerm(permissions.ApproveComment, comment))

        self.assertEqual(self.workflow.getInfoFor(self.forum, 'review_state'), 'memberposting')
        self.assertEqual(self.workflow.getInfoFor(self.conv, 'review_state'), 'active')
        self.assertEqual(self.workflow.getInfoFor(comment, 'review_state'), 'published')

# make_moderated disabled until moderation is fixed in general
#    def testAutoSubmitModerated(self):
#        self.workflow.doActionFor(self.forum, 'make_moderated')
#
#        self.login('member')
#
#        conv = self.forum.addConversation('conv2', 'conv2 body')
#        comment = conv.objectValues()[0]
#
#        self.failIf(checkPerm(permissions.ApproveComment, self.forum))
#        self.failIf(checkPerm(permissions.ApproveComment, self.conv))
#        self.failIf(checkPerm(permissions.ApproveComment, comment))
#
#        self.assertEqual(self.workflow.getInfoFor(self.forum, 'review_state'), 'moderated')
#        self.assertEqual(self.workflow.getInfoFor(conv, 'review_state'), 'pending')
#        self.assertEqual(self.workflow.getInfoFor(comment, 'review_state'), 'pending')

    def testCommentEditing(self):
        self.login('manager')

        conv = self.forum.addConversation('conv2', 'conv2 body')
        comment = conv.objectValues()[0]
        
        self.failUnless(checkPerm(permissions.EditComment, comment))
        
        self.logout()

        self.login('member2')
        self.failIf(checkPerm(permissions.EditComment, comment))


class TestWorkflowsCreation(PloneboardTestCase.PloneboardTestCase):

    def afterSetUp(self):
        self.workflow = self.portal.portal_workflow

    def testWorkflowsCreated(self):
        workflows = ['ploneboard_workflow', 'ploneboard_forum_workflow',
                     'ploneboard_conversation_workflow', 'ploneboard_comment_workflow']
        for workflow in workflows:
            self.failUnless(workflow in self.workflow.objectIds(), "%s missing" % workflow)

    def testPreserveChainsOnReinstall(self):
        boardtypes = ('Ploneboard',
                      'PloneboardForum',
                      'PloneboardConversation',
                      'PloneboardComment')

        self.workflow.setChainForPortalTypes(boardtypes, 'plone_workflow')
        self.workflow.getChainForPortalType('Ploneboard')
        for boardtype in boardtypes:
            self.failUnless('plone_workflow' in self.workflow.getChainForPortalType(boardtype),
                            'Workflow chain for %s not set' % boardtype)

        self.portal.portal_quickinstaller.reinstallProducts(['Ploneboard'])
        for boardtype in boardtypes:
            chain = self.workflow.getChainForPortalType(boardtype)
            self.failUnless('plone_workflow' in chain,
                            'Overwritten workflow chain for %s: %s' % (boardtype, ', '.join(chain)))

    def testPermissionsOnPortal(self):
        p=Permission('Ploneboard: Add Comment Attachment', (), self.portal)
        roles=p.getRoles()
        self.failUnless('Member' in roles)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestCommentWorkflow))
    suite.addTest(makeSuite(TestWorkflowsCreation))
    return suite
