class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n > 0:
            ans.append(chr((n - 1) % 26 + ord('A')))
            n = (n - 1) // 26
        return ''.join(ans[::-1])
