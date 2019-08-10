class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = ['']
        if numerator * denominator < 0:
            sign = ['-']
        numerator, denominator = abs(numerator), abs(denominator)
        
        q, r = numerator // denominator, numerator % denominator
        quotient = [str(q), '.']
        remainder = []
        
        while str(r) not in remainder:
            remainder.append(str(r))
            q, r = r*10 // denominator, r*10 % denominator
            quotient.append(str(q))
            
        if r == 0:
            quotient.pop()
            if quotient[-1] == '.':
                quotient.pop()
        else:
            i = remainder.index(str(r))
            quotient.insert(i+2, '(')
            quotient.append(')')
        
        return ''.join(sign + quotient)
