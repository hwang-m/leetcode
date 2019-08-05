class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        maxprofit = 0
        for i, p in enumerate(prices[1:]):
            if p > prices[i]:
                maxprofit += p - prices[i]
        
        return maxprofit
