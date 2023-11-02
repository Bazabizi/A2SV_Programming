# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,root):
        if not root:
            return [0 , 0]
        left = self.traversal(root.left)      
        right = self.traversal(root.right)

        sumup = right[1] + left[1] + root.val
        size = left[0] + right[0] + 1
        average = sumup // size
        if average == root.val:
            self.count += 1
        return [ size, sumup]
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        ans = self.traversal(root)
        return self.count