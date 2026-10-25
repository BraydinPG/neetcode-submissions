class Solution:
    def isPalindrome(self, s: str) -> bool:
        # If it is a palindrome, the opposites in the string will = each other
        s = "".join(char.lower() for char in s if char.isalnum())
        L, R = 0, len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True
