class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            result +=1
            left = i -1
            right = i + 1
            # print(s[i])
            while left >= 0 and right <len(s) and s[left] == s[right]:
                result += 1
                left -=1
                right +=1
            if i+1< len(s) and s[i] == s[i+1]:
                result += 1
                left = i -1
                right = i + 2
                while left >= 0 and right <len(s) and s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1
        return result


if __name__ == "__main__":
    obj = Solution()
    obj.countSubstrings("aaa")