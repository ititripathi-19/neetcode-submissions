class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers)-1
        i = 0
        nsum = numbers[i]+numbers[j]
        while ( nsum != target ):
            if(nsum<target):
                i=i+1
            if(nsum>target):
                j=j-1
            nsum = numbers[i]+numbers[j]
            print(i,j,nsum)
        return [i+1,j+1]