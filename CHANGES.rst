Changelog
=========

3.5 (unreleased)
----------------

- Fix wrong permission check in add conversation viewlet. Fixes #29.
  [jensens]

- Check if toPloneboardTime gets a callable and call it to get a Datetime
  [jensens]

- Fixed visual issue with HTML lists when WISIWYG editor is enabled 
  [keul]

- Call unmarkCreationFlag method after comment creation, to remove creation flag
  [cekk]

- Fixed attachment translations [cekk]

- Fixed bug: moderation_form fail to render when using VirtualHostMonster
  [rafaelbco]

3.4 (2013-05-11)
----------------

- Updated i18n machinery [kiorky]

- More robust & quickier functionnal tests
  [kiorky]

- Refresh buildout infra
  [kiorky]

- Better setup for TravisCI tests
  [kiorky]

- Made tests pass. Added Travis support.
  [sureshvv]

- Fix genericsetup import steps declaration
  [kiorky]

- Compatilbity with new plone.batching
  [kiorky]

- Preserve Link with URL as text instead of creating nesting "a" nodes.
  Issue #10 at https://github.com/collective/Products.Ploneboard/issues/10
  Allow URI with round brackets. Issue #7
  [ksuess]

- Updated Spanish translations
  [macagua]

- Updated i18n support, adding i18n sentences for translation strings, synced
  the pot files and updated the po files.
  [macagua]

- Fix issue #11 at https://github.com/collective/Products.Ploneboard/issues/11
  [macagua]

- Fix issue #9 at https://github.com/collective/Products.Ploneboard/issues/9
  [sureshvv]

- Make pb_attachment a resource js file rather than dtml
  [sureshvv]

- Add forum property that will enable members to edit their own comments
  [sureshvv]

- Fixed imports for Plone 4.3
  [kroman0]

- Fixed i18n headers, added locales folder and updated pt-br translations
  [davilima6]

- Add button label to start a new conversation instead of reusing the "add comment"
  label.
  [gaudenz]

- Don't show workflow actions and reply button while composing a reply.
  [gaudenz]

- Fix compatibility with classic (non Chameleon) Zope template engine
  [gaudenz]

- Remove "Quick Reply" label. From the users point of view this is just
  a normal reply.
  [gaudenz]

- Do no swallow ConflictError anymore [keul]

- Update number of comments looking at the current users permissions
  (before this the number were updated even if a comment was not published)
  [cekk]

- Fixed forum view: always display the third column in forum view
  [keul]

- Rejected comments can now be modified from owners before submitting again
  [keul]

- Added support for "Site Administrator" role
  [keul]

- Forum area is not visible to users (even if published) if inside private
  folders
  [keul]

- Allowed translations for "Anonymous" comment in ploneboard views [cekk]

- Added Captcha support for anonymous. If recaptcha is installed and configured. [cekk]

- Fixed italian translations [cekk]

- Fixed add_comment_script. After adding a new comment, if the user
  (logged or anonymous) can't access to the comment (for example if it's moderated),
  he will be redirected to the discussion
  [cekk]

- Added text field to Ploneboard AT [cekk]

3.3 (2012-09-08)
----------------

- Add default permission mappings for the Plone 'Reader', 'Contributor',
  'Editor', and 'Reviewer' roles used on the sharing tab.
  [rossp]

- Rename default GS profile to "default" and keep "ploneboard" as a
  backwards compatibility alias only.
  [gaudenz]

- Add upgrade step to register form controller actions for comments.
  [gaudenz]

- Add upgrade step to register ploneboard.css in portal_css.
  [gaudenz]

- Add manifest [aclark4life]

3.2 (2011-12-22)
----------------

- Added odd/even class on conversation view comments.
  [thomasdesvenain]

- Conversation views are restricted to View permission (not public),
  so if it is visible to authenticated members only,
  anonymous are redirected to login form.
  [thomasdesvenain]

- Fixed threaded conversation view after conversation_view template removed.
  [thomasdesvenain]

3.1 (2011-12-07)
----------------

- Fix threaded conversation view using a browser view instead of template.
  [thomasdesvenain]

- I18n fixes on add conversation form.
  Updated translation files.
  [thomasdesvenain]

- Refactor: make it easier to use another type of conversation.
  [thomasdesvenain]

- Refactor: add conversation form and messages comes in a viewlet.
  [thomasdesvenain]

- Enable choice of what board or forum to show in recent portlet
  [martior]

3.0 (2011-10-06)
----------------

- Use the base profile from CMFPlacefulWorkflow to avoid nuking the default
  workflow chain settings by installing unused workflows.
  [tesdal]

- Pinned `python-dateutil` to be less than version 2.0, as this a Python 3 only
  release.
  [keul]

- Synchronized French po from pot and completed translations.
  [sgeulette]

- Polish translations added.
  [radekj]

- German translation updated.
  [ksuess]

- Updated Danish translations.
  [kroman0]

- Synced with pot and updated Swedish translations.
  [svincic]

- Plone 4 and 4.1 compatible.
  [thomasdesvenain, rochecompaan, jaroel, vmaksymiv, ksuess, radekj,
  maciej.zieba, jensens, maartenkling]


2.2 (2011-02-08)
----------------

- Minor updates to German translation. "Message Board" is now "Foren" instead of
  "Forum".
  [thet]

- Added profile for a Ploneboard intranet workflow. Note that currently there
  are not transitions to publish selected content outside the intranet.
  [thet]

