class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            '[': ']',
            '{': '}',
            '(': ')'
        }
        for char in s:
            if char in valid:
                stack.append(char)
            elif stack == []:
                return False
            elif char != valid[stack[-1]]:
                return False
            else:
                stack.pop(-1)
        return stack == []

        




            
            
            
            
        
        

