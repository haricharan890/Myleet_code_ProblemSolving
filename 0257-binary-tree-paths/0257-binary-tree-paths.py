# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr = []
        self.dfs(root, "", arr)
        return arr
    
    def dfs(self, root, string, res): 
        if not root: 
            return 
        string += str(root.val) + "->"
        if not root.left and not root.right: 
            res.append(string[ : - 2])
        self.dfs(root.left, string, res)
        self.dfs(root.right, string, res)

    



        