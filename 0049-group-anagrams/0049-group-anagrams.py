class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prev={}
        for word in strs:
            key=''.join(sorted(word))
            if key in prev:
                prev[key].append(word)
            else:
                prev[key]=[word]

        arr= (list(prev.values()))
        arr.sort(key=len)
        return arr
