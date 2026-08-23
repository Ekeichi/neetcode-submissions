class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lignes = len(matrix)
        colonnes = len(matrix[0])
        
        gauche = 0
        droite = lignes * colonnes - 1

        while gauche <= droite:

            milieu = (gauche + droite) // 2

            ligne = milieu // colonnes
            colonne = milieu % colonnes

            if matrix[ligne][colonne] == target:
                return True
            elif matrix[ligne][colonne] > target:
                droite = milieu - 1
            else:
                gauche = milieu + 1
        

        return False

        