# myapp/management/commands/add_records.py

from django.core.management.base import BaseCommand
from home.models import UserInfo

class Command(BaseCommand):
    help = 'Adds records to the database'

    def handle(self, *args, **kwargs):
        # Logic to add records
        UserInfo.objects.create(username='John', email='john@example.com', password='123456')

        self.stdout.write(self.style.SUCCESS('Records added successfully'))
