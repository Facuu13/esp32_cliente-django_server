# importar BaseCommand desde django.core.management
from django.core.management.base import BaseCommand
# importar timezone desde django.utils
from django.utils import timezone
# importar DataPoint desde api.models
from api.models import DataPoint

class Command(BaseCommand):
    help = 'Ingest demo data points into the database'

    def handle(self, *args, **options):
        demo_data = [
            {"source": "sensor_1", "key": "temperature", "value": 22.5},
            {"source": "sensor_2", "key": "humidity", "value": 45.0},
            {"source": "sensor_1", "key": "temperature", "value": 23.0},
            {"source": "sensor_3", "key": "pressure", "value": 1013.25},
            {"source": "sensor_2", "key": "humidity", "value": 50.0},
        ]

        for data in demo_data:
            DataPoint.objects.create(
                source=data["source"],
                key=data["key"],
                value=data["value"],
                ts=timezone.now()
            )

        self.stdout.write(self.style.SUCCESS('Successfully ingested demo data points'))