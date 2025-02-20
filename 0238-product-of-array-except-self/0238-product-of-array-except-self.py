class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lanswer = [1] * len(nums)
        for l in range(1,len(nums)):
            lanswer[l]  = lanswer[l-1] * nums[l-1] 

        ranswer = [1] * len(nums)
        for r in range(len(nums)-2, -1, -1):
            ranswer[r] = ranswer[r+1] * nums[r+1]
        
        answer = [1] * len(nums)
        for i in range(len(nums)):
            answer[i] = lanswer[i] * ranswer[i]
            

        return answer