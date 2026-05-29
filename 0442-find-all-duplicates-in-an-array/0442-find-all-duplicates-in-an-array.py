class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        prev={}
        for i in nums:
            if i in prev:
                prev[i]+=1
            else:
                prev[i]=1
        for i in prev:
            if prev[i]==2:
                ans.append(i)
        return ans