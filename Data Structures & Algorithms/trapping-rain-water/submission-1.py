class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        max_l = [0] * (len(height))
        max_r = [0] * (len(height))
        for i in range(1,len(height)):
            max_l[i] = max(height[i-1],max_l[i-1])
        for i in range(len(height)-2,-1,-1):
            max_r[i] = max(height[i+1],max_r[i+1])
        for i in range(len(height)):
            water = min(max_l[i],max_r[i]) - height[i]
            if(water>=0):
                total = total+water
        print(total)
        return total