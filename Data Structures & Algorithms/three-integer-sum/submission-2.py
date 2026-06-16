class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            else:
                j = i+1
                k = len(nums)-1
                while j<k:
                    threeSum = nums[i]+nums[j]+nums[k]
                    if threeSum<0:
                        j=j+1
                    elif threeSum>0:
                        k = k-1
                    elif threeSum==0:
                        res.append([nums[i],nums[j],nums[k]])
                        j = j+1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        k = k-1
        return res