from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        def is_adjacent(begin, end):
            k = 1
            i = 0
            j = 0
            for i in range(len(begin)):
                if begin[i] != end[j]:
                    k -= 1
                if k < 0:
                    return False
                j += 1

            return True
        
    
        seen = {beginWord}
        queue = deque([(beginWord, 1)])
        while queue:
            word, steps = queue.popleft()
            for another_word in wordList:
                if is_adjacent(word, another_word) and another_word not in seen:
                    if another_word == endWord:
                        return steps + 1
                    seen.add(another_word)
                    queue.append((another_word, steps + 1))

        return 0