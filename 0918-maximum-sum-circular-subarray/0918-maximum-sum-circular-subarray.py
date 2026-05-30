class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_sum=nums[0]
        global_max=nums[0]
        global_min=nums[0]
        current_min=nums[0]
        total_sum=0

        for i in range(1,len(nums)):
            current_sum= max(nums[i] , current_sum + nums[i])
            global_max= max(global_max , current_sum)
        
        for i in range(1,len(nums)):
            current_min= min(nums[i] , current_min + nums[i])
            global_min= min(global_min , current_min)
        total_sum=sum(nums)

        if global_max < 0:
            return global_max
        
        return max(global_max, total_sum - global_min)