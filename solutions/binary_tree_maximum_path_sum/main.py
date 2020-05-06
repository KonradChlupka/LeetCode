class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.best = root.val
        return max(self.cost_to_root(root), self.best)

    def cost_to_root(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = max(self.cost_to_root(root.left), 0)
        right = max(self.cost_to_root(root.right), 0)

        cost_through_root = left + right + root.val
        if cost_through_root > self.best:
            self.best = cost_through_root

        return root.val + max(left, right)
