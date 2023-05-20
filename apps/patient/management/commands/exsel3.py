from django.core.management.base import BaseCommand

from apps.common.uttils import  import_data3


class Command(BaseCommand):
    help = "Import data from excel file"

    def handle(self, *args, **options):
        data = "data/covid3.xls"
        import_data3(data)
        self.stdout.write(self.style.SUCCESS("Successfully imported data from excel file"))
