from collections import defaultdict


def get_nearest_cities(num_cities, cities, x_coor, y_coor, queries_amount, queries):
    cities_coordinates = {}
    for idx, city_name in enumerate(cities):
        cities_coordinates[city_name] = (x_coor[idx], y_coor[idx])

    x_coordinate_cities = defaultdict(list)
    y_coordinate_cities = defaultdict(list)
    for city_name, coor in cities_coordinates.items():
        x = coor[0]
        y = coor[1]
        x_coordinate_cities[x].append(city_name)
        y_coordinate_cities[y].append(city_name)

    results = []
    for query_city_name in queries:
        result_distance = float('inf')
        result_city = None

        query_city_coordinate_x = cities_coordinates[query_city_name][0]
        query_city_coordinate_y = cities_coordinates[query_city_name][1]

        nearest_cities_x = x_coordinate_cities[query_city_coordinate_x]
        nearest_cities_y = y_coordinate_cities[query_city_coordinate_y]

        for nearest_city in nearest_cities_x:
            if nearest_city == query_city_name:
                continue

            nearest_city_coor_y = cities_coordinates[nearest_city][1]
            distance = abs(nearest_city_coor_y - query_city_coordinate_y)
            if distance < result_distance:
                result_distance = distance
                result_city = nearest_city

        for nearest_city in nearest_cities_y:
            if nearest_city == query_city_name:
                continue

            nearest_city_coor_x = cities_coordinates[nearest_city][0]
            distance = abs(nearest_city_coor_x - query_city_coordinate_x)
            if distance < result_distance:
                result_distance = distance
                result_city = nearest_city

        results.append(result_city)
    return results


num_cities = 3
cities = ['c1', 'c2', 'c3']
x_coor = [3, 2, 1]
y_coor = [3, 2, 3]
queries_amount = 3
queries = ['c1', 'c2', 'c3']
print(get_nearest_cities(num_cities, cities, x_coor, y_coor, queries_amount, queries))
