class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        compteur = Counter(nums) 

        return [element for element, frequence in compteur.most_common(k)]