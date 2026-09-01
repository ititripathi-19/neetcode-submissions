class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)
        mid = l+h // 2
        while(mid<h):
            print(mid)
            if(target==nums[mid]):
                return mid
            elif(target<nums[mid]):
                h -= 1
            elif(target>nums[mid]):
                l += 1
            mid = l+h // 2
        return -1