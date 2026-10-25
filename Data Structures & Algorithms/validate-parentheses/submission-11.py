class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for char in s:
            if char in valid:
                stack.append(valid[char])
            elif not stack or stack.pop() != char:
                return False
                
        return not stack

        




            
            
            
            
        
        

