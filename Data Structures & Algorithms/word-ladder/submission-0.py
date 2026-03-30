from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        
        queue = deque()
        queue.append(beginWord)
        length = 1
        visits = set()

        while queue:

            for _ in range(len(queue)):
                word = queue.popleft()
                visits.add(word)
                if word == endWord:
                    return length

                for i in range(len(word)):
                    original = word[i]

                    for c in range(ord("a"), ord("z")+1):
                        ch = chr(c)
                        if ch == original:
                            continue
                        
                        new_word = word[:i] + ch + word[i+1:]
                        if new_word in wordList and new_word not in visits:
                            queue.append(new_word)

                print(queue)

            length += 1

        return 0