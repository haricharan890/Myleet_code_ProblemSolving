class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        intMAX = 2**31 - 1
        intMIN = -2**31
        if dividend == intMIN and divisor == -1:
            return intMAX
    
        negative = (dividend < 0) ^ (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0
        while a >= b:
            temp = b
            multiple = 1
            while (temp << 1) <= a:
                temp <<= 1
                multiple <<= 1
            a -= temp
            quotient += multiple
    
        if negative:
            quotient = -quotient
        if quotient < intMIN:
            return intMIN
        if quotient > intMAX:
            return intMAX
        return quotient