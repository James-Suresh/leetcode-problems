class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        res=0
        cset = set()
        for i in allowed:
            cset.add(i)
        for w in words:
            for i,c in enumerate(w):
                if c not in cset:
                    break
                elif i==len(w)-1:
                    res+=1
        
        return res
                    
        