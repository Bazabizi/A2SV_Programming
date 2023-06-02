class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = len(ratings)
        size = candies
        idx = 0
        while idx < size -1:
            if ratings[idx] == ratings[idx + 1]:
                idx += 1
                continue
            up = 0
            while idx < size - 1 and ratings[idx] < ratings[idx + 1]:
                up += 1
                candies += up
                idx += 1
            
            down = 0
            while idx < size - 1 and ratings[idx] > ratings[idx + 1]:
                down += 1
                candies += down
                idx += 1
            
            candies -= min(up , down)
            
        return candies