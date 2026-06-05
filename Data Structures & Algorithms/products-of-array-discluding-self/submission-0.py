class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        resp = []
        pre = [1] * n
        suf = [1] * n 
        for i in range(1,n):
            pre[i] = nums[i-1]*pre[i-1] 
            suf[n-i-1] = nums[n-i]*suf[n-i]
        
        for i in range(n):
            resp.append(pre[i]*suf[i])

        return resp