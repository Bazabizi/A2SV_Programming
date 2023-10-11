class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        arr = [1]
        for i in range(1,k):
            
            val = arr[-1]*power
            arr.append(val)
        
        total = 0
        for idx in range(k):
            total += arr[idx]*(ord(s[idx]) - ord('a') + 1)
        
        if (total)%modulo == hashValue:
            return s[:k]
        left = 0
        for right in range(k , n):
            if hashValue == (total)%modulo:
                return s[left:left + k]
            total -= (arr[0])*(ord(s[left]) - ord('a') + 1)
            total //= (power)
            total += arr[k-1]*(ord(s[right]) - ord('a') + 1)
           
            left += 1
            # print(total)

        if hashValue == (total)%modulo:
                return s[left:left + k]