class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        length = 0
        res, line = [], []
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                remaining_space = maxWidth - length
                spaces = remaining_space // max(1, len(line)-1)
                extras = remaining_space % max(1, len(line)-1)

                for j in range(max(1, len(line)-1)):
                    line[j] += " " * spaces
                    if extras != 0:
                        line[j] += " "
                        extras -= 1

                res.append("".join(line))
                line, length = [], 0

            line.append(words[i])
            length += len(words[i])
            i += 1

        line = " ".join(line)
        remaining_spaces = maxWidth - len(line)
        line += " " * remaining_spaces
        res.append(line)

        return res
