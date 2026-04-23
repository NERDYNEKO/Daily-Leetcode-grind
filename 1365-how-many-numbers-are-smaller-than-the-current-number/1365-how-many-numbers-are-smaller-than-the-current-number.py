class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        result = []
        
        for num in nums:
            result.append(sorted_nums.index(num))  # gives count
        
        return result
        
        
            