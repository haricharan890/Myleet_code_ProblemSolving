class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(start, end):
            if start == end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = build(start, mid)
            root.right = build(mid + 1, end)
            return root
        return build(0, len(nums))