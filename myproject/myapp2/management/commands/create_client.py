from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        user = Client(name='John', email='john@example.com',
                      phone_number='89107777777',
                      address="bla bla lba",
                      registration_date='2021-12-12 11:44')
        user.save()
        self.stdout.write(f'{user}')