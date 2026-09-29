class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1

        sorted_items = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return [num for num, count in sorted_items[:k]]
            