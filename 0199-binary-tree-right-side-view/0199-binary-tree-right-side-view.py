# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root , level):
        if not root :
            return
        if level == len(self.ans):
            self.ans.append(root.val)
        self.inorder(root.right , level + 1)
        self.inorder(root.left, level + 1)

    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.inorder(root,0)
        return self.ans