from django.core.management.base import BaseCommand
import pyodbc

from config.settings import DATABASE, USER, PASSWORD, HOST, DRIVER, PAD_DATABASE



class Command(BaseCommand):
    help = 'Create the database'

    def handle(self, *args, **options):

        ConnectionString = f'''DRIVER={{{DRIVER}}};
        SERVER={HOST};
        DATABASE={PAD_DATABASE};
        UID={USER};
        PWD={PASSWORD};
        TrustServerCertificate=yes;
        Encrypt=no'''

        try:
            conn = pyodbc.connect(ConnectionString)
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            conn.autocommit = True
            try:
                conn.execute(fr"CREATE DATABASE {DATABASE};")
            except pyodbc.ProgrammingError as ex:
                print(ex)
            else:
                print(f"База данных {DATABASE} успешно создана")
