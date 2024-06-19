#  Count Distinct Substrings

# BruteForce Solution

def countDistinctSubstrings(s):
    # Initialize a set to store unique substrings
    unique = set()
    n = len(s)  # Length of the input string
    
    # Iterate through each character in the string
    for i in range(n):
        substr = ""  # Initialize an empty substring
        unique.add(substr)  # Add the empty substring to the set (optional)
        
        # Build substrings starting from index i
        for j in range(i, n):
            substr += s[j]  # Append the current character to the substring
            unique.add(substr)  # Add the current substring to the set
    
    # Return the number of unique substrings
    return len(unique)


# Time Complexity: O(N * N)
# Space Complexity: O(N * N)


# Optimal Solution (using Trie)

class TrieNode:
    def __init__(self):
        # Initialize an array for children with 26 None values (one for each letter)
        self.children = [None] * 26
        # Boolean to check if a node represents the end of a substring
        self.isEnd = False

def countDistinctSubstrings(s):
    root = TrieNode()  # Create the root node of the Trie
    n = len(s)  # Length of the input string
    count = 0  # Initialize count of distinct substrings

    # Iterate through each character in the string
    for i in range(n):
        node = root  # Start from the root node for each new starting character

        # Build substrings starting from index i
        for j in range(i, n):
            index = ord(s[j]) - ord('a')  # Calculate the index for the character
            if node.children[index] is None:
                # If the child node does not exist, create a new TrieNode
                node.children[index] = TrieNode()
                count += 1  # Increment count as a new substring is found
            node = node.children[index]  # Move to the next node

    return count + 1  # Add 1 to count the empty substring


# Time Complexity: O(N * N) where N is the length of the word.
# Space Complexity: O(N * N) Where N is the length of the word.
