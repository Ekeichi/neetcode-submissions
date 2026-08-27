from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        target_count = Counter(s1)

        for right in range(len(s1),len(s2)+1):
            window_count = Counter(s2[left:right])
            if target_count == window_count:
                return True
            
            left += 1
            
        
        return False