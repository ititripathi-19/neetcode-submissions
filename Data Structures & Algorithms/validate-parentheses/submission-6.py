class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        resp = True
        if len(s)==1:
            return False

        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                x = ''
                if stack:
                    x  = stack.pop()
                if i==')' and x == '(':
                    continue
                elif i=='}' and x == '{':
                    continue
                elif i==']' and x == '[':
                    continue
                else:
                    resp = False
                    break
        if resp and len(stack)==0:
            resp = True
        else:
            resp = False 
        return resp