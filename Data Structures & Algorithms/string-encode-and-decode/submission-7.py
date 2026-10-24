class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "%xd%"
        return "%%".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "%xd%":
            return []
        if not s:
            return [""]
        return s.split("%%")
