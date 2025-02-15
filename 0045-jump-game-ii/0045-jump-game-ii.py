from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # 이미 목표에 도달한 경우 점프 필요 없음
        
        jumps = 0  # 점프 횟수
        max_reach = 0  # 현재까지 도달할 수 있는 가장 먼 위치
        end = 0  # 현재 점프에서 도달할 수 있는 끝 위치
        
        for i in range(n - 1):  # 마지막 인덱스는 점프할 필요 없음
            max_reach = max(max_reach, i + nums[i])  # 최대 도달 가능 위치 업데이트
            
            if i == end:  # 현재 점프의 끝에 도달한 경우
                jumps += 1
                end = max_reach  # 새로운 점프 범위 설정
                
                if end >= n - 1:  # 마지막 위치에 도달 가능하면 종료
                    break
        
        return jumps