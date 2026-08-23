class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [x for ligne in matrix for x in ligne]

        gauche = 0
        droite = len(flat) - 1

        while gauche <= droite:

            milieu = (gauche + droite) // 2

            if flat[milieu] == target:
                return True
            elif flat[milieu] > target:
                droite = milieu - 1
            else:
                gauche = milieu + 1
        

        return False

        