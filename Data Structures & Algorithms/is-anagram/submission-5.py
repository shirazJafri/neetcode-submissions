class Solution:
    def getCharCounts(self, s: str) -> dict:
        charCounts = {}
        for char in s:
            charCounts[char] = charCounts.get(char, 0) + 1
        return charCounts

    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        
        if len(s) != len(t):
            return False

        sCharCounts = self.getCharCounts(s)
        tCharCounts = self.getCharCounts(t)
        
        return sCharCounts == tCharCounts
