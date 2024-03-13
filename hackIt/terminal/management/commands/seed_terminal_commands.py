from typing import Any
from django.core.management import BaseCommand
from django_seed import Seed


from models import TerminalCommands

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        seeder = Seed.seeder()

        seeder.add_entity(TerminalCommands,1,{
            'command':'zap',
            'action':'zap.sh -daemon -quickurl'
        })
        seeder.add_entity(TerminalCommands,1,{
            'command':'zap',
            'action':'zap.sh -daemon -quickurl'
        })