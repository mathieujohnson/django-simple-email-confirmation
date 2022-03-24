from django.dispatch import Signal

email_confirmed = Signal()
unconfirmed_email_created = Signal()
primary_email_changed = Signal()
