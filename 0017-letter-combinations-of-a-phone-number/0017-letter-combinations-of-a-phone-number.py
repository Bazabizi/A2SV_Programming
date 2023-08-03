class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        reference = {
            "2" : ["a" , "b" , "c"],
            "3" : ["d" , "e" , "f"],
            "4" : ["g" , "h" , "i"],
            "5" : ["j" , "k" , "l"],
            "6" : ["m" , "n" , "o"],
            "7" : ["p" , "q" , "r" , "s"],
            "8" : ["t" , "u" , "v"],
            "9" : [ "w" , "x" , "y" , "z"]
        }
        ans = []
        if len(digits) > 0:
            ans = reference[digits[0]]
            
            for letter in digits[1:]:
                ans = product(ans , reference[letter])
                ans = ["".join(element) for element in ans]        
        ans = list(map(list , ans))
        # print(ans)
        ans = ["".join(element) for element in ans]
        return ans