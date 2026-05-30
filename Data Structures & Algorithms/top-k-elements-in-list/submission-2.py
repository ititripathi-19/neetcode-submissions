class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resp = dict()
        for i in range(len(nums)):
            if nums[i] not in resp:
                resp[nums[i]] = 1
            else:
                resp[nums[i]] += 1
        print(resp.items())
        sort = dict(sorted(resp.items(), key=lambda item:item[1], reverse=True))
        print(sort)
        return list(sort.keys())[0:k]