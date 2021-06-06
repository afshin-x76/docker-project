from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    '''
     if there is no user in database it will
    create superuser with username=admin, password=admin, email=admin@admin.com
    Note this is only for test!!
    The best practice is that to load your exist data from old database.
    '''
    def handle(self, *args, **kwargs):
        if not User.objects.all().exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@admin.com",
                password="admin"
            )