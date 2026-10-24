class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}

        stack = []

        for char in s:
            if len(stack) > 0 and char in mapping and stack[-1] == mapping[char]:
                stack.pop()
            else:
                stack.append(char)


        return True if not stack else False
