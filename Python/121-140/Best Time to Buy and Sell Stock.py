class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for p in prices:
            maxprofit = max(p - minprice, maxprofit)
            minprice = min(p, minprice)
        return maxprofit
