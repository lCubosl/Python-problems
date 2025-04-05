city_map =  {}

cities = ["calgary", "Vancouver", "Toronto"]
city_map["Canada"] = []
city_map["Canada"] += cities

city_map["USA"] = []
cities = ["New York", "Austin", "Seatle"]
city_map["USA"] += cities

city_map["Portugal"] = []
cities = ["Lisboa", "Leiria", "Porto"]
city_map["Portugal"] += cities

city_list = city_map.values()

print(city_map)
print(city_list)