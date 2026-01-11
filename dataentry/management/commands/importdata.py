import csv
from django.core.management.base import BaseCommand
# from dataentry.models import Student
from django.apps import apps
from django.db import DataError

from dataentry.utils import check_csv_errors
# #proposed command -python manage.py importdata file_path
# class Command(BaseCommand):

#     help='inserting/importing data from csv file'

#     def add_arguments(self, parser):
#         parser.add_argument('filepath',type=str,help='Path to the csv file')
        
#     def handle(self, *args, **kwargs):
#         #logic goes here
#         file_path=kwargs['filepath']
#         with open(file_path,'r') as file:
#             reader=csv.DictReader(file)
#             for row in reader:
#                 Student.objects.create(**row)
      
#         self.stdout.write(self.style.SUCCESS('Data imported from csv successfully'))

# import data to any model 

#proposed command -python manage.py importdata file_path model_name
class Command(BaseCommand):

    help='inserting/importing data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('filepath',type=str,help='Path to the csv file')
        parser.add_argument('model_name', type=str, help='Name of the Model')

        
    def handle(self, *args, **kwargs):
        #logic goes here
        file_path=kwargs['filepath']
        model_name=kwargs['model_name'].capitalize()

        #Search for models across all installed apps
        # model=None
        # for app_config in apps.get_app_configs():
        #     #Try to search for the model 
        #     try:
        #         model=apps.get_model(app_config.label,model_name)
        #         break # stop searching once the model is found
        #     except LookupError:
        #         continue # model not found in this app, continue searching in next app.

        # if not model:
        #     raise CommandError(f"Model '{model_name}' not found in any app'!")

        #get all the field names of the model that we found 
        # model_fields=[field.name for field in model._meta.fields if field.name !='id']

        # with open(file_path,'r') as file:
        #     reader=csv.DictReader(file)
        #     csv_header=reader.fieldnames
        #     #compare csv header with model's field names
        #     if csv_header!=model_fields:
        #         raise DataError(f"CSV file doesn't match with the {model_name} table fields")
        model = check_csv_errors(file_path, model_name)

        with open(file_path,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
      
        self.stdout.write(self.style.SUCCESS('Data imported from csv successfully'))
