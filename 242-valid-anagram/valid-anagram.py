class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # either we can count using dictionary , decide by decrementing out alphabet counter, 
        """
        we could set counter and decrement values of other values and if any value becomes negative or unknown letter come out then False
        """
        if len(t) != len(s): return False 
        count = collections.defaultdict(int)
        for l in s:
            count[l] += 1
        
        for l in t:
            count[l] -= 1
            if count[l] < 0:
                return False
        return True # [l == 0 for l in count]