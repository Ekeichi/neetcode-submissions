class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        for right in range(len(s1),len(s2)+1):
            if sorted(s1) == sorted(s2[left:right]):
                return True
            else:
                left += 1
        
        return False