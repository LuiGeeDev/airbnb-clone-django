from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This commands says hello to me"

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, times):
            self.stdout.write(self.style.WARNING("I love you"))

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you",
            type=int,
        )
