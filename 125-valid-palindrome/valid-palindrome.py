class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        result=""
        left=0
        
        for i in s:
            if i.isalnum():
                result+=i
        right=len(result)-1
        while left<right:
            if result[left]!=result[right]:
                return False
            left+=1
            right-=1
           
        return True
            
            


