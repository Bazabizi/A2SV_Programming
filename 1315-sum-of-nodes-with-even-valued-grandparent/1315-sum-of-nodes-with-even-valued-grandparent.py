# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        def sumOfGrandParent(grandParent, parent):
            nonlocal ans
            if grandParent.val % 2 == 0:
                if parent and parent.left :
                    ans += parent.left.val
                if parent and parent.right :
                    ans += parent.right.val
            if parent:
                sumOfGrandParent(parent,parent.right)
                sumOfGrandParent(parent,parent.left)
            
        sumOfGrandParent(root, root.left)
        sumOfGrandParent(root, root.right)
        return ans