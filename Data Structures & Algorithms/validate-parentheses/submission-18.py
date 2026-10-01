class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if x == "(":
                    if char != ")":
                        return False
                if x == "{":
                    if char != "}":
                        return False
                if x == "[":
                    if char != "]":
                        return False

        return len(stack) == 0