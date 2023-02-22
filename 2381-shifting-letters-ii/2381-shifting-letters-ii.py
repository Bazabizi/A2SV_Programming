class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        size = len(s)
        prefixSum = [0]*(len(s)+1)
        
        for left , right, direction in shifts:
            if direction == 1:
                prefixSum[left] += 1
                prefixSum[right+1] += -1
            else:
                prefixSum[left] += -1
                prefixSum[right+1] += 1
        for idx in range(1,size):
            prefixSum[idx] += prefixSum[idx-1]
        
        ans =""
        for idx in range(size):
            ASCII_val = ord(s[idx])+ prefixSum[idx]
            if ASCII_val < 97:
                while ASCII_val < 97:
                    ASCII_val += 26
            elif ASCII_val > 122:
                while ASCII_val > 122:
                    ASCII_val -= 26
                
            ans += chr(ASCII_val)
        return ans
                