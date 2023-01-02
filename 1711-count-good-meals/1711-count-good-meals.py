class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        deliciousness.sort()
        pair=0
        count = defaultdict(int)
        squares=[]
        
            
        for i in range(22):
            squares.append(2**i)
        
        for num in deliciousness:
            for square in squares:
                if square - num in count:
                    pair += count[square-num] 
            
            count[num] += 1
        
        return pair % (10**9 + 7)