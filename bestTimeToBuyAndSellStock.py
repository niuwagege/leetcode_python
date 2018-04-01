class Solution(object):
    """
    :type prices: List[int]
    :rtype: int
    """
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        buy = prices[0]
        reward = 0
        for i in range(1, len(prices)):
            if prices[i] > buy:
                cur_reward = prices[i] - buy
                if cur_reward > reward:
                    reward = cur_reward
            elif prices[i] < prices[i - 1]:
                buy = prices[i]
        return reward

