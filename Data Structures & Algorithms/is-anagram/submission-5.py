class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for ele in s:
            if ele in count:
                count[ele] += 1
            else:
                count[ele] = 1
        
        for ele in t:
            if ele in count:
                count[ele] -= 1
            else:
                return False
        
        for val in count.values():
            if val != 0:
                return False
        
        return True
