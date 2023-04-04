class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime = set()
        for val in nums:
            num = 2
            while num*num <= val:

                while val % num==0:
                    prime.add(num)
                    val//= num
                num += 1

            if val > 1:
                prime.add(val)
 
        return len(prime)