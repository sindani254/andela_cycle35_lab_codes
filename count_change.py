def count_change(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]


print(count_change(100, [1, 5, 10, 25]))
print(count_change(100000, [1, 5, 10, 25, 50, 100]))
