from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0  # 총 이익
        
        for i in range(1, len(prices)):  # 첫째 날 이후부터 탐색
            if prices[i] > prices[i - 1]:  # 가격이 상승하는 경우 차익 실현
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit  # 최대 이익 반환