- Fixed bug where you could not change Maximum Attachment Size while editing a
  Forum. Added test.
  [sureshvv]

- Moved event notifications for object creation to later phase. Objects
  should be populated with data when firing ObjectInitializedEvent.
  [naro]

- Remove catalog.xml and set up catalog from code instead. This avoids nuking
  index on update/reinstall.
  [tesdal]

- Fix some references to the wrong the names of some browser views.
  [rossp]

- Fix a setuphandler step dependency.
  [rossp]

- Add some french translations in the plone domain and fix the translation of
  "help_body_attachments_maxsize" in Ploneboard-fr.po.
  [sylvainb]

- ploneboard_recent and ploneboard_unanswered views need access to the
  toPloneboardTime method. This fixes
  http://plone.org/products/ploneboard/issues/207 as well as
  http://plone.org/products/ploneboard/issues/208
  [sylvainb]

- No more Zope2 interfaces
  [toutpt]

- Merged changes from plone4-compatibility branch
  [jcbrand]

- Defined global variables in templates, for Plone4 compatibility
  [jcbrand]

- Fix Spanish translation for "Log in to start a conversation".
  [timo]

- Fix translation for "Post comment" and "Cancel" for the add_comment_form.
  [timo]


2.1b2 - 20091019
----------------

- Set up dependencies correctly.
  [tesdal]

2.1b1 - 20091019
----------------

- Create forums data structure in board view as dict of dicts.
  [tesdal]

- Create conversations data structure in forum view as list of dicts.
  This can be easily cached, although there is no support for it yet.
  [tesdal]

- Create comment automatically in conversation if adding conversation
  with text.
  [tesdal]

- Made profiles for funkload testing.
  [tesdal]

- Add the complete list of date elements when translating dates to allow
  customization of format by overriding the base translation string.
  [kdeldycke]

- Fixed cosmetic bug (search results relevance percentage).
  [glenfant]

- Added Swedish translation, thanks to Martin Lundwall.
  [hannosch]

- Add Russian translation, courtesy of Eugene Korenevsky.
  [wichert]

- Add missing empty alt-text for content type icons in the search results.
  [wichert]

- Modified author retrieval to allow for blank fullnames on users, falling back
  to their user ID instead.
  [rockdj]

- Added event notifications for object creation with _createObjectByType for
  Conversation, Comment and Attachment objects.
  [daftdog]

- Make Conversation batch size configurable. Used to be 30 always.
  [sureshvv]

- When adding comment, do not redirect to first page of conversation always.
  Redirect to page anchored to comment
  [sureshvv]

- When viewing a forum, clicking on Most recent comment link should take you there
  [sureshvv]

- Make toPloneboardTime obsolete as a PythonScript. It is now a method in the view class.
  [sureshvv]

- User can edit thier and only their comments using PlacefulWorkflow
  [sureshvv]

- Added workflow to lock an entire message board
  [sureshvv]

2.0 - March 14, 2008
--------------------

- Index newly added comments so all their data is correct in the catalog.
  [wichert]

- Rework the RSS feed: make the Ploneboard RSS feed work recursively so
  a feed on a forum shows all conversations and a feed on the board itself
  shows all comments from all fora. Enabled feeds on the Ploneboard type.
  [wichert]

- Remove the object_provides index from Ploneboard: Plone 3.0 has a much
  more efficient version of that itself.
  [wichert]

- Add an explicit visualClear below the 'start new conversation' button
  so it does not overlap the table. This fixes
  http://plone.org/products/ploneboard/issues/161
  [wichert]

- In preparation of PLIP195 being merged for Plone 3.1: declare
  Products.SimpleAttachment as a dependency in our GS profile.
  [wichert]

_ Update the Lithuanian translation. This fixes
  http://plone.org/products/ploneboard/issues/164
  [wichert]

- Correct the attachment size vocabulary: the values should be integers,
  not strings. This fixes http://plone.org/products/ploneboard/issues/168
  as well as http://plone.org/products/ploneboard/issues/144
  [wichert]

- Honour the content-type for comments when transforming them. Doing things
  like replacing newlines with <br/> on text/html comments is kind of silly.
  [wichert].


2.0rc1 - December 21, 2007
--------------------------

- Make the comment-icon a link to the comment. This fixes
  http://plone.org/products/ploneboard/issues/78
  [wichert]

- Fix a corner case: creating a conversation without text but with attachments
  would loose the attachments.
  [wichert]

- When creating a new conversation do not set its description to the
  entered text.
  [wichert]

- Switch to a plone.app.controlpanel based control panel.
  [wichert]

- Correct base class for portlet add form. This fixes
  http://plone.org/products/ploneboard/issues/154
  [wichert]


2.0b2 - December 19, 2007
-------------------------

- Correct login-name vs userid usage.
  [wichert]

- Correct attachment handling, which broke in previous 2.0 releases.
  [fschulze]

- Add a search form to the board view.
  [wichert]

- Disable non-working javascript-based sorting on conversation and forum views.
  [wichert]

- Port the recent conversations portlet to plone.portlets.
  [wichert]

2.0b1 - November 28, 2007
-------------------------

- Portlets management enabled, Plone 3.0 tests, deprecations hidden.
  [glenfant]

- French translation completed.
  [glenfant]

- Port to Plone 3.0
  [wichert, fschulze]
