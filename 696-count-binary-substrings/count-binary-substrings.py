class Solution(object):
    def countBinarySubstrings(self, s):
        """
        add min neighbor between two consecutive aligned measured values except not forgetting last difference
        """
        cur, prev, count = 1, 0, 0
        for bi in range(1, len(s)):
            if s[bi-1] != s[bi]:
                count += min(prev, cur)
                prev = cur
                cur = 1
                continue
            cur += 1

        return count + min(prev, cur)