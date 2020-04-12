class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.answer = 0

        def height(node):
            if not node:
                return 0
            left, right = height(node.left), height(node.right)
            self.answer = max(self.answer, left + right)
            return max(left, right) + 1

        height(root)
        return self.answer
