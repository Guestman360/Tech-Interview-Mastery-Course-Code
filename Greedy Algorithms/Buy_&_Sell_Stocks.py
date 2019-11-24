# Brute Force
def maxProfit(prices):
  max_profit = 0

  for i in range(0, len(prices)):
      for j in range(0, len(prices)):
          profit = prices[j] - prices[i]
          if profit > max_profit:
              max_profit = profit
  return max_profit

# Final Solution
def maxProfit(prices):
  if len(prices) <= 1:
      return 0
  profit = 0
  low = prices[0]
  for i in range(1,len(prices)):
      if prices[i] < low:
          low = prices[i]
      else:
          profit = max(prices[i]-low, profit)
  return profit