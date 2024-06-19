# 1707. Maximum XOR With an Element From Array

# BruteForce Solution

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Initialize the result list
        res = []
        
        # Process each query
        for xi, ai in queries:
            max_Xor = -1  # Initialize max_Xor for the current query
            
            # Iterate over all numbers in nums
            for num in nums:
                # Check if the number is less than or equal to ai
                if num <= ai:
                    # Calculate XOR and update max_Xor if it's greater
                    max_Xor = max(max_Xor, num ^ xi)
            
            # Append the result of the current query to the result list
            res.append(max_Xor)
        
        # Return the result list
        return res


# Time Complexity: O(N * Q)
# Space Complexity: O(N)
    

# Optimal Solution (using Trie)
    
class TrieNode:
    def __init__(self):
        self.links = [None, None]

    def contains_key(self, bit):
        return self.links[bit] is not None
    
    def get(self, bit):
        return self.links[bit]
    
    def put(self, bit, node):
        self.links[bit] = node

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.contains_key(bit):
                node.put(bit, TrieNode())
            node = node.get(bit)
    
    def get_max_xor(self, num):
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.contains_key(1 - bit):
                max_xor |= (1 << i)
                node = node.get(1 - bit)
            else:
                node = node.get(bit)
        return max_xor

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Sort the numbers for efficient processing
        nums.sort()
        
        # Pair each query with its index and sort by ai
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        
        # Initialize the result list
        res = [-1] * len(queries)
        
        # Initialize the Trie
        trie = Trie()
        
        # Process each query
        j = 0
        for idx, (xi, ai) in queries:
            # Insert nums into the Trie up to ai
            while j < len(nums) and nums[j] <= ai:
                trie.insert(nums[j])
                j += 1
            # If the Trie has any elements, calculate the max XOR
            if j > 0:
                res[idx] = trie.get_max_xor(xi)
        
        return res



# Time Complexity: O(N + Q + Qlog(Q))
# Space Complexity: O(N + Q)