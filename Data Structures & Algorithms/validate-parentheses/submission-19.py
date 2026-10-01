class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if pairs[x] != char:
                    return False

        return not stack