# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanced(self, root):
        if not root:
            return [0 , True]
        check = True
        left = self.balanced(root.left)
        right = self.balanced(root.right)
        left[0] += 1
        right[0] += 1
        if max(right[0] , left[0])- 1 > min(right[0],left[0]):
            check = False
        return [max(left[0] , right[0]) , check and left[1] and right[1]]
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = self.balanced(root)
        return ans[1]