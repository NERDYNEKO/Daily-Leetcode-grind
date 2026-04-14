class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak=0
        max_streak=0
        for i in nums:
            if i==1:
                current_streak+=1
            else:
                current_streak=0

            max_streak=max(current_streak,max_streak)
        return max_streak

                    
                


        
       
     
        
           


