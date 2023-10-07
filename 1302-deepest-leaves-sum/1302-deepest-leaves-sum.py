# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int)
        def dfs(idx,root):
            if not root:
                return 0
            count[idx] += root.val
            dfs(idx + 1 , root.left)
            dfs(idx + 1 , root.right)
        dfs(0 , root)
        return count[max(count.keys())]