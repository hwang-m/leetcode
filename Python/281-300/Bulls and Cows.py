class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # assume len(secret) == len(guess)
        A = B = 0
        counts = [0] * 10
        countg = [0] * 10
        
        for s, g in zip(secret, guess):
            if s == g:
                A += 1
            else:
                counts[int(s)] += 1
                countg[int(g)] += 1
        
        B = sum(min(i,j) for i, j in zip(counts, countg))
        
        return f'{A}A{B}B'
