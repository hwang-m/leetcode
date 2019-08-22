class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        # count the number of papers with c citations for c from 0 to n
        count = [0] * (n+1)
        for c in citations:
            if c > n:
                count[n] += 1
            else:
                count[c] += 1
        
        # modify list to count papers with at least c citations
        for i in range(n, 0, -1):
            count[i-1] = count[i-1] + count[i]
        
        # find h-index
        for h in range(n+1):
            if count[h] < h: return h-1
        return n
