import json

from django.core.management import BaseCommand
from django.core.management.commands import loaddata


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('data.json', 'r', encoding='utf-16') as f:
            file = json.load(f)



