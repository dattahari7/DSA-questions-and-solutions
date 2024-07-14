# Introduction to DP


class Solution:
    
    def __init__(self):
        self.mod = 10 ** 9 + 7
    def topDown(self, n):
        # Code here
        
        def fab(n, dp):
            dp[0] = 0
            dp[1] = 1
            
            for i in range(2, n + 1):
                dp[i] = (dp[i-1] + dp[i-2]) % self.mod
            
            return dp[n]
            
        dp = [-1] * (n + 1)
        return fab(n, dp)
            
        
    def bottomUp(self, n):
        # Code here
        
        if n <= 1:
            return n
        prev2, prev1= 0, 1
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1 % self.mod
    
# Time Complexity: O(n)
# Space Complexity: O(n)