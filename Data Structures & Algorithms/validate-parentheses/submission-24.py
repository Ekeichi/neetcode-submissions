class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')','{':'}','[':']'}
        tas = []

        for carac in s:
            if carac in dic:
                tas.append(carac)
            else:
                if not tas:
                    return False
                x = tas.pop()
                if dic[x] != carac:
                    return False
                
        
        return not tas