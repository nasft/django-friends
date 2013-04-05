from django.conf import settings
from django.db.models import signals
from django.utils.translation import ugettext_noop as _


if "notification" in settings.INSTALLED_APPS:
    from notification.models import NoticeType

    def create_notice_types(app, created_models, verbosity, **kwargs):
        NoticeType.create("friends_invite", _("Invitation Received"), _("you have received an invitation"), default=2)
        NoticeType.create("friends_invite_sent", _("Invitation Sent"), _("you have sent an invitation"), default=1)
        NoticeType.create("friends_accept", _("Acceptance Received"), _("an invitation you sent has been accepted"), default=2)
        NoticeType.create("friends_accept_sent", _("Acceptance Sent"), _("you have accepted an invitation you received"), default=1)
        NoticeType.create("friends_otherconnect", _("Other Connection"), _("one of your friends has a new connection"), default=2)
        NoticeType.create("join_accept", _("Join Invitation Accepted"), _("an invitation you sent to join this site has been accepted"), default=2)

    signals.post_syncdb.connect(create_notice_types, sender=NoticeType)
else:
    print "Skipping creation of NoticeTypes as notification app not found"
