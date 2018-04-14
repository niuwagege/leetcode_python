class Solution2(object):
    def get_scores(self,nums):
        if len(nums) == 1:
            return nums[0]
        else:
            return max(nums[0]-self.get_scores(nums[1:]),nums[-1]-self.get_scores(nums[:-1]))
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.get_scores(nums)>=0

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        scores = [[0] * (length - j) for j in range(length)]
        for i in range(len(scores)):
            scores[i][0] = nums[i]
        for j in range(1,length):
            for i in range(0,length-j):
                scores[i][j] = max(nums[i+j]-scores[i][j-1],nums[i]-scores[i+1][j-1])
        return scores[0][-1]>=0

obj = Solution()
obj.PredictTheWinner([1,5,2])