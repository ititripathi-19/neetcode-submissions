class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        found = []
        for row in matrix:
            if(target>=row[0] and target<=row[n-1]):
                found = row
            else:
                continue
        l = 0
        h = len(found)-1
        #print(found)
        #print(l,h)
        while(l<=h):
            mid = (l+h)//2
            if(target==found[mid]):
                return True
            elif(target>found[mid]):
                l=mid+1
            elif(target<found[mid]):
                h=mid-1
        return False