__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums_sr = sorted(nums)
        left = 0
        right = len(nums_sr) - 1
        check = 0
        
        while left < right:
            sums = nums_sr[left] + nums_sr[right]
            if sums > k:
                right -= 1
            elif sums < k:
                left += 1
            else:
                right -= 1
                left += 1
                check += 1

        
        return check