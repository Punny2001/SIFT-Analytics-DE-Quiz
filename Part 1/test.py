def count_ways_to_make_amount(coins, amount):
    ways = [0] * (amount + 1)
    ways[0] = 1  # One way to make zero amount (use no coins)

    for coin in coins:
        for x in range(coin, amount + 1):
            ways[x] += ways[x - coin]
    
    return ways

# Define the coins in stang
coins = [25, 50, 100, 200, 500, 1000]
# Define the amount in stang
amount = 1000

# Get the number of ways to make the amount
number_of_ways = count_ways_to_make_amount(coins, amount)
print(number_of_ways)