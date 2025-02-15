from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # 초기 최소 가격을 무한대로 설정
        max_profit = 0  # 최대 이익 초기화
        
        for price in prices:
            if price < min_price:
                min_price = price  # 새로운 최저가 갱신
            else:
                max_profit = max(max_profit, price - min_price)  # 최대 이익 갱신
        
        return max_profit  # 최대 이익 반환