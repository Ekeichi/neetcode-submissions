class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(st)}#{st}" for st in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        # On parcourt la chaîne encodée avec un pointeur i
        while i < len(s):
            # 1. On cherche où se trouve le prochain '#' en partant de i
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. Le nombre entre i et j est la longueur du mot à extraire
            longueur = int(s[i:j])
            
            # 3. Le mot commence juste après le '#' (j + 1) et s'arrête après sa longueur
            debut_mot = j + 1
            fin_mot = debut_mot + longueur
            
            res.append(s[debut_mot:fin_mot])
            
            # 4. On déplace notre pointeur i au début du prochain bloc
            i = fin_mot
            
        return res