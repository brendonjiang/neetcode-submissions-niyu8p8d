class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        output = defaultdict(list)

        for word in strs:
            tup = [0 for _ in range(26)]
            for char in word:
                print(tup)
                idx = ord("z") - ord(char)
                print(idx)
                print(ord("z"), ord(char))
                tup[idx] += 1

            output[tuple(tup)].append(word)

        return list(output.values())