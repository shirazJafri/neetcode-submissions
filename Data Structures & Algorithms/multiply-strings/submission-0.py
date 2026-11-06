class Solution:
    def getNumberFromString(self, numStr: str) -> int:
        num = 0
        index = 0
        pow = len(numStr) - 1

        while pow >= 0 and index < len(numStr):
            num += int(numStr[index]) * (10**pow)
            index += 1
            pow -= 1

        return num

    def multiply(self, num1: str, num2: str) -> str:
        result = self.getNumberFromString(num1) * self.getNumberFromString(num2)

        return str(result)
