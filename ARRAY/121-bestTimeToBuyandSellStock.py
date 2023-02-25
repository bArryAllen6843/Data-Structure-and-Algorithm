def solve(prices):
    max_profit = 0
    min_price_till_now = 99999
    for price in prices:
        max_profit = max(max_profit, price - min_price_till_now)
        min_price_till_now = min(min_price_till_now, price)
    return max_profit


if __name__ == '__main__':
    a = [4, 7, 2, 6, 9, 3, 11]
    print("Maximum profit : " + str(solve(a)))
