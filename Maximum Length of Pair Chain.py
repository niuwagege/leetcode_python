class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda x: x[1])
        current_key = float("-inf")
        length = 0
        for pair in pairs:
            if pair[0] > current_key:
                length += 1
                current_key = pair[0]

        return length

if __name__ == "__main__":
    obj = Solution()
    obj.findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]])