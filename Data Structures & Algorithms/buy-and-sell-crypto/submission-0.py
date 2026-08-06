class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProf = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if(prices[i]<prices[j]):
                    profit = prices[j] - prices[i]
                    maxProf = max(maxProf, profit)
                    print(maxProf)
        return maxProf