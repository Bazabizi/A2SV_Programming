# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameValue(self,root , parent_val):
        if not root:
            return [0 , 0]
        left = self.sameValue(root.left,root.val)
        right = self.sameValue(root.right, root.val)
        
        ans = left[0] + right[0]
        ans = max(left[1] ,right[1],ans)
        if root.val == parent_val:
            return max(left[0],right[0]) + 1 ,  ans
        
        return 0 , ans
        
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = self.sameValue(root , 0)
        return ans[1]
        
            
                