from collections import defaultdict


def totalFruits(fruits):
    basket = defaultdict(int)
    j = 0
    i = 0
    res = 0
    for i in range(len(fruits)):
        basket[fruits[i]] += 1
        while len(basket) > 2:
            basket[fruits[j]] -= 1
            if basket[fruits[j]] == 0:
                del basket[fruits[j]]
            j += 1
        res = max(res, i - j + 1)
    return res


if __name__ == '__main__':
    a = [1, 2, 3, 2, 2]
    print(totalFruits(a))
