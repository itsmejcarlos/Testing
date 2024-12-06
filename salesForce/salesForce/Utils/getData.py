import os
import csv


class GetData:
    def get_data(self):
        ruta=""
        try:
            ruta="D:\\evidencias\\text.csv"
            with open(ruta) as data:
                lines = csv.DictReader(data)
                db = {}
                for row in lines:
                    db['sim'] = row['Sim']
                    db['IMEI'] = row['IMEI']
                print(db)
        except FileNotFoundError:
            print("Archivo no encontrado en ruta: "+ ruta)

gd = GetData()

gd.get_data()
