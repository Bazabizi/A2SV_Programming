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
        left[0] += 1
        left[1] += root.val
        right = self.traversal(root.right)
        right[0] += 1
        right[1] += root.val
        sumup = right[1] + left[1] + root.val
        average = sumup // (left[0] + right[0] + 1)
        if average == root.val:
            self.count += 1
        return [ left[0] + right[0] + 1, sumup]
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        ans = self.traversal(root)
        return self.count