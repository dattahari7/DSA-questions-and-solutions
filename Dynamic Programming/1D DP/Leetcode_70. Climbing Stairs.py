# 70. Climbing Stairs

# Brute Force Solution (using Recursion)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# Time Complexity: O(n!)
# Space Complexity: O(n)


# Optimal Solution (using Dp memoization)

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n, dp):
            # Base case: if n is 0 or 1, there is only 1 way to climb
            if n <= 1:
                return 1
            # If the result is already computed, return it
            if dp[n] != -1:
                return dp[n]
            # Recursively calculate the number of ways to climb the current step
            dp[n] = climb(n-1, dp) + climb(n-2, dp)
            return dp[n]
        
        # Initialize the dp array with -1 for all positions
        dp = [-1] * (n + 1)
        # Call the climb function starting from step n
        return climb(n, dp)



# Time Complexity: O(n)
# Space Complexity: O(n) + O(n) ~= O(n)


# Optimal Solution (using Dp tabulation)

class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize the dp array with -1 for all positions
        dp = [-1] * (n + 1)
        
        # Base cases: There is 1 way to climb 0 or 1 stairs
        dp[0] = dp[1] = 1
        
        # Fill the dp array for each number of stairs from 2 to n
        for i in range(2, n + 1):
            # The number of ways to reach the ith step is the sum of the ways to reach (i-1)th and (i-2)th steps
            dp[i] = dp[i-1] + dp[i-2]
        
        # The result is the number of ways to reach the nth step
        return dp[n]


# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimal Solution (using Space optimization)

class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize the first two steps with 1 way to reach each
        first, second = 1, 1
        
        # Iterate from the 2nd step to the nth step
        for i in range(2, n + 1):
            # Calculate the current step as the sum of the ways to reach the previous two steps
            curr = first + second
            # Update the second step to the previous first step
            second = first
            # Update the first step to the current step
            first = curr
        
        # Return the number of ways to reach the nth step
        return first


# Time Complexity: O(n)
# Space Complexity: O(1)