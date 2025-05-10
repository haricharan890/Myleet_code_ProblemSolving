class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True  # Both are None
        if not p or not q:
            return False  # One is None and the other is not
        if p.val != q.val:
            return False  # Values are different
        
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)