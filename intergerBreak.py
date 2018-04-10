class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 1
        result = [1] * (n+1)
        result[2] = 2
        for i in range(3, n+1):
            result[i] = 0
            for j in range(1, i//2+1):
                cur = result[j] * result[i-j]
                if cur > result[i]:
                    result[i] = cur
            if i != len(result) - 1 and i > result[i]:
                result[i] = i
        return result[-1]

if __name__ == "__main__":
    obj = Solution()
    obj.integerBreak(6)