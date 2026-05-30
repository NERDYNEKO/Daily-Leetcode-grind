class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        current_sum= global_max=nums[0]
        current_min=global_min=nums[0]
        total_sum=sum(nums)

        for i in nums[1:]:
            current_sum= max(i , current_sum + i)
            global_max= max(global_max , current_sum)
        
        for i in nums[1:]:
            current_min= min( i , current_min + i)
            global_min= min(global_min , current_min)


        if global_max < 0:
            return global_max
        
        return max(global_max, total_sum - global_min)