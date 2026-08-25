class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        correspondance = { '(': ')', '{': '}', '[': ']' }
        invert = []
        
        for char in s:
            if char in correspondance:
                invert.append(correspondance[char])
            else:
                if not invert or char != invert.pop():
                    return False
                    
        return not invert
