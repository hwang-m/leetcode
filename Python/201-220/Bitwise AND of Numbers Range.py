class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n: return m
        
        ms = bin(m)[2:].zfill(31)
        ns = bin(n)[2:].zfill(31)
        
        # find the first bit where m and n differ.
        for i in range(31):
            if ms[i] != ns[i]:
                break
        # since m and n are different, will break before the end.
        # fill the rest with 0's
        return int(ms[:i] + (31-i) * '0', 2)
