from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        self.stdout.write(f"Total users: {users.count()}")
        for user in users:
            self.stdout.write(f"User: {user.username}, Staff: {user.is_staff}, Superuser: {user.is_superuser}")