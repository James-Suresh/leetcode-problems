class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        out = set()
        for p in paths:
            out.add(p[1])
        for p in paths:
            if p[0] in out:
                out.remove(p[0])
            
        
        return out.pop()
                
                