class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit_sum=0
            n=nums[i]
            while n>0:
                last_digit=n%10
                digit_sum+=last_digit
                n=n//10
                nums[i]=digit_sum
        return min(nums)



