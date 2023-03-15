# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def numberOfNodes(self,root):
        if not root:
            return 0
        
        return 1 + self.numberOfNodes(root.left) + self.numberOfNodes(root.right)
        
    def traverse(self,root, idx , n):
        if not root:
            return True
        if idx >= n:
            return False
        left = self.traverse(root.left , idx*2 + 1 , n)
        right = self.traverse(root.right ,idx*2 +2 , n)
        return left and right
    
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        nodes = self.numberOfNodes(root)
        return self.traverse(root , 0 , nodes)