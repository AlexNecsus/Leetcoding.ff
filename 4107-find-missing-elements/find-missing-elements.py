class Solution(object):
    def findMissingElements(self, nums):
        """
        we need to get min, then max
        after that we need to check range for missing
        """
        final = []
        if len(nums) > 1:
            nums.sort()
            # list.extend(range(1, num + 1))
            res = []
            res.extend(range(nums[0], nums[-1] + 1))
            # res = res - nums
            nums = set(nums)
            final = [item for item in res if item not in nums]
        return final