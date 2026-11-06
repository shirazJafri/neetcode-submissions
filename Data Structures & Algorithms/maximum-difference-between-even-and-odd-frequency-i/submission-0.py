from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)

        a1, a2 = 0, 101
        for value in counts.values():
            if value % 2 == 0:
                a2 = min(a2, value)
            else:
                a1 = max(a1, value)

        return a1 - a2
