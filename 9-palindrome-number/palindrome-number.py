class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=x
        if x<0:
            return False
        rev=0
        while x>0:
            last_digit=x%10
            rev=rev*10+last_digit
            x=x//10
        if rev==original:
            return True
        else:
            return False
