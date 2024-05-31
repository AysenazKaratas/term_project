from .city import City
import folium

class Map:
    def __init__(self):
        self.cities_map = []

    def add_city(self, city_to_add : City):
        self.cities_map.append(city_to_add)

    def print_cities(self):
        if len(self.cities_map) == 0:
            print("Map is empty!")
        else:
            for city in self.cities_map:
                print("""
                Country: {}, {}
                City: {}
                latitude: {}
                longitude: {}
                Population: {}
                """.format(city.country, city.iso2, city.city_name, city.lat, city.lng, city.population))


    def save_map_locations(self):
        if len(self.cities_map) == 0:
            print("Map is empty!")
        else:
            for city in self.cities_map:
                my_map = folium.Map([city.lat,city.lng], zoom_start=12)
                folium.Marker(
                    location=[city.lat, city.lng],
                    tooltip="Your Location",
                    popup=f"{city.city_name}",
                ).add_to(my_map)
                my_map.save("assets/cities/{}.html".format(city.city_name))