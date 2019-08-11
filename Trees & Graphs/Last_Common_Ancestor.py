import Tree

def findLCA(root, n1, n2): 
      
    # Base Case 
    if root is None: 
        return None
  
    # If node matches either of our targets, return root
    if root.data == n1 or root.data == n2: 
        return root  
  
    # Look for keys in left and right subtrees 
    left_lca = findLCA(root.left, n1, n2)  
    right_lca = findLCA(root.right, n1, n2) 
  
    # If both the left and right children return not null values
    # then we know this node is the LCA
    if left_lca and right_lca: 
        return root  
  
    # Otherwise check if left subtree or right subtree is LCA 
    return left_lca if left_lca is not None else right_lca 