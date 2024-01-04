import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant.settings")
import django
django.setup()

import csv, json
from datetime import datetime
from search.models import Restaurant, Dishes

def import_restaurant(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        all_records = []
        for row in reader:
            all_records.append(Restaurant(ID=row[0], name=row[1], location=row[2], lat_long=row[4], other_details=row[5]))
        Restaurant.objects.bulk_create(all_records)

        all_dishes = []
        for row in reader:
            dishes = json.loads(row[3])
            dishes = list(dishes.items())
            ID = Restaurant.objects.get(ID=row[0])
            all_dishes += [Dishes(restaurant=ID, item=dish[0], price=dish[1]) for dish in dishes]
        Dishes.objects.bulk_create(all_dishes)
            
def import_dishes(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        all_dishes = []
        for row in reader:
            dishes = json.loads(row[3])
            dishes = list(dishes.items())
            ID = Restaurant.objects.get(ID=row[0])
            all_dishes += [Dishes(restaurant=ID, item=dish[0], price=dish[1]) for dish in dishes]
        Dishes.objects.bulk_create(all_dishes)

if __name__ == '__main__':
    csv_file_path = 'restaurants_small.csv'
    import_restaurant(csv_file_path)
    import_dishes(csv_file_path)
