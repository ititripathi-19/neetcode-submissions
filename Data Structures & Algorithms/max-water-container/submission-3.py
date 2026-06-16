class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxProd = 0
        while(i<j):
            prod = (j-i) * min(heights[i],heights[j])
            if(heights[i]<heights[j]):
                i = i+1
            elif(heights[i]>heights[j]):
                j = j-1
            else:
                i = i+1
                j = j-1
            maxProd = max(maxProd, prod)
        return maxProd
