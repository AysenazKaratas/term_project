import csv
from models.city import City
from models.map import Map
import folium

file_path = "data/cleaned_germany_city_data.csv"

cities_map = Map()

def read_csv(file_path: str) -> None:    
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            temp = City(city_name=row[0], lat=float(row[1]),lng=float(row[2]),country=row[3], iso2=row[4], population=float(row[6]))
            cities_map.add_city(temp)

read_csv(file_path)

print("1: Display City Names & Informations")
print("2: Save City Map Locations")
choice = int(input("Please enter your choice: "))

if choice == 1:
    cities_map.print_cities()
elif choice == 2:
    cities_map.save_map_locations()
else:
    print("Wrong choice!")