class Solution:
    def search(self, nums: List[int], target: int) -> int:
        gauche = 0
        droite = len(nums) - 1

        while gauche <= droite:
            milieu = (gauche + droite) // 2

            if nums[milieu] == target:
                return milieu
            elif nums[milieu] > target:
                droite = milieu - 1
            else:
                gauche = milieu + 1
            
        return -1
            
