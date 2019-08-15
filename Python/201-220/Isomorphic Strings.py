class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #assume s and t have the same length
        table = {}
        valueset = set()
        
        for cs, ct in zip(s, t):
            if not cs in table:
                if not ct in valueset:
                    table[cs] = ct
                    valueset.add(ct)
                else:
                    return False
            elif cs in table and table[cs] != ct:
                return False
        
        return True
