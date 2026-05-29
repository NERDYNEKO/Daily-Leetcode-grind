class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=[]
        for n in nums:
            sum_digit=0
            while n>0:
                digit=n%10
                sum_digit+=digit
                n=n//10
            ans.append(sum_digit)
        return min(ans)

