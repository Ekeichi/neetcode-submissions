class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        one_step=0
        two_step=0

        for i in range(2, n+1):
            current =  min(one_step+cost[i-1],two_step+cost[i-2])
            two_step = one_step
            one_step = current

        return one_step
        