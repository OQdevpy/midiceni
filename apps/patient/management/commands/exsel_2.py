from django.core.management.base import BaseCommand

from apps.common.uttils import import_data2


class Command(BaseCommand):
    help = "Import data from excel file"

    def handle(self, *args, **options):
        data = "data/covid2.xls"
        import_data2(data)
        self.stdout.write(self.style.SUCCESS("Successfully imported data from excel file"))
