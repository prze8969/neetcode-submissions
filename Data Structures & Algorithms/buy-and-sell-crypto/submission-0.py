class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float('inf')
        maxx = 0
        for price in prices:
            if price < minn:
                minn=price
            elif price - minn > maxx:
                maxx = price - minn
        return maxx
        