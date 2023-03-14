# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root , num):
        if not root:
            return
        num += str(root.val)
        if not root.left and not root.right:
            self.store.append(num)
            return
        self.traverse(root.left , num)
        self.traverse(root.right , num)
        return
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.store = []
        ans = 0
        self.traverse(root , "")
        for num in self.store:
            ans += int(num)
        
        return ans