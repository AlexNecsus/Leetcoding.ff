class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        [3,6,7,11] max = 11, len = 4 -> range(4-11) -> mid(k) = 8, ceil(pile / k) -> (3.. / k) -> 1, 1, 1, 2 => 5 because this value isnt minimal nearset to hour we have to go either high or low, we choose low in our case
         max and len(piles)
        """
        
        def can_finish(k):
            time = 0
            for p in piles:
                time += (p + k - 1) // k
                if time > h:
                    return False
            return True

        low, high = 1, max(piles)
        
        while low < high: 
            k = (high + low) // 2
            if can_finish(k):
                high = k
            else:
                low = k + 1
        return low
