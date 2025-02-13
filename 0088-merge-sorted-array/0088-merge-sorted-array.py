class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1+nums2
        nums1.sort()
        nums1[:] = [x for x in nums1 if x!=0]

        