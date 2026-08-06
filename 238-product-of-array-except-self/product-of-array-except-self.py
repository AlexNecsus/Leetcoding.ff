class Solution(object):
    def productExceptSelf(self, nums):
        """
        ->
        [1, 2, 3, 4]

            |
        [1, 1, 2, 6] , (2x3)

                  <-
        [1, 2, 3, 4]
                 |
        [24, 12, 8, 6]
        """

        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] 

        postfix = 1
        for i in range(len(nums) -1, -1 , -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res