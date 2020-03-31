from itertools import combinations

# choose_best_sum(230, 4, xs)
def choose_best_sum(t, k, ls):
    """

    :param t: max distance
    :param k: towns
    :param ls: towns distance
    :return:
    """
    # your code
    available = []
    combs_distance = list(combinations(ls, k))
    for e in combs_distance:
        sum_of_e = sum(e)
        if sum_of_e <= t:
            available.append(sum_of_e)
        pass
    available.sort()
    return available[-1] if len(available) > 0 else None


# 大神的解法
def choose_best_sum2(t, k, ls):
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(430, 8, xs))
