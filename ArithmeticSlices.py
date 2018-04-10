class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<3:
            return 0
        count = 0
        start = 0
        step = A[1] - A[0]
        for end in range(2,len(A)):
            if A[end] - A[end-1] != step:
                count += (end-start-1)*(end-start-2)/2
                step = A[end] - A[end-1]
                start = end - 1
        count += (end-start)*(end-start-1)/2
        return count


obj = Solution()
obj.numberOfArithmeticSlices([1, 2,3,4])
