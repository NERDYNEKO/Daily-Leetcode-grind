class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        prev={}
        for i in nums1:
            prev[i]=1
        ans=[]
        for i in nums2:
            if i in prev and i not in ans:
                ans.append(i)
        return ans