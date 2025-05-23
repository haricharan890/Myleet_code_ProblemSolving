# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if root !=None:
            if root.left!= None:
                result+=self.postorderTraversal(root.left)
            if root.right!=None:
                result+=self.postorderTraversal(root.right)
            result.append(root.val)
        return result
        