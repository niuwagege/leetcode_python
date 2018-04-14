class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        total_earn = 0
        buy = prices[0]
        sell = -1
        for price in prices[1:]:
            if sell == -1:
                if price > buy + fee:
                    sell = price
                elif price < buy:
                    buy = price
            else:
                if price < sell - fee:
                    total_earn += sell - buy - fee
                    buy = price
                    sell = -1
                elif price > sell:
                    sell = price
        return total_earn + max(0,sell - buy -fee)

obj = Solution()
obj.maxProfit([1,3,7,5,10,3],3)