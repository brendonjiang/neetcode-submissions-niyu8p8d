from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False
        note = defaultdict(int)
        mag = defaultdict(int)

        for char in ransomNote:
            note[char] += 1
        
        for char in magazine:
            mag[char] += 1

        for char, freq in note.items():
            if freq > mag[char]:
                return False

        return True
        