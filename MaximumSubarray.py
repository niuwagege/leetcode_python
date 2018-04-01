class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub = nums[0]
        cur = nums[0]
        for i in range(1,len(nums)):
            if cur <= 0 :
                cur = 0
            cur += nums[i]
            if cur > max_sub:
                max_sub = cur
        return max_sub