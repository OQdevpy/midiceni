from django.core.management.base import BaseCommand

from apps.common.uttils import import_data


class Command(BaseCommand):
    help = "Import data from excel file"

    def handle(self, *args, **options):
        data = "data/covid1.xls"
        import_data(data)
        self.stdout.write(self.style.SUCCESS("Successfully imported data from excel file"))
