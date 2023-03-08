# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanced(self, root):
        if not root:
            return 0 , True
        check = True
        left , isleftBalanced = self.balanced(root.left)
        right , isrightBalanced = self.balanced(root.right)
        
        if max(right , left)- 1 > min(right ,left ):
            check = False
        return max(left , right) + 1 , check and isleftBalanced and isrightBalanced
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = self.balanced(root)
        return ans[1]