class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)==len(t)):
            dictS = dict()
            dictT = dict()
            for i in range(len(s)):
                if(s[i] in dictS.keys()):
                    dictS[s[i]] += 1
                if(s[i] not in dictS.keys()):
                    dictS[s[i]] = 1
                if(t[i] in dictT.keys()):
                    dictT[t[i]] += 1
                if(t[i] not in dictT.keys()):
                    dictT[t[i]] = 1
            if dictS == dictT:
                return True
            else:
                return False
        else:
            return False