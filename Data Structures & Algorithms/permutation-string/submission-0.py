class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        NUMBER_OF_CHARACTERS = 26
        START_IDX_CHAR = ord("a")

        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        counts_s1 = [0] * NUMBER_OF_CHARACTERS
        counts_s2 = [0] * NUMBER_OF_CHARACTERS

        for i in range(n1):
            counts_s1[ord(s1[i]) - START_IDX_CHAR] += 1
            counts_s2[ord(s2[i]) - START_IDX_CHAR] += 1

        if counts_s1 == counts_s2:
            return True

        for i in range(n1, n2):
            counts_s2[ord(s2[i]) - START_IDX_CHAR] += 1
            counts_s2[ord(s2[i - n1]) - START_IDX_CHAR] -= 1
            if counts_s2 == counts_s1:
                return True

        return False
