import csv
from models.city import City

def read_csv(filepath):
    cities = []
    try:
        with open(filepath, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                city = City(row.get('city'), row.get('lat'), row.get('lng'), row.get('country'), row.get('iso2'),
                            row.get('admin_name'), row.get('population'), row.get('population_proper'))
                cities.append(city)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return cities