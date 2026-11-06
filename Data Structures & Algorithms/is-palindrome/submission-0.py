import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex_pattern = re.compile("[\W_]+")
        clean_string = regex_pattern.sub("", s)
        clean_string = clean_string.lower()

        start_pointer = 0
        end_pointer = len(clean_string) - 1

        while start_pointer <= end_pointer:
            if clean_string[start_pointer] != clean_string[end_pointer]:
                return False

            start_pointer += 1
            end_pointer -= 1

        return True
