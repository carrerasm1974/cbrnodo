import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand
from base.models import Transitorio

class Command(BaseCommand):
    help = "Cargar datos desde CSV"
    
    def handle(self, *args, **options):
        datafile = settings.BASE_DIR / 'base' / 'archivos' / 'classData.csv'
        try:
            dt = pd.read_csv(datafile)
        except:
            print ("Error abriendo el archivo")

        for _,row in dt.iterrows():
            Transitorio.objects.create(
                ia = row['Ia'],
                ib = row['Ib'],
                ic = row['Ic'],
                va = row['Va'],
                vb = row['Vb'],
                vc = row['Vc'],
            )
