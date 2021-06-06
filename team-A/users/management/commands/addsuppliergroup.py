from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        permissions = Permission.objects.filter(content_type__app_label='products')
        group, state = Group.objects.get_or_create(name='Supplier-Permissions')
        if state:
            for perm in permissions:
                group.permissions.add(perm)
            group.save()