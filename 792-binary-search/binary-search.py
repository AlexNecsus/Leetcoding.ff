class Solution(object):
    def Rsearch(self, l, r, nums, target):
        m = (l + r) // 2
        if l > r: 
            return m if target == nums[m] else -1
        if nums[m] < target:
            return self.Rsearch(m + 1, r, nums, target)
        elif nums[m] > target:
            return self.Rsearch(l, m - 1, nums, target)
        elif nums[m] == target:
            return m
    def search(self, nums, target):
        return self.Rsearch(0, len(nums) - 1, nums, target)