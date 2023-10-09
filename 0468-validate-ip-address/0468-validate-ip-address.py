class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        
        if '.' in queryIP:
            arr = queryIP.split('.')
            if len(arr) !=  4 :
                return 'Neither'
            for num in arr:
                
                if num.isdigit():
                    val = int(num)
                    if len(str(val)) != len(num) or val >= 256:
                        return 'Neither'
                else:
                    return 'Neither'
            
            return 'IPv4'
        
        arr = queryIP.split(':')
        if len(arr) !=  8:
            return 'Neither'
        for num in arr:
            if 1<= len(num)<= 4:
                for l in num:
                    if not l.isdigit() and not 'A' <= l <= 'F' and not 'a' <= l <= 'f':
                        return 'Neither'
            else:
                return 'Neither'
        return 'IPv6'