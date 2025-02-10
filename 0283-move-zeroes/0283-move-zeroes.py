class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nnums = []
        zr = []
        for n in range(0,len(nums)):
            if nums[n] != 0:
                nnums.append(nums[n])
            else:
                zr.append(nums[n])
        
        nums[:] = nnums + zr
