class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # On compare les deux chaînes une fois triées
        return sorted(s) == sorted(t)

        