class TrieNode:
    def __init__(self) -> None:
        self.is_end = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for idx, c in enumerate(word):
            if c not in node.children and c != ".": return False
            if c == ".": return self._backtrack(word, node, idx)
            node = node.children[c]
        return node is not None and node.is_end

    def _backtrack(self, word: str, node: TrieNode, index: int) -> bool:
        if index == len(word):
            return node.is_end
        c = word[index]
        if c == ".":
            for child in node.children:
                if self._backtrack(word, node.children[child], index + 1):
                    return True
            return False
        if c not in node.children: return False
        return self._backtrack(word, node.children[c], index + 1)
        
