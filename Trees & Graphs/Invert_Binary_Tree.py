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