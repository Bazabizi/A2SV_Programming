# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if not root:
            return []
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        ans = []
        ans.extend(left)
        ans.append(root.val)
        ans.extend(right)
        return ans
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans  = self.inorder(root)
        length = len(ans)
        for idx in range(length-1):
            if ans[idx] >= ans[idx + 1]:
                return False
        return True