def maxProfit(prices: [int]) -> int:
    maxProfit = 0
    buyDay = 0
    for sellDay in range(len(prices)):
        if prices[sellDay] < prices[buyDay]:
            buyDay = sellDay
        maxProfit = max(prices[sellDay]-prices[buyDay], maxProfit)
    return maxProfit


prices = [2, 3, 4, 5, 6, 1, 2, 4, 2]
print(f"Max profit is {maxProfit(prices)}")
