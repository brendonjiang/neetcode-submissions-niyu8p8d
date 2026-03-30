class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        
        for word in strs:
            string += str(len(word)) + '#' + word
        
        return string

    def decode(self, s: str) -> List[str]:

        i = 0
        output = []

        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            i += 1
            length = int(length)
            output.append(s[i:i+length])
            i += length

        return output            