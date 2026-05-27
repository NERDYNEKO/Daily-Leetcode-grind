class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        used=set()
        prev={}
        if len(s)!=len(t):
            return False

        for x,y in zip(s,t):
            if x in prev:
                if prev[x]!=y:
                    return False
            
            if x not in prev:
                if y in used:
                    return False
            prev[x]=y
            used.add(y)
        return True        