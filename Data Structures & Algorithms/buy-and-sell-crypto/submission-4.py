class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        size = len(prices)
        for i, p in enumerate(prices):
            lowest = p
            highest = max(prices[i:size])
            profit = max(profit, highest-lowest)
        
        return profit
