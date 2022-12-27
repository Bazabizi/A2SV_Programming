class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        lcm=n
        while lcm%2==1:
            lcm*=2
            
        return lcm
        