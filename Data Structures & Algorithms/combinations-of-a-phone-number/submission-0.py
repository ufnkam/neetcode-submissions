class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        combs, curr_comb = [], []
        self._backtrack(digits, 0, digit_map, curr_comb, combs)
        return combs

    def _backtrack(
        self,
        digits: str,
        index: int,
        digit_map: dict[str, list[str]],
        curr_comb: list[list[str]],
        combs: list[str],
    ) -> None:
        if index == len(digits):
            combs.append("".join(curr_comb))
            return
        for c in digit_map[digits[index]]:
            curr_comb.append(c)
            self._backtrack(digits, index + 1, digit_map, curr_comb, combs)
            curr_comb.pop()


        


