class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        categories = {}
        
        def count_letters(word: str):
            ans = [0] * 26
            for char in word:
                ans[ord(char) - ord('a')] += 1
            return tuple(ans)
        
        for word in strs:
            count = count_letters(word)
            if count in categories:
                categories[count].append(word)
            else:
                categories[count] = [word]
        
        if not categories:
            return []
        
        return list(categories.values())
