class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nm = n // 2 + 1
        nodup = list(set(nums))

        nins = [0]*len(nodup)

        for i in range(0,len(nodup)):
            for ls in range(0,len(nums)):
                if nums[ls] == nodup[i]:
                    nins[i] += 1
        
        for k in range(0,len(nins)):
            if nins[k] > nm:
                return nodup[k]




