# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self,root):
        if not root.left and not root.right:
            return [str(root.val)]
        ans = []
        if root.left:
            left = self.path(root.left)
            for path in left:
                newPath = str(root.val) + "->" + path
                ans.append(newPath)
        
        if root.right:
            right = self.path(root.right)
            for path in right:
                newPath = str(root.val) + "->" + path
                ans.append(newPath)
        
        return ans
        
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.path(root)