class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        hashT = {}
        for char in t:
            hashT[char] = hashT.get(char, 0) + 1

        window = {}

        l = 0
        have = 0
        need = len(hashT)

        res = [-1, -1]
        reslen = float('inf')

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in hashT and window[char] == hashT[char]:
                have += 1

            while have == need:
                if r - l + 1 < reslen:
                    res = [l, r]
                    reslen = r - l + 1

                if s[l] in hashT and window[s[l]] == hashT[s[l]]:
                    have -= 1

                window[s[l]] -= 1
                l += 1

        if res[0] == -1:
            return ""

        return s[res[0]:res[1] + 1]