class Solution:
    def firstUniqChar(self, s: str) -> int:
        prev={}
        for i in s:
            if i in prev:
                prev[i]+=1
            else:
                prev[i]=1
        for i in s:
            if prev[i]==1:
                return s.index(i)
        return -1  
            