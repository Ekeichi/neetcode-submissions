class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        tri_decroissant = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    
        return [cle for cle, valeur in tri_decroissant[:k]]