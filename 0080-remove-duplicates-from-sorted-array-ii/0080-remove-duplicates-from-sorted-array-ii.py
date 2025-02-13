class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return len(nums)  # 길이가 2 이하라면 이미 조건 충족
        
        write_index = 2  # 중복 허용 개수 (최대 2개까지 허용)
        
        for read_index in range(2, len(nums)):
            if nums[read_index] != nums[write_index - 2]:  # 중복 2개 이상 허용 안됨
                nums[write_index] = nums[read_index]
                write_index += 1
        
        return write_index  # 중복 제거 후 유효한 길이 반환
