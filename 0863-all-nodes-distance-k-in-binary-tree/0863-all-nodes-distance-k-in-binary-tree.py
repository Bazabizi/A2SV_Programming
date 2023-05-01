# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        graph = defaultdict(list)
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                
            if node.right:
                queue.append(node.right)
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
        
        ans = []
        count = 0
        visited = set([target.val])
        queue.append(target.val)
        while queue and count <= k:
            size = len(queue)
            count += 1
            for _ in range(size):
                vertix = queue.popleft()
                for val in graph[vertix]:
                    if val not in visited:
                        queue.append(val)
                        visited.add(val)
                        if k == count :
                            ans.append(val)
            
        return ans
            