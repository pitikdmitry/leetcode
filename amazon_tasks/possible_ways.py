from math import sqrt


def is_prime(s):
    nums_s = int(s)
    if nums_s == 1:
        return False
    for i in range(2, int(sqrt(nums_s) + 2)):
        if nums_s % i == 0:
            return False
    return True


def possible_ways(s, i, current_sequence):
    if i == len(s):
        print(current_sequence)
        return

    for last_symbol in range(i, len(s)):
        current_s = s[i:last_symbol + 1]
        if is_prime(current_s) is True:
            current_sequence.append(int(current_s))
            possible_ways(s, last_symbol + 1, current_sequence)
            current_sequence.pop()

    return


possible_ways('3175', 0, [])
