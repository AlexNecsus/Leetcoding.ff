class Solution(object):
    def minEatingSpeed(self, piles, h):
        # upgrade result to least possible time
        # math.ceil for division rounding 
        # if hours <= h 
        # k =? 1 - max(piles)
        res = [0]
        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += ((p + k - 1)// k)
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res