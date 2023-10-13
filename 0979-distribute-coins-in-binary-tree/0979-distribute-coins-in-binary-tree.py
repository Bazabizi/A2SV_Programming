# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def traverse(root , parent):
            nonlocal ans
            if not root:
                return 0
            left = traverse(root.left , parent)
            right = traverse(root.right , parent)
            have = left + right
            have  += root.val - 1
            
            ans += abs(have) 
            
            return have
        
        traverse(root , root)
        return ans