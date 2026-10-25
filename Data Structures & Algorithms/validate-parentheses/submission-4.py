class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        if len(s) % 2 != 0: return False
        mapping = {
            "]": "[",
            ")": "(",
            "}": "{",
        }

        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and s[i] in mapping and mapping[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return len(stack) == 0