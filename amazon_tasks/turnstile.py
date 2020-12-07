def get_time(input_times, directions):
    enter_queue = []
    exit_queue = []
    for idx in range(len(directions)):
        direction = directions[idx]
        if direction == 0:
            enter_queue.append(idx)
        else:
            exit_queue.append(idx)

    result = [-1 for i in range(len(input_times))]
    current_time = 0
    previous_time = -10
    previous_dir = 0
    while len(enter_queue) > 0 and len(exit_queue) > 0:
        enter_idx = enter_queue[0]
        enter_time = input_times[enter_idx]
        exit_idx = exit_queue[0]
        exit_time = input_times[exit_idx]
§§
        current_time = max(current_time, exit_time)
        time_diff = current_time - previous_time
        if time_diff > 1:
            result[exit_idx] = current_time
            exit_queue.pop(0)
            previous_dir = 1
        else:
            if previous_dir == 0:
                result[enter_idx] = current_time
                enter_queue.pop(0)
                previous_dir = 0
            else:
                result[exit_idx] = current_time
                exit_queue.pop(0)
                previous_dir = 1

        previous_time = current_time
        current_time += 1

    return result

# t = [0, 1, 1, 1, 3]
t = [0, 0, 1, 5]
d = [0, 1, 1, 0]
print(get_time(t, d))



