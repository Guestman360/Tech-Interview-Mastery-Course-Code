# Brute Force
def maxProfit(self, prices):
    max_profit = 0

    for i in range(0, len(prices):
        for j in range(0, len(prices):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

# Final Solution
def maxProfit(self, prices):
    if len(prices)==0: return 0
    if len(prices)==1: return 0
        curMax=prices[len(prices)-1]
        maxP=0
        for i in range(len(prices)):
            temp=prices[len(prices)-i-1]
            if temp>curMax:
                curMax=temp
            curProfit=curMax-temp
            if curProfit>maxP:
                maxP=curProfit
        return maxP