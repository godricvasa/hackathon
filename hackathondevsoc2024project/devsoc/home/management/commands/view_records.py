# myapp/management/commands/access_records.py

from django.core.management.base import BaseCommand
from home.models import *  

class Command(BaseCommand):
    help = 'Access records from the database'

    def handle(self, *args, **kwargs):
        # Retrieve records from the database
        records = Question.objects.all()

        # Display records
        for record in records:
            print(f"Name: {record.title}, Email: {record.content}, Phone: {record.created_at}")
