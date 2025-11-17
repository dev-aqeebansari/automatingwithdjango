from django.core.management.base import BaseCommand



#Proposed command = python manage.py greeting John
#Proposed output = Hi {name}, Good morning
class Command(BaseCommand):
    help="Greets the user"


    def add_arguments(self, parser):
        parser.add_argument('username',type=str,help='specifies user name')

    def handle(self, *args, **kwargs):
        # write the logic
        name=kwargs['username']
        greeting=f'Hi {name}, Good Morning! '
        # print(kwargs)
        self.stdout.write(greeting)
        self.stderr.write(greeting)
        self.stderr.write(self.style.WARNING(greeting))
        self.stderr.write(self.style.SUCCESS(greeting))

        




