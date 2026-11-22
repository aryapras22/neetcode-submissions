class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy, sell = 0, 0, 0

        for i in range(len(prices)):
            buy = prices[i]
            for k in range(i, len(prices)):
                sell = prices[k]
                if profit < (sell-buy):
                    profit = sell - buy

        return profit
