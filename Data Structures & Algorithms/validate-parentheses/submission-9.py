from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        valid = {']': '[', '}': '{', ')': '('}
        
        for char in s:
            if char not in valid:
                stack.append(char)
            elif not stack or valid[char] != stack[-1]:
                return False
            else:
                stack.pop()
        
        return not stack

        




            
            
            
            
        
        

