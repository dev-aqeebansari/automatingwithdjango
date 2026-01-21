from django.core.management.base import BaseCommand
from stockanalysis.models import Stock

class Command(BaseCommand):
    help = "Delete all Stock records"

    def handle(self, *args, **kwargs):
        Stock.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Stocks deleted successfully"))
