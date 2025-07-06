class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1 or n == 7:
            return True
        
        sett = {n,2,3,4,5,6,8,9}

        while True:

            ssum = 0
            while n != 0:
                last = n%10
                n = n //10
                ssum += last**2
            n = ssum
            if ssum == 1:
                return True
            if n in sett:
                return False
            else:
                sett.add(n)

