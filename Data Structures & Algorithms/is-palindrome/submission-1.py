class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.split(" ")
        print(st)
        st = "".join(st)
        j = len(st)-1
        flag = True
        for i in range(len(st)):
            if(st[i].isalnum()):
                if(st[j].isalnum()):
                    if(st[i].lower()==st[j].lower()):
                        j=j-1
                    else:
                        flag = False
                        break
                else:
                    j=j-1
                    if(st[i].lower()==st[j].lower()):
                        j=j-1
                    else:
                        flag = False
                        break
        print(len(st))
        print(st)
        print(flag)
        return flag
        