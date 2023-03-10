# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root,column , row):
        if not root:
            return 
        self.columnOrder[column].append([row ,root.val])
        self.traverse(root.left, column - 1 , row + 1)
        self.traverse(root.right, column + 1 , row + 1)
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.columnOrder = defaultdict(list)
        self.traverse(root,0, 0)
        temp =[]
        
        for key , arr in self.columnOrder.items():
            temp.append((key,sorted(arr)))
        temp.sort()
        ans = []
        for col , arr in temp:
            x = []
            for row, value in arr:
                x.append(value)
            ans.append(x)
        return ans
        