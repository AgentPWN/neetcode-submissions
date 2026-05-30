# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def subtree(cur, n):
            if not cur:
                return None, n
            value, n = subtree(cur.left, n)
            if value is not None:
                return value, n
            n += 1
            if n==k:
                return cur.val, n
            return subtree(cur.right, n)

        return subtree(root, 0)[0]