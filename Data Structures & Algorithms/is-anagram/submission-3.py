class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts_s = {}
        char_counts_t = {}

        for char in s:
            char_counts_s[char] = char_counts_s.get(char, 0) + 1

        for char in t:
            char_counts_t[char] = char_counts_t.get(char, 0) + 1

        return char_counts_s == char_counts_t