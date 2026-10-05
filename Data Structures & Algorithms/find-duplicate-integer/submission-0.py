class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hmap = {}
        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                return i
        
        