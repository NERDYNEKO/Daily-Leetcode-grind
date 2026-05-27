class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        used=set()
        prev={}
        if len(pattern)!=len(s):
                return False 
        for x ,y in zip(pattern , s):
            if x in prev:
                if prev[x]==y:
                    pass
                    
                else:
                    return False
            
            if x not in prev:
                 if y in used:
                    return False
            prev[x]=y
            used.add(y)
        return True  
           
            
    
        

                