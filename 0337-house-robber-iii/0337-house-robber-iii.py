# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = defaultdict(int)
        def dp(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            val = 0
            if root.left:
                val += dp(root.left.right) + dp(root.left.left)
            if root.right:
                val += dp(root.right.left) + dp(root.right.right)
            
            memo[root] = max(val + root.val  , dp(root.left) + dp(root.right))
            
            return memo[root]
        return dp(root)