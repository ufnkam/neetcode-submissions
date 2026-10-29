import string
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset: return 0
        wordset.discard(beginWord)
        queue = deque([(beginWord, 1)])
        while queue:
            word, steps = queue.popleft()
            if word == endWord: return steps
            for ne in self._neighbours(word, wordset):
                wordset.remove(ne)
                queue.append((ne, steps + 1))
        return 0

    @staticmethod
    def _neighbours(word: str, wordset: set[str]) -> str:
        nehs = []
        for i in range(len(word)):
            for c in string.ascii_lowercase:
                if word[i] == c: continue
                candidate = word[:i] + c + word[i + 1:]
                if candidate not in wordset: continue
                nehs.append(candidate)
        return nehs

        