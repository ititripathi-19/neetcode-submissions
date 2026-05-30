class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resp = dict()
        for i in range(len(strs)):
            sort = ''.join(sorted(strs[i]))
            print(sort)
            if(sort not in resp.keys()):
                resp[sort] = [i]
            else:
                resp[sort].append(i)
        print(resp)
        finalResp = []
        for i in resp.keys():
            temp = []
            for k in resp[i]:
                temp.append(strs[k])
            finalResp.append(temp)
        print(finalResp)
        return(finalResp)
