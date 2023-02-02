class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        left = 0 
        right = 1
        size = len(chars)
        while left < size:
            right = left +1
            while right < size and chars[right] == chars[left]:
                right += 1
            chars[index] = chars[left]
            index += 1
            count = str(right-left)
            if count != "1":
                for letter in count:
                    chars[index] = letter
                    index += 1
            left = right
        
        return index