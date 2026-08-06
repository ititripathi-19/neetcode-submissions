class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        maxProf = 0
        while(r<len(prices)):
            if(prices[l]<prices[r]):
                maxProf = max(maxProf, prices[r]-prices[l])
                r = r+1
            else:
                l = r
                r = r+1
            print(maxProf)
        return maxProf