# 721. Accounts Merge

# Optimal Solution (using union find(DisjointSet))

class DisjointSetUnion:
    def __init__(self, n):
        # Initialize parent array where each node is its own parent initially
        self.parent = list(range(n))
        # Initialize sizes of each set to 1
        self.size = [1] * n
    
    def find(self, u):
        # Path compression: makes the tree flat
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Union by size: attach smaller tree under root of larger tree
        root_u = self.find(u)  # Find root of u
        root_v = self.find(v)  # Find root of v
        if root_u != root_v:  # Only union if they are in different sets
            if self.size[root_u] < self.size[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DisjointSetUnion(n)

        # Map each email to its corresponding account index
        map_mail_node = {}
        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail not in map_mail_node:
                    # If email is not seen before, map it to current account index
                    map_mail_node[mail] = i
                else:
                    # If email is already seen, union the two accounts
                    dsu.union(i, map_mail_node[mail])
                
        # Group emails by their root parent index
        merged_mail = [[] for _ in range(n)]
        for mail, node in map_mail_node.items():
            parent_node = dsu.find(node)  # Find the root parent index
            merged_mail[parent_node].append(mail)

        res = []

        # Build the result list
        for i in range(n):
            if len(merged_mail[i]) == 0:
                continue  # Skip empty lists
            merged_mail[i].sort()  # Sort emails lexicographically
            temp = [accounts[i][0]]  # Start with the account name
            temp.extend(merged_mail[i])  # Add sorted emails
            res.append(temp)  # Add to the result list

        return res


# Time Complexity: O(N+E) + O(E*4ɑ) + O(N*(ElogE + E)) where N = no. of indices or nodes and E = no. of emails. The first term is for visiting all the emails. The second term is for merging the accounts. And the third term is for sorting the emails and storing them in the answer array.

# Space Complexity: O(N)+ O(N) +O(2N) ~ O(N) where N = no. of nodes/indices. The first and second space is for the ‘mergedMail’ and the ‘ans’ array. The last term is for the parent and size array used inside the Disjoint set data structure.
