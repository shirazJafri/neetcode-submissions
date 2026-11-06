class Solution:
    def scoreOfString(self, s: str) -> int:
        strScore = 0
        strAsciiValues = [ord(char) for char in s]

        for i in range(1, len(strAsciiValues)):
            strScore += abs(strAsciiValues[i - 1] - strAsciiValues[i])

        return strScore
