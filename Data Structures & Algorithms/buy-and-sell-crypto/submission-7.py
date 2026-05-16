class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        buy = prices[0]
        for price in prices:
            if price < buy: buy = price
            else:
                maxProf = max(maxProf, price - buy)
        return maxProf