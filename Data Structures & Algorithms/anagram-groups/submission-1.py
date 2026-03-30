class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_arr = [0]*26
        myDict = {}
        for word in strs:
            for letter in word:
                index = ord(letter) - 97
                letter_arr[index] += 1
            letter_tup = tuple(letter_arr)
            if letter_tup not in myDict:
                myDict[letter_tup] = []
            myDict[letter_tup].append(word)
            letter_arr = [0]*26
        
        output = list(myDict.values())
        return output    
