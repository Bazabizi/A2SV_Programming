# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(root , left):
            if not root:
                return 0

            if not root.left and not root.right:
                if left:
                    return root.val
                return 0
            left = traverse(root.left , 1)
            right = traverse(root.right , 0)
            return right + left
        return traverse(root, 0) 
