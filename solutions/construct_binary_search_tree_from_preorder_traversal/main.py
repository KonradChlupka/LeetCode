class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            parent = stack[-1]
            child = TreeNode(preorder[i])
            while stack and stack[-1].val < child.val:
                parent = stack.pop()
            if parent.val < child.val:
                parent.right = child
            else:
                parent.left = child
            stack.append(child)
        return root
