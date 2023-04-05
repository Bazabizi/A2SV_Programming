class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) <= 1:
            return False
        count = defaultdict(int)
        for num in deck:
            count[num] += 1
            
        minVal = min(count.values())
        for val in count.values():
            minVal = math.gcd(minVal,val)
        if minVal == 1:
            return False
        return True