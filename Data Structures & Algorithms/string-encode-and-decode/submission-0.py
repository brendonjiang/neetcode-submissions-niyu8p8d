class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s += str(len(word)) + '#' + word
        return s
        
    def decode(self, s: str) -> List[str]:
        i = 0
        arr = []
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1

            length = int(length)
            i += 1
            arr.append(s[i:i+length])
            i += length
        return arr

