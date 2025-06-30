class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # handle empty tree
        if not root:
            return []

        # start with adding the first node to the queue
        q = deque([root])
        res = []

        # reverse flag to be reverted per level
        reverse = False
        
        # BFS...
        while q:
            # determine the current size of the queue
            #   to register nodes at the currrent level
            size = len(q)
            curr_res = deque([])

            # pop all nodes at the current level one by one
            #   and add their children to the queue
            for _ in range(size):
                node = q.popleft()
                for c in [node.left, node.right]:
                    if c:
                        q.append(c)

                # append at the start if reverse, else append at the end
                if reverse:
                    curr_res.appendleft(node.val)
                else:
                    curr_res.append(node.val)

            # append the current level array to result list
            #   after processing all nodes at the current level
            # also, convert deque to list
            res.append(list(curr_res))

            # flag flip
            reverse = not reverse
        return res