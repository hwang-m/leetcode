class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dic = {0:1,
              1:1+9,
              2:1+9+9*9,
              3:1+9+9*9+9*9*8,
              4:1+9+9*9+9*9*8+9*9*8*7,
              5:1+9+9*9+9*9*8+9*9*8*7+9*9*8*7*6,
              6:1+9+9*9+9*9*8+9*9*8*7+9*9*8*7*6+9*9*8*7*6*5,
              7:1+9+9*9+9*9*8+9*9*8*7+9*9*8*7*6+9*9*8*7*6*5+9*9*8*7*6*5*4,
              8:1+9+9*9+9*9*8+9*9*8*7+9*9*8*7*6+9*9*8*7*6*5+9*9*8*7*6*5*4+9*9*8*7*6*5*4*3,
              9:1+9+9*9+9*9*8+9*9*8*7+9*9*8*7*6+9*9*8*7*6*5+9*9*8*7*6*5*4+9*9*8*7*6*5*4*3+9*9*8*7*6*5*4*3*2,
              10:1+9+9*9+9*9*8+9*9*8*7+9*9*8*7*6+9*9*8*7*6*5+9*9*8*7*6*5*4+9*9*8*7*6*5*4*3+9*9*8*7*6*5*4*3*2+9*9*8*7*6*5*4*3*2*1
              }
        if n in dic: return dic[n]
        if n > 10: return dic[10]
