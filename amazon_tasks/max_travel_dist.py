def get_closest_routes(initial_dist, dist, forward_list, return_list, current_flights, result, result_int):
    if dist > initial_dist:
        return

    best_res = result_int[0]
    cur_res = initial_dist - dist
    if cur_res < best_res:
        result_int[0] = cur_res
        if len(result) > 0:
            result.pop()
        result.append(list(current_flights))

    for i in range(len(forward_list)):
        for j in range(len(return_list)):
            forward_route = forward_list.pop(i)
            return_route = return_list.pop(j)
            current_flights.append((forward_route[0], return_route[0]))

            get_closest_routes(initial_dist, dist + forward_route[1] + return_route[1], forward_list, return_list, current_flights, result, result_int)

            current_flights.pop()
            forward_list.insert(i, forward_route)
            return_list.insert(j, return_route)


max_dist = 7
forward_list = [[1, 2], [2, 4], [3, 6]]
return_list = [[1, 3], [2, 1]]
result = []
result_int = [max_dist]
get_closest_routes(max_dist, 0, forward_list, return_list, [], result, result_int)
print(result_int)
print(result)
