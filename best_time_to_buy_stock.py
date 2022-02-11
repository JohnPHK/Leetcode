class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy_index]:
                buy_index = i
            elif prices[i] - prices[buy_index] > profit:
                profit = prices[i] - prices[buy_index]
                

        
        return profit
