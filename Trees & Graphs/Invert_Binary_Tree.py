import collections

# Recursive Solution
def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None
    
    res = TreeNode(root.val)
    if root.right:
        res.left = invertTree(root.right)
    else:
        res.left = None
    
    if root.left:
        res.right = invertTree(root.left)
    else:
        res.right = None
        
    return res

#Iterative Solution (w/ queue)
def invertTree(self, root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        if node:
            node.left, node.right = node.right, node.left
            q.append(node.left)
            q.append(node.right)
    return root