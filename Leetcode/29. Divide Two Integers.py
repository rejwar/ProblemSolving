class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 1:
            return dividend if dividend >= -2147483648 else -2147483648
        if divisor == -1:
            return -dividend if -dividend < 2147483648 else 2147483647

        sign = 1
        if dividend < 0:
            sign *= -1
        if divisor < 0:
            sign *= -1

        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor
        
        res = 0
        i = 1
        while dividend >= divisor:
            if divisor ** (i+1) > dividend:
                res += divisor**(i-1)
                dividend -= divisor**i
                i = 1
            else:
                i += 1
        return sign*res
