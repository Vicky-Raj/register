from django.core.management.base import BaseCommand
import pandas as pd
from home.models import Record

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        sheet = pd.read_excel('home/sheets/a2.xlsx')
        for i in range(107):
            record = Record()
            record.current = sheet['current'][i]
            record.place = sheet['place'][i]
            record.zone = sheet['zone'][i]
            record.save()
            print(sheet['current'][i])