class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(filter(str.isalnum, s))
        s1 = list(s)
        n = len(s1)

        slow, fast = 0, n - 1
        while slow <= fast:
            slow_val = s1[slow]
            s1[slow] = s1[fast]
            s1[fast] = slow_val

            slow += 1
            fast -= 1
        
        output = "".join(s1)

        return output == s

        