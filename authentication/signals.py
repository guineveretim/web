
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender='authentication.Status')
def update_status(sender, instance, created, **kwargs):
    if created:
        return

    status = instance
    subject = 'Status Update Notification'
    message = f'Your status has been updated to: {status.status}'
    from_email = settings.EMAIL_HOST_USER  # Ensure this setting is correctly defined

    # Assume your Status model has a relationship with the Application model
    # Example: status.application.user.email
    to_email = status.application.user.email  # Adjust this according to your actual model relationships
    
    send_mail(subject, message, from_email, [to_email], fail_silently=False)
