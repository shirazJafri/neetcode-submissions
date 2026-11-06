class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def anagramKey(self, hashMap: dict[str, List[str]], s: str) -> str:
        for string in hashMap:
            if self.isAnagram(string, s):
                return string
        return None

    def formattedOutput(self, hashMap: dict[str, List[str]]) -> List[List[str]]:
        output = []
        for key, value in hashMap.items():
            value.append(key)
            output.append(value)
        return output

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for string in strs:
            anagramKey = self.anagramKey(hashMap, string)
            if anagramKey is None:
                hashMap[string] = []
            else:
                hashMap[anagramKey].append(string)

        return self.formattedOutput(hashMap)
