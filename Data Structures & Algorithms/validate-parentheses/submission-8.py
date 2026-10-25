class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for char in s:
            if char not in valid:
                stack.append(char)
            elif stack == []:
                return False
            elif valid[char] != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack

        




            
            
            
            
        
        

