from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

from .models import Customer


def customer_profile(sender, instance, created, **kwargs):
    if created:
        set_group = Group.objects.get(name='customers')
        instance.groups.add(set_group)

        Customer.objects.create(user=instance, name=instance.username, email=instance.email)

post_save.connect(customer_profile, sender=User)
