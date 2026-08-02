class Solution(object):
    def topKFrequent(self, nums, k):
        """
        freq is all we need , and there's also heap
        1. we count freaquency, 2. change val with keys , 3. we go through frequeny in reverse order.
        """
        count = collections.defaultdict(int) 
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for f in freq[i]:
                res.append(f)
                if len(res) == k:
                    return res