import heapq

def get_koef(five_star_amount, total):
    return ((five_star_amount + 1) / (total + 1)) - (five_star_amount / total)


def count_steps(ratings, threshold):
    max_heap = []

    current_rating_sum = 0
    for rating in ratings:
        current_rating_sum += rating[0] / rating[1]
        koef = get_koef(rating[0], rating[1])
        heapq.heappush(max_heap, (-koef, rating[0], rating[1]))

    current_rating = current_rating_sum / len(ratings)
    steps = 0
    while current_rating < threshold:
        _, five_star_amount, total_amount = heapq.heappop(max_heap)
        current_rating_sum -= (five_star_amount / total_amount)
        five_star_amount += 1
        total_amount += 1
        current_rating_sum += (five_star_amount / total_amount)
        current_rating = current_rating_sum / len(ratings)
        heapq.heappush(max_heap, (-get_koef(five_star_amount, total_amount), five_star_amount, total_amount))
        steps += 1

    return steps


ratings = [[4, 4], [1, 2], [3, 6]]
threshold = 0.77
print(count_steps(ratings, threshold))
