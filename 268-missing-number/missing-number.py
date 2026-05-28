class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        prev=[]
        n=len(nums)
        for i in range(0,n+1):
            if i  not in prev:
                prev.append(i)
            if  i not in nums:
                return i
            
      