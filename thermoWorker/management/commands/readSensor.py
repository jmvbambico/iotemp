from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core.management import BaseCommand
import time
import random

class Command(BaseCommand):
    help = "Simulate reading sensor from database and broadcast over channel."

    def handle(self, *args, **options):
        layer = get_channel_layer()

        while True:
            temp = random.randint(0,100)

            async_to_sync(layer.group_send)(
                'thermo',
                {
                    'type'    : 'temp_read',
                    'message' : temp
                }
            )

            time.sleep(10)
            self.stdout.write("Sensor reading: " + str(temp))