class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        s1, s2 = 1, 2

        for i in range(3, n + 1):
            cur_s = s1 + s2
            s1, s2 = s2, cur_s
        return cur_s
