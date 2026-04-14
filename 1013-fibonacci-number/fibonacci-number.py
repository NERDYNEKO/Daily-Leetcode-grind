class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        prev=0
        current=1
        for i in range(2,n+1):
            next_value=prev+current
            prev=current
            current=next_value
        return current
                    
        
                    
        