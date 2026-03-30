class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        myLetters = {2:["a", "b", "c"], 3:["d", "e", "f"], 4: ["g", "h", "i"], 5:["j", "k", "l"], 6:["m", "n", "o"], 7:["p", "q", "r", "s"], 8:["t", "u", "v"], 9:["w", "x", "y", "z"]}
        if digits == "":
            return []
        
        def helper(i, curset):
            if i == len(digits):
                combs.append("".join(curset.copy()))
                return

            
            for j in range(len(myLetters[int(digits[i])])):
                curset.append(myLetters[int(digits[i])][j])
                helper(i+1, curset)
                curset.pop()

            return

        combs = []
        helper(0, [])

        return combs