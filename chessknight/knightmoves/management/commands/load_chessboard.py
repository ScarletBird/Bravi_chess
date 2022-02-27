import csv
from django.core.management import BaseCommand
from knightmoves.models import BoardSpace

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                BoardSpace.objects.create(
                    coordinate=row[0]
                )
            