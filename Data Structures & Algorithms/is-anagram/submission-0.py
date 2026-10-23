class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChar = {}
        tChar = {}
        for char in s:
            if char not in sChar:
                sChar[char] = 1
            else:
                sChar[char] += 1
        for char in t:
            if char not in tChar:
                tChar[char] = 1
            else:
                tChar[char] += 1
        if tChar == sChar:
            return True
        return False
        