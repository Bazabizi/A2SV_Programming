# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def symmetricTree(self,leftroot , rightroot):
        if not leftroot and not rightroot:
            return True
        if not leftroot or not rightroot:
            return False
        if leftroot.val != rightroot.val:
            return False
        
        left = self.symmetricTree(leftroot.left , rightroot.right)
        right = self.symmetricTree(leftroot.right , rightroot.left)
        
        return left and right
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetricTree(root.left , root.right)