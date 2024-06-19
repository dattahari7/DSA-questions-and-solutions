# 1858. Longest Word With All Prefixes

# Optimal Solution (using Trie)

class TrieNode:
    def __init__(self):
        # Initialize a node with an array of children (size 26 for each letter in the alphabet)
        # and a flag to mark the end of a word
        self.children = [None] * 26
        self.isEnd = False

class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def insert(self, word):
        # Insert a word into the Trie
        node = self.root
        for ch in word:
            # Calculate the index of the character
            index = ord(ch) - ord('a')
            # If the character is not present, create a new node
            if node.children[index] is None:
                node.children[index] = TrieNode()
            # Move to the child node
            node = node.children[index]
        # Mark the end of the word
        node.isEnd = True

    def has_all_prefixes(self, word):
        # Check if all prefixes of the word are present in the Trie
        node = self.root
        for ch in word:
            # Calculate the index of the character
            index = ord(ch) - ord('a')
            # If the character is not present, return False
            if node.children[index] is None:
                return False
            # Move to the child node
            node = node.children[index]
            # If the current node is not the end of a word, return False
            if not node.isEnd:
                return False
        # All prefixes are present
        return True

def completeString(n: int, a: List[str]) -> str:
    # Function to find the longest word with all prefixes present in the Trie
    trie = Trie()
    # Insert all words into the Trie
    for word in a:
        trie.insert(word)
    
    longest = ""
    # Check each word to see if all its prefixes are present in the Trie
    for word in a:
        if trie.has_all_prefixes(word):
            # Update the longest word if the current word is longer or lexicographically smaller
            if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                longest = word

    # Return the longest word or None if no such word exists
    return longest if longest else None


# Time Complexity: O(L) where L is the length of the word
# Space Complexity: O(L * N) Where L is the length of the longest word, and N is the number of words. 
