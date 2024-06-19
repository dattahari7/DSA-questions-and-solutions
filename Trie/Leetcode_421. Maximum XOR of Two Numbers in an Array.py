# 421. Maximum XOR of Two Numbers in an Array

# Optimal Solution (using Trie)

class TrieNode:
    def __init__(self):
        # Initialize an array for binary digits (0 and 1)
        self.links = [None, None]

    # Check if the node has a child for the given bit
    def contains_key(self, bit):
        return self.links[bit] is not None
    
    # Get the child node for the given bit
    def get(self, bit):
        return self.links[bit]
    
    # Set the child node for the given bit
    def put(self, bit, node):
        self.links[bit] = node

class Trie:
    def __init__(self):
        # Initialize the root of the Trie
        self.root = TrieNode()
    
    # Insert a number into the Trie
    def insert(self, num):
        node = self.root
        # Iterate through the bits of the number from the most significant bit to the least significant bit
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # If there is no child for the current bit, create a new TrieNode
            if not node.contains_key(bit):
                node.put(bit, TrieNode())
            node = node.get(bit)
    
    # Find the maximum XOR for a given number with the numbers already inserted in the Trie
    def get_max(self, num):
        node = self.root
        maxi = 0
        # Iterate through the bits of the number from the most significant bit to the least significant bit
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Try to find the opposite bit to maximize the XOR
            if node.contains_key(1 - bit):
                maxi |= (1 << i)
                node = node.get(1 - bit)
            else:
                node = node.get(bit)
        return maxi

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()  # Initialize the Trie
        maxi = 0  # Initialize the maximum XOR value
        # Insert all numbers into the Trie
        for num in nums:
            trie.insert(num)
        # Find the maximum XOR for each number with the numbers in the Trie
        for num in nums:
            maxi = max(maxi, trie.get_max(num))
        return maxi  # Return the maximum XOR value


# Time Complexity: O(N + M)
# Space Complexity: O(N)