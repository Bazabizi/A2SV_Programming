# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        def preorder(root):
            if not root:
                return 
            count[root.val] += 1
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        maxVal = max(count.values())
        ans = []
        for key , val in count.items():
            if val == maxVal:
                ans.append(key)
        return ans