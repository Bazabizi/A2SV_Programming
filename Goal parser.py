class Solution:
    def interpret(self, command: str) -> str:
        result=""
        length=len(command)
        idx=0
        letter_o="()"
        letter_al="(al)"

        while idx<length:
            if command[idx]=='G':
                result +='G'
                idx += 1

            elif command[idx:idx+2]==letter_o:
                result +='o'
                idx += 2
            else:
                result +="al"
                idx += 4
        
        return result
