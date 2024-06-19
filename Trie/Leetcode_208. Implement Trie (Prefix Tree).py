# 208. Implement Trie (Prefix Tree)

# Optimal Solution

class TrieNode:
    def __init__(self) -> None:
        # Initialize the node with an empty dictionary for children
        # and a boolean flag to mark the end of a word
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        # Initialize the Trie with a root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Insert a word into the Trie
        node = self.root
        for ch in word:
            # Traverse the Trie, creating new nodes as needed
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        # Mark the end of the word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Search for a word in the Trie
        node = self.root
        for ch in word:
            # Traverse the Trie and check if the word exists
            if ch not in node.children:
                return False
            node = node.children[ch]
        # Return true if the word is found and is marked as end of a word
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Check if there is any word in the Trie that starts with the given prefix
        node = self.root
        for ch in prefix:
            # Traverse the Trie and check if the prefix exists
            if ch not in node.children:
                return False
            node = node.children[ch]
        # If traversal is successful, return true
        return True


# Time Complexity: O(L) where L is the length of the word
# Space Complexity: O(L * N) Where L is the length of the longest word, and N is the number of words. 
