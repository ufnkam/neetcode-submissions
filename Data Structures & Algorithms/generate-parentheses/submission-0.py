class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs, curr_comb = [], []
        self._backtrack(0, 0, n, curr_comb, combs)
        return ["".join(comb) for comb in combs]

    def _backtrack(
        self,
        opened: int,
        closed: int,
        n: int,
        curr_comb: list[str],
        combs: list[str],
    ) -> None:
        if len(curr_comb) == n * 2:
            combs.append(curr_comb.copy())
            return

        if opened < n:
            curr_comb.append("(")
            self._backtrack(opened + 1, closed, n, curr_comb, combs)
            curr_comb.pop()

        if closed < opened:
            curr_comb.append(")")
            self._backtrack(opened, closed + 1, n, curr_comb, combs)
            curr_comb.pop()
