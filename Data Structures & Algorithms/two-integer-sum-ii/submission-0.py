class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashSet = {}
        res = []
        for i in range(len(numbers)):
            if numbers[i] not in hashSet.keys():
                hashSet[target-numbers[i]] =  i+1
            else:
                print(hashSet)
                print('IN ELSE BABE', numbers[i])
                res.append(hashSet[numbers[i]])
                res.append(i+1)
                break
        print(hashSet)
        return res       