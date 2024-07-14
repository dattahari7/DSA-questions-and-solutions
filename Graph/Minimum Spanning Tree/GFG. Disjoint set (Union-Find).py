# Disjoint set (Union-Find)

# Optimal Solution

# function should return parent of x
def find(A, X):
    # Code here
    X1=X
    while(A[X-1]!=X):
        X=A[X-1]
    A[X1-1]=X
    return X

# function shouldn't return or print anything
def unionSet(A, X, Z):
    # Code here
    rank=[0]*len(A)
    px=find(A,X)
    pz=find(A,Z)
    if px!=pz:
        if rank[px-1]>rank[pz-1]:
            A[pz-1]=px
        elif rank[px-1]<rank[pz-1]:
            A[px-1]=pz
        else:
            A[px-1]=pz
            rank[px-1]+=1
            
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)