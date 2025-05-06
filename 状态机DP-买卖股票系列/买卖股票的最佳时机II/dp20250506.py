class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=[0]*(len(prices)-1)
        for i in range(len(prices)-1):
            res[i]=prices[i+1]-prices[i]
        return sum([r for r in res if r>0])

        