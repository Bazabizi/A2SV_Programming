class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        outdegree = defaultdict(list)
        indegree = defaultdict(int)
        
        for idx , ingredient in enumerate(ingredients):
            food = recipes[idx]
            for val in ingredient:
                outdegree[val].append(food)
                indegree[food] += 1
        
        recipes = set(recipes)
        queue = deque()
        for ingredient in supplies:
            queue.append(ingredient)
        
        ans = []
        while queue:
            food = queue.popleft()
            if food in recipes:
                ans.append(food)
            
            for val in outdegree[food]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    queue.append(val)
        
        return ans