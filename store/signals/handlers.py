from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import User
from store.models import Customer


@receiver(post_save, sender=User)
def create_customer_for_new_user(sender, **kwargs):
    if kwargs['created']:
        Customer.objects.create(user=kwargs['instance'])
