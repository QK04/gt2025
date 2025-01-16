def construct_adjacency_matrix(edges, n):
    adj_matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        adj_matrix[u-1][v-1] = 1
    return adj_matrix


def inorder_traversal(tree, node):
    if node not in tree:
        return []
    
    left = inorder_traversal(tree, tree[node][0]) if len(tree[node]) > 0 else []
    right = inorder_traversal(tree, tree[node][1]) if len(tree[node]) > 1 else []
    
    return left + [node] + right

edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
n = 8 

# Step 1: Construct adjacency matrix for graph G
adj_matrix = construct_adjacency_matrix(edges, n)
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

# Step 2: Convert Graph to Adjacency List for Tree
tree = {
    1: [3, 2], 
    2: [6, 5], 
    3: [4], 
    4: [8], 
    5: [7],          
    6: [],       
    7: [],           
    8: []    
}

# Input node label (x)
x = int(input("\nEnter the node label (x) in Inorder: "))

# Step 3: Perform Inorder Traversal
inorder_result = inorder_traversal(tree, x)
print(f"Inorder traversal of subtree rooted at node {x}: {inorder_result}")