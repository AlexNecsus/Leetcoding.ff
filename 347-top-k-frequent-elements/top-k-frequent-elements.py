class Solution(object):
    def topKFrequent(self, nums, k):
        """
        heap 
        """
        import heapq
        from collections import Counter

        count = Counter(nums)
        heap = []

        for n, c in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (c, n))
            else:
                heapq.heappushpop(heap, (c, n))
        return [h[1] for h in heap]