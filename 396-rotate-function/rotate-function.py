class Solution(object):
    def maxRotateFunction(self, nums):
        """
        f0 = f + total - (N * nums[N - i])
        """
        
        total = 0
        f0 = 0
        for i in range(len(nums)):
            total += nums[i]
            f0 += (i * nums[i]) 
        
        Max = f0
        lf = f0
        for i in range(1, len(nums)):
            f = lf + total - (len(nums) * nums[len(nums) - i])
            Max = max(Max, f)
            lf = f
        return Max