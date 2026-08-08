class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = [0]*26
        for i in s1:
            s1freq[ord(i)-ord('a')] += 1
        wind = len(s1)
        #print(s1freq)
        for i in range(0,len(s2)-wind+1):
            subfreq = [0]*26
            substr = s2[i:i+wind]
            print(substr)
            for x in substr:
                subfreq[ord(x)-ord('a')] += 1
            #print(subfreq)
            if s1freq == subfreq:
                return True
        return False