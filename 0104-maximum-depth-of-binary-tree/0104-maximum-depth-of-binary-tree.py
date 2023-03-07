# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self,root , n):
        if not root:
            return n
        left = self.depth(root.left , n + 1)
        right = self.depth(root.right , n + 1)
        return max(left , right)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root , 0)