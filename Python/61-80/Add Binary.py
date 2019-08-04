class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0 or a == '0':
            return b
        if len(b) == 0 or b == '0':
            return a
        
        q, r = (int(a[-1]) + int(b[-1])) // 2, (int(a[-1]) + int(b[-1])) % 2
        
        return self.addBinary(self.addBinary(a[:-1], b[:-1]), str(q)) + str(r)
