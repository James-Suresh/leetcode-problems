class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        hm={}
        wset=set()
        pset=set()
        l= s.split(" ")
        if (len(pattern)!=len(l)):
            return False
        for i,c in enumerate(pattern):
            if l[i] in wset:
                if c == hm[l[i]]:
                    continue
                else:
                    return False
            elif c not in pset:
                hm[l[i]] = c
                wset.add(l[i])
                pset.add(c)
            else:
                return False
        return True