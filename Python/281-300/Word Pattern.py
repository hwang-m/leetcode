class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        lis = str.split()
        return len(pattern) == len(lis) and len(set(pattern)) == len(set(lis)) and len(set(pattern)) == len(set(zip(pattern, lis)))
