class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            
        # Un tableau de listes vides, de taille N + 1
        seaux = [[] for _ in range(len(nums) + 1)]
        
        # On range chaque nombre dans le seau correspondant à sa fréquence
        for num, freq in dic.items():
            seaux[freq].append(num)
            
        # On parcourt les seaux en partant de la fin (plus hautes fréquences)
        resultat = []
        for i in range(len(seaux) - 1, 0, -1):
            for num in seaux[i]:
                resultat.append(num)
                if len(resultat) == k:
                    return resultat