# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        left = max(left , 0)
        right = max(right , 0)
        self.ans = max(self.ans , left + right + root.val)
        maxVal = max(left + root.val , right + root.val)
        
        return maxVal
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        self.dfs(root)
        return self.ans