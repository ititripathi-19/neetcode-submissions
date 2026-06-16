class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxProd = 0
        for i in range(len(heights)-1):
            prod=1
            for j in range(i+1,len(heights)):
                prod = (j-i)*(min(heights[i], heights[j]))
                # print(prod)
                maxProd = max(prod,maxProd)
        return maxProd