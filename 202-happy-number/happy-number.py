class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while True:
            if n==1:
                return True
            if n in seen:
                return False
            seen.add(n)

            total=0
            while(n):
                digit=n%10
                num=digit**2
                total+=num
                n=n//10
            n=total