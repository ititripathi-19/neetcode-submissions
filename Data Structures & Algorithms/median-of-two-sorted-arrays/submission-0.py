class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_nums = nums1 + nums2 
        n = len(final_nums)
        final_nums = sorted(final_nums)
        median = 0
        mid = n//2
        if(n%2==0):
            median = (final_nums[mid]+final_nums[mid-1])/2
        else:
            median = final_nums[mid]
        print (float(median))
        return float(median)