class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "}": "{", "]": "["}
        stk = []

        for char in s:
            if char not in hashmap:
                stk.append(char)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[char]:
                        return False
        return not stk
