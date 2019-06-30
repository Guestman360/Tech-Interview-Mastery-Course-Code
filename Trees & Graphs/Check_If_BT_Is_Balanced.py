def isBalanced(root, height): 
      
    # lh and rh to store height of  
    # left and right subtree 
    lh = Height() 
    rh = Height() 
  
    # Base condition when tree is  
    # empty return true 
    if root is None: 
        return True
  
    # l and r are used to check if left 
    # and right subtree are balanced 
    l = isBalanced(root.left, lh) 
    r = isBalanced(root.right, rh) 
  
    # height of tree is maximum of  
    # left subtree height and 
    # right subtree height plus 1 
    height.height = max(lh.height, rh.height) + 1
  
    if abs(lh.height - rh.height) <= 1: 
        return l and r 
  
    # if we reach here then the tree  
    # is not balanced 
    return False