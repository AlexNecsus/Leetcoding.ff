import math
class Solution(object):
    def smallestNumber(self, n, t):
        """
        digit product eh
        """
        def dpn(n):
            n = abs(n)
            if n == 0:
                return 0
                
            product = 1
            while n > 0:
                digit = n % 10  # Extract the last digit
                if digit == 0:
                    return 0    # Early exit optimization
                product *= digit
                n //= 10
            return product

        dp = dpn(n)
        while dp % t != 0:
            if dp == 0:
                return n
            n += 1
            dp = dpn(n)
        return n