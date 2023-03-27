# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findGreaterNumber(self, left, right, preorder,val):
        for idx in range(left,right):
            if preorder[idx] > val:
                return idx
        return -1
    
    
    def preorder(self, left , right , preorder):
        if left > right:
            return None
        root = TreeNode(preorder[left])
        index = self.findGreaterNumber(left + 1, right + 1, preorder , root.val)
        
        if index == -1:
            root.right = None
            index  = right + 1
        else:
            root.right = self.preorder(index, right , preorder)
        root.left = self.preorder(left + 1, index - 1 , preorder)
            
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.preorder( 0 , len(preorder) - 1 , preorder)
    