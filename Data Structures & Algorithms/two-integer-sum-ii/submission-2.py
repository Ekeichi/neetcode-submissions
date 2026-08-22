class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        for i in range(len(numbers)):
            sum = numbers[left] + numbers[right]
            if sum == target:

                return [left +1 ,right +1 ]
            
            else:

                if sum >= target:
                    right -= 1
                else:
                    left += 1