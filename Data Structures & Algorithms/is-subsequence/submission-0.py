class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and not t:
            return True

        ptrS = 0
        ptrT = 0

        while ptrS < len(s) and ptrT < len(t):
            if s[ptrS] == t[ptrT]:
                ptrS += 1
                ptrT += 1
            else:
                ptrT += 1

        return ptrS == len(s)
