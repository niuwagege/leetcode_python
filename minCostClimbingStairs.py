class Solution(object):
    def __init__(self):
        self.cost_history_list = list()


    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        self.cost_history_list = [-1] * len(cost)
        return min(self.recursiveMinCostCS(cost, len(cost)-1), self.recursiveMinCostCS(cost, len(cost)-2))


    def recursiveMinCostCS(self, cost, index):
        if index <= 1:
            if self.cost_history_list[index] == -1:
                self.cost_history_list[index] = cost[index]
        else:
            if self.cost_history_list[index] == -1:
                self.cost_history_list[index] = cost[index] + min(self.recursiveMinCostCS(cost, index-1),
                                                                  self.recursiveMinCostCS(cost, index-2))
        return self.cost_history_list[index]


class Solution2(object):
    def __init__(self):
        self.cost_history_list = list()

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp1, dp2, cur_dp = 0, 0, 0
        for i in range(2,len(cost)+1):
            cur_dp = min(dp1+cost[i-2], dp2+cost[i-1])
            dp1 = dp2
            dp2 = cur_dp
        return cur_dp


