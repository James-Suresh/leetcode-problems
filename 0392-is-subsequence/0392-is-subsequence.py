class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l=0
        r=len(t)-1
        s=list(s)
        while l<r:
            if len(s) == 0:
                return True
            while l<r and t[l] != s[0]:
                l+=1
            while l<r and t[r] != s[-1]:
                r-=1
          
            if t[l] == s[0]:
                
                if l==r:
                    break
                s.pop(0)
                l+=1
                
            if s and t[r] == s[-1]:
                s.pop()
                r-=1
        
        if l == r and len(s)>0:
            if s[0]==t[l]:
                s.pop()

        if len(s) == 0:
                return True
        return False
        