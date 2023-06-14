# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minval = float('inf')
        self.parent = None
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            
            if self.parent is not None:
                self.minval = min(self.minval , root.val - self.parent)
            
            self.parent = root.val
            inorder(root.right)
        
        inorder(root)
        return self.minval