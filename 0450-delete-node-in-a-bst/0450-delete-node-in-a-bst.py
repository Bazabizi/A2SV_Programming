# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left , key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left:
                temp = self.maxVal(root.left)
                root.val = temp.val
                root.left = self.deleteNode(root.left , temp.val)
            else:
                temp = self.minVal(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right , temp.val)
        
        return root
    def minVal(self,root):
        while root.left:
            root = root.left
        return root
    
    
    def maxVal(self, root):
        while root.right:
            root = root.right
        
        return root