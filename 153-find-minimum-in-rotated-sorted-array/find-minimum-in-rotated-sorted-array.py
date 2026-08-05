class Solution(object):
    def findMin(self, nums):
        """
        so we need to find corelation between max and min values while executing
        binary search algo

        """
        # if nums == []: return nums

        # Min = nums[0]
        # l, r = 0, len(nums) - 1 
        # while l < r:
        #     m = (l + r) // 2
        #     # if nums[] 

        #     if nums[m] < nums[l]:
        #         r = m - 1                
        #     else:
        #         Min = min(nums[m], Min)
        #         l = m + 1
        # return Min

        return sorted(nums)[0]