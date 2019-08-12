class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        st = '{0:032b}'.format(n)
        return int(st[::-1], 2)
