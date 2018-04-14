class Solution(object):
    def arrangement(self, x, y):
        result = 1
        for i in range(x + 1, y + 1):
            result *= i
        return result

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 10
        elif n == 2:
            return 91
        result = [0] * min(n + 1, 11)
        result[0], result[1], result[2] = 1, 10, 91

        for i in range(3, min(n + 1, 11)):
            result[i] = result[i - 1] + self.arrangement(10 - i, 10) - self.arrangement(10 - i, 9)

        return result[-1]


obj = Solution()
# print(obj.countNumbersWithUniqueDigits(0))
# print(obj.countNumbersWithUniqueDigits(1))
# print(obj.countNumbersWithUniqueDigits(2))
print(obj.countNumbersWithUniqueDigits(10))
print(obj.countNumbersWithUniqueDigits(13))