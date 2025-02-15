from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # k가 n보다 큰 경우, 실제 회전 횟수를 줄이기
        
        # Step 1: 전체 리스트 뒤집기
        nums.reverse()
        
        # Step 2: 처음 k개의 원소를 다시 뒤집기
        nums[:k] = reversed(nums[:k])
        
        # Step 3: 나머지 원소들을 다시 뒤집기
        nums[k:] = reversed(nums[k:])