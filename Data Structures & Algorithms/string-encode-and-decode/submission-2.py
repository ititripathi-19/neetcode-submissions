class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded = encoded+strs[i]
            encoded = encoded + "\n"
        # encoded = encoded.rstrip('\n')
        return encoded
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        word = ""
        for i in range(len(s)):
            if(s[i]=="\n"):
                word = word.lstrip('\n')
                decoded.append(word)
                word = ""
            word = word + s[i]
        return decoded