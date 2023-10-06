# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int ) -> List[List[int]]:
        ans = []
        def dfs( root , temp , targetsum , total):
            if not root:
                return 
            if total + root.val == targetSum:
                if not root.right and not root.left:
                    ans.append(temp + [root.val])
                    return
            dfs(root.left , temp + [root.val] , targetSum , total + root.val)
            dfs(root.right , temp + [root.val] , targetSum , total + root.val)
            
        dfs(root ,[], targetSum , 0)
        return ans