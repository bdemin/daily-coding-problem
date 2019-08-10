# Given a array of numbers representing the stock prices of a company
# in chronological order, write a function that calculates the maximum
# profit you could have made from buying and selling that stock once.
# You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5,
# since you could buy the stock at 5 dollars and sell it at 10 dollars.


# Brute force solution:
def calc_max_profit(stock_prices):
    max_profit = 0
    for i in range(len(stock_prices)):
        buy_price = stock_prices[i]
        for j in range(i+1, len(stock_prices)):
            sell_price = stock_prices[j]

            if sell_price - buy_price > max_profit:
                max_profit = sell_price - buy_price

    return max_profit


# Driver code
stock_prices = [9, 11, 8, 5, 7, 10]
assert calc_max_profit(stock_prices) == 5
