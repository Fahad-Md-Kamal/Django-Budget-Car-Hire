# Deleveoped
# Fahad Md Kamal
# NCC ID: 00171328

from django.apps import AppConfig


class FleetConfig(AppConfig):
    name = 'fleet'

    def ready(self):
        import fleet.signals
   
