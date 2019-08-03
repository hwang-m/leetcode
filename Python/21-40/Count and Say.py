class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        s = self.countAndSay(n - 1)
        ans = []
        pre = -1
        
        for i, val in enumerate(s):
            if i + 1 < len(s) and val == s[i+1]:
                i+=1
            else:
                ans.append(str(i - pre))
                pre = i
                ans.append(val)
        
        return ''.join(ans)
