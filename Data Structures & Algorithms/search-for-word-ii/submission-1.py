class TrieNode:
    def __init__(self) -> None:
        self.word: str | None = None
        self.children: dict[str, TrieNode] = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children: 
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words: return []
        trie = Trie()
        for word in words: trie.insert(word)
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        found = []
        for i in range(rows):
            for j in range(cols):
                if board[i][j] not in trie.root.children: continue
                self._dfs(i, j, board, trie.root.children[board[i][j]], found, visited)
        return found

    def _dfs(
        self, 
        row: int, 
        col: int, 
        board: list[list[str]], 
        node: TrieNode, 
        found: list[str],
        visited: list[list[bool]]
    ) -> None:
        if node.word:
            found.append(node.word)
            node.word = None
        visited[row][col] = True
        for dr, dc in self._dirs():
            new_row = row + dr
            new_col = col + dc

            if (
                self._is_cell_valid(new_row, new_col, board)
                and not visited[new_row][new_col]
                and board[new_row][new_col] in node.children
            ):
                new_c = board[new_row][new_col]
                self._dfs(
                    new_row, new_col, board, node.children[new_c], 
                    found, visited
                )

        visited[row][col] = False

    @staticmethod
    def _dirs() -> list[tuple[int, int]]:
        return [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]
    
    @staticmethod
    def _is_cell_valid(row: int, col: int, board: list[list[str]]) -> bool:
        return (
            row >= 0
            and col >= 0
            and row < len(board)
            and col < len(board[0])
        )

        