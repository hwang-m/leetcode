class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        terms = [0] * (len(num1) + len(num2) - 1)
        
        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                terms[i + j] += int(n1) * int(n2)
                
        #note: the following returns 000...00 for num * 0
        # for i in range(len(num1) + len(num2) - 2, 0, -1):
        #     ans[i - 1] += ans[i] // 10
        #     ans[i] = str(ans[i] % 10)
        # ans[0] = str(ans[0])
        # return ''.join(ans)
        
        product = 0
        for val in terms:
            product = product * 10 + val
        return str(product)
