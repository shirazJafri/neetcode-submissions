class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        pow = n - 1

        num = 0
        for digit in digits:
            num += digit * (10**pow)
            pow -= 1

        plusOne = num + 1
        reversedResult = []
        while plusOne > 0:
            reversedResult.append(plusOne % 10)
            plusOne //= 10

        return list(reversed(reversedResult))
