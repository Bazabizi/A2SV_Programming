# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum = 0
        def sumup(root ):
            nonlocal sum
            if not root:
                return
            sumup(root.right)
            root.val += sum
            sum = root.val
            sumup(root.left)
        
        sumup(root )
        return root
