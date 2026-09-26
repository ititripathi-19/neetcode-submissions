class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minV = nums[0]
        for i in nums:
            if i<minV:
                minV = i
            else:
                continue
        return minV 