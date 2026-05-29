class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        resp = dict()
        for i in nums:
            if i in resp.keys():
                return True
            else:
                resp[i] = 1
        return False