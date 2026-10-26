class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        schar = {}
        tchar = {}
        for char in s:
            if char not in schar:
                schar[char] = 1
            else:
                schar[char] += 1
        
        for char in t:
            if char not in schar:
                return False
            elif char not in tchar:
                tchar[char] = 1
            else:
                tchar[char] += 1

        return schar == tchar
        