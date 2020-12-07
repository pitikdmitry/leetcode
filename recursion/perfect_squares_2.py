from math import sqrt


def get_squares(n, squares, current_squares, result):
    if n == 0:
        #   found result
        if len(result) == 0:
            result.append(list(current_squares))
        elif len(current_squares) < len(result[0]):
            result.pop()
            result.append(list(current_squares))
        return
    if n < 0:
        #   return error
        return

    for num in squares:
        current_squares.append(num)
        get_squares(n - num, squares, current_squares, result)
        current_squares.pop()


n = 18
squares = [x ** 2 for x in range(1, int(sqrt(n)) + 1)]
result = []
get_squares(n, squares, [], result)
print(result)
