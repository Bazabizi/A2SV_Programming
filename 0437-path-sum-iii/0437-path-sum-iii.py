# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root , total , targetSum):
           
            if not root:
                return
            
            total = total + root.val
            if total == targetSum:
                self.ans += 1
            
            dfs(root.left , total  , targetSum)
            dfs(root.right , total  , targetSum)
        
        if not root:
            return 0
        dfs(root , 0 , targetSum)
        self.pathSum(root.left , targetSum)
        self.pathSum(root.right , targetSum)
        
        
        return self.ans
            