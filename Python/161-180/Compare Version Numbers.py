class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = [int(r) for r in version1.split('.')]
        l2 = [int(r) for r in version2.split('.')]
        
        for val1, val2 in itertools.zip_longest(l1, l2, fillvalue = 0):
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
            
        return 0
