from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Make a user a superuser'

    def handle(self, *args, **options):
        user = User.objects.get(username='digital')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS('Successfully made digital a superuser'))
