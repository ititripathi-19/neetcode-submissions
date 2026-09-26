class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        minV = nums[0]
        while(l<=r):
            if(nums[l]<nums[r]):
                minV = min(nums[l], minV)
                break
            mid = (l+r)//2
            #print(l,r,mid)
            minV = min(nums[mid], minV)
            if(nums[mid]>=nums[l]):
                l = mid+1
            else:
                r = mid-1
        return minV