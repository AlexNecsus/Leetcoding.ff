class Solution(object):
    def findMin(self, nums):
        """
        so we need to find corelation between max and min values while executing
        binary search algo
        but our guy says that we dont really have to look for a pivot.
        """
        Min = nums[0]
        l, r = 0, len(nums) - 1 
        while l < r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                Min = min(nums[l], Min) 
                break
            Min = min(nums[m], Min)
            if nums[m] < nums[l]:
                r = m - 1                
            else:
                Min = min(nums[r], Min)
                l = m + 1
        return Min
