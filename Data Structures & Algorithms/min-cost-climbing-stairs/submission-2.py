from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def f(i):
            if i == 0 or i == 1:
                return 0
            else:
                return min(f(i-2)+cost[i-2],f(i-1)+cost[i-1])
        
        n = len(cost)

        return f(n)
        



        