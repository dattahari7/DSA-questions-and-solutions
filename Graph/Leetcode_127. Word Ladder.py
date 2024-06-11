# 127. Word Ladder

# Optimal Solution

from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert wordList to a set for O(1) lookups
        vis = set(wordList)
        # If endWord is not in the wordList, return 0
        if endWord not in vis:
            return 0
        
        # Initialize the queue with the beginWord and starting step count
        que = deque([(beginWord, 1)])
        # Remove the beginWord from the visited set if it exists
        if beginWord in vis:
            vis.remove(beginWord)
        
        # Perform BFS
        while que:
            word, steps = que.popleft()
            
            # Check if we have reached the endWord
            if word == endWord:
                return steps
            
            # Try changing each character of the word to every letter from 'a' to 'z'
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # Form a new word by changing one character at position i
                    newWord = word[:i] + c + word[i + 1:]
                    
                    # If the new word is in the visited set
                    if newWord in vis:
                        # Add the new word to the queue with incremented step count
                        que.append((newWord, steps + 1))
                        # Mark the new word as visited by removing it from the set
                        vis.remove(newWord)
                        
        # If no transformation sequence exists, return 0
        return 0


# Time Complexity: O(N * M * 26)
# Space Complexity: O(N)