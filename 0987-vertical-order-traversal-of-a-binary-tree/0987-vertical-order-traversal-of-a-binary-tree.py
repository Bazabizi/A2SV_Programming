# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        position = defaultdict(list)
        
        def dfs(root , row , col):
            if not root:
                return
            
            position[col].append([row , root.val])
            dfs(root.left , row + 1 , col - 1)
            dfs(root.right , row + 1 , col + 1)
            
        {
            1: [[1,2] , [1 , 3]]
        }
        dfs(root , 0 , 0)
        array_to_be_sorted = []
        for key , value in position.items():
            
            value.sort()
            temp = []
            for row , val in value:
                temp.append(val)
            
            array_to_be_sorted.append([key , temp])
        
        
        array_to_be_sorted.sort()
        
        ans = []
        for col , values in array_to_be_sorted:
            ans.append(values)
        
        return ans


