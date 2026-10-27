class TrieNode:
    def __init__(self) -> None: 
        self.children = {}
        self.is_end = False
    

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end
    
    def _find(self, prefix: str) -> TrieNode | None:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node
        
    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None
        