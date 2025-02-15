from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # 현재 도달 가능한 최대 인덱스
        
        for i, jump in enumerate(nums):
            if i > max_reach:  # 현재 위치가 도달할 수 없는 곳이라면 False
                return False
            max_reach = max(max_reach, i + jump)  # 최대 도달 가능 위치 갱신
            
            if max_reach >= len(nums) - 1:  # 마지막 인덱스에 도달 가능하면 True
                return True
        
        return False  # 마지막까지 도달 못하면 False