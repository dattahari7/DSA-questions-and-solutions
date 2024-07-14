# Frog Jump (Geek Jump)

# Brute Force Solution

class Solution:
    def minimumEnergy(self, height, n):
        # Recursive function to find the minimum energy required to reach the nth step
        def minEng(height, n):
            # Base case: no energy needed to stay at the first step
            if n == 0:
                return 0
            # Base case: energy needed to jump from the first to the second step
            if n == 1:
                return abs(height[1] - height[0])
            
            # Energy needed to jump from (n-1)th step to the nth step
            jumpOne = minEng(height, n-1) + abs(height[n] - height[n-1])
            
            # Initialize jumpTwo with a large value
            jumpTwo = float('inf')
            
            # If n is greater than 1, calculate the energy needed to jump from (n-2)th step to the nth step
            if n > 1:
                jumpTwo = minEng(height, n-2) + abs(height[n] - height[n-2])
                
            # Return the minimum energy needed to reach the nth step
            return min(jumpOne, jumpTwo)
        
        # Call the recursive function starting from the last step (n-1)
        return minEng(height, n-1)

# Time Complexity: O(n!)
# Space Complexity: O(n)

# Optimal Solution (using Dp memoization)

class Solution:
    def minimumEnergy(self, height, n):
        # Recursive function to find the minimum energy required to reach the nth step
        def minEng(height, n, dp):
            # Base case: no energy needed to stay at the first step
            if n == 0:
                return 0
            # Base case: energy needed to jump from the first to the second step
            if n == 1:
                return abs(height[1] - height[0])
            
            # Return the already computed value if available
            if dp[n] != -1:
                return dp[n]
            
            # Energy needed to jump from (n-1)th step to the nth step
            jumpOne = minEng(height, n-1, dp) + abs(height[n] - height[n-1])
            
            # Initialize jumpTwo with a large value
            jumpTwo = float('inf')
            
            # If n is greater than 1, calculate the energy needed to jump from (n-2)th step to the nth step
            if n > 1:
                jumpTwo = minEng(height, n-2, dp) + abs(height[n] - height[n-2])
                
            # Store the result in dp array and return the minimum energy needed to reach the nth step
            dp[n] = min(jumpOne, jumpTwo)
            return dp[n]
        
        # Initialize the dp array with -1 to indicate that those values are not computed yet
        dp = [-1] * n
        
        # Call the recursive function starting from the last step (n-1)
        return minEng(height, n-1, dp)


# Time Complexity: O(n)
# Space Complexity: O(n) + O(n) stack space ~= O(n)

# Optimal Solution (using Dp tabulation)

class Solution:
    def minimumEnergy(self, height, n):
        # Initialize the dp array to store the minimum energy required to reach each step
        dp = [-1] * n
        # Base case: no energy needed to stay at the first step
        dp[0] = 0
        
        # Iterate through each step from the second step to the nth step
        for idx in range(1, n):
            # Initialize the energy needed for a two-step jump with a large value
            jumpTwo = float('inf')
            # Calculate the energy needed for a one-step jump from the previous step
            jumpOne = dp[idx - 1] + abs(height[idx] - height[idx - 1])
            
            # If the current step is beyond the second step, calculate the energy for a two-step jump
            if idx > 1:
                jumpTwo = dp[idx - 2] + abs(height[idx] - height[idx - 2])
                
            # Store the minimum energy needed to reach the current step
            dp[idx] = min(jumpOne, jumpTwo)
        
        # Return the minimum energy required to reach the last step
        return dp[n - 1]


# Time Complexity: O(n)
# Space Complexity: O(n)


# Optimal Solution (using space optimization)

class Solution:
    def minimumEnergy(self, height, n):
        # Initialize previous two steps energy values
        prev1, prev2 = 0, 0
        
        # Iterate through each step from the second step to the nth step
        for idx in range(1, n):
            # Initialize the energy needed for a two-step jump with a large value
            jumpTwo = float('inf')
            # Calculate the energy needed for a one-step jump from the previous step
            jumpOne = prev1 + abs(height[idx] - height[idx - 1])
            
            # If the current step is beyond the second step, calculate the energy for a two-step jump
            if idx > 1:
                jumpTwo = prev2 + abs(height[idx] - height[idx - 2])
                
            # Store the minimum energy needed to reach the current step
            curr = min(jumpOne, jumpTwo)
            # Update the energy values for the next iteration
            prev2 = prev1
            prev1 = curr
 
        # Return the minimum energy required to reach the last step
        return prev1


# Time Complexity: O(n)
# Space Complexity: O(1)