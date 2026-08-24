class Solution:
    def climbStairs(self, n: int) -> int:
            
        if n <= 2:
            return max(0, n)
    
        one_step_behind = 2  # represents dp[i-1]
        two_steps_behind = 1 # represents dp[i-2]
        
        for i in range(3, n + 1):
            current = one_step_behind + two_steps_behind
            two_steps_behind = one_step_behind
            one_step_behind = current
            
        return one_step_behind