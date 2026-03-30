class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 201
        check_word = None

        for word in strs:
            length = len(word)
            if length < min_length:
                check_word = word
            min_length = min(min_length, length)

        
        output = ""
        i = 0

        for char in check_word:
            for word in strs:
                if char != word[i]:
                    return output
            output += char
            i += 1

        return output
