class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        myMap = {}
        i = 1
        for char in order:
            myMap[char] = i
            i += 1

        i, j = 0, 1

        while j <= len(words)-1:
            if words[i] == words[j]:
                i += 1
                j += 1
                continue

            if len(words[j]) < len(words[i]):
                if words[j] == words[i][:len(words[j])]:
                    return False

            if len(words[j]) > len(words[i]):
                if words[i] == words[j][:len(words[i])]:
                    i += 1
                    j += 1

                    continue

            for k in range(min(len(words[i]), len(words[j]))):
                if myMap[words[i][k]] < myMap[words[j][k]]:
                    i += 1
                    j += 1

                    break

                elif myMap[words[i][k]] > myMap[words[j][k]]:
                    return False

        return True
