class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        saved = prices[0]
        profit = 0
        for price in prices:
            if price < saved:
                saved = price
            elif price - saved > profit:
                profit = price - saved
        return profit