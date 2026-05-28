class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        prev={}
        
        for i in ransomNote:
            if i in prev:
                prev[i]+=1
            else:
                prev[i]=1

        check={}
        for i in magazine:
            if i in check:
                check[i]+=1
            else:
                check[i]=1
                
        for i in prev:
            if i not in check:
                return False
            if prev[i]>check[i]:
                return False 
        return True
      
