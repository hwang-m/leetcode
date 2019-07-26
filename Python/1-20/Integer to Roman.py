class Solution:
    def intToRoman(self, num: int) -> str:
        #Input is guaranteed to be within the range from 1 to 3999
        number = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        ans = []
        
        for n, s in zip(number, symbol):
            q, num = num // n, num % n
            ans.append(s * q)
        
        return ''.join(ans)
