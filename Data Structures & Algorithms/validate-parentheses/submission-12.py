class Solution:
    def isValid(self, s: str) -> bool:
        invert = []

        for i in s:
            if i == "(":
                invert.append(")")
            elif i == "{":
                invert.append("}")
            elif i == "[":
                invert.append("]")
            else:
                if not invert or i != invert.pop():
                    return False
            
        return len(invert) == 0
