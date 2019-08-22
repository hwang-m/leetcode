# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        if isBadVersion(left):
            return left
        while right - left > 1:
            avg = int((left + right) / 2)
            if isBadVersion(avg):
                right = avg
            else:
                left = avg
        return right
