class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=l=0
        minn=float('inf')
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                minn=min(minn,r-l+1)
                sum-=nums[l]
                l+=1
            
        return 0 if minn==float('inf') else minn   
        