class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        mxa = 0

        while left < right:
            bt = right - left
            h = min(height[left], height[right])
            mxa = max(mxa, bt * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return mxa 