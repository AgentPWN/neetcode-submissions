class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()

                rightSide = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(rightSide.val)

        return result