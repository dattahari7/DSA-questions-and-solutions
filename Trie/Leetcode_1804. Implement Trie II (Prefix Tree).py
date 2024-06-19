# 1804. Implement Trie II (Prefix Tree)

# Optimal Solution

class Node:
    def __init__(self):
        # Initialize a node with an array of children (size 26 for each letter in the alphabet),
        # end_with_count to count occurrences of words ending at this node,
        # and prefix_count to count occurrences of words passing through this node
        self.children = [None] * 26
        self.end_with_count = 0
        self.prefix_count = 0

class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = Node()

    def insert(self, word):
        # Insert a word into the Trie
        node = self.root
        for ch in word:
            # Calculate the index of the character
            index = ord(ch) - ord('a')
            # If the character is not present, create a new node
            if node.children[index] is None:
                node.children[index] = Node()
            # Move to the child node and increment the prefix count
            node = node.children[index]
            node.prefix_count += 1
        # After inserting all characters, increment the end_with_count at the last node
        node.end_with_count += 1

    def countWordsEqualTo(self, word):
        # Count words in the Trie that are exactly equal to the given word
        node = self.root
        for ch in word:
            # Calculate the index of the character
            index = ord(ch) - ord('a')
            # If the character is not present, return 0
            if node.children[index] is None:
                return 0
            else:
                # Move to the child node
                node = node.children[index]
        # Return the count of words ending at this node
        return node.end_with_count

    def countWordsStartingWith(self, word):
        # Count words in the Trie that start with the given prefix
        node = self.root
        for ch in word:
            # Calculate the index of the character
            index = ord(ch) - ord('a')
            # If the character is not present, return 0
            if node.children[index] is None:
                return 0
            else:
                # Move to the child node
                node = node.children[index]
        # Return the count of words passing through this node
        return node.prefix_count

    def erase(self, word):
        # Erase a word from the Trie
        node = self.root
        for ch in word:
            # Calculate the index of the character
            index = ord(ch) - ord('a')
            # If the character is not present, return as the word does not exist
            if node.children[index] is None:
                return
            else:
                # Move to the child node and decrement the prefix count
                node = node.children[index]
                node.prefix_count -= 1
        # Decrement the end_with_count at the last node
        node.end_with_count -= 1



# Time Complexity: O(L) where L is the length of the word
# Space Complexity: O(L * N) Where L is the length of the longest word, and N is the number of words. 
