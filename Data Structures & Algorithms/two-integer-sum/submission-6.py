class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = {}

        for i, num in enumerate(nums):
            reste = target - num
        
            if reste in dico:
                return [dico[reste], i]
            else:
                dico[num] = i
