class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def palCheck(w):
            
            if len(w)<=1:
                return True
            l=0
            r=len(w)-1
            while l<r:
                if w[l] == w[r]:
                    l+=1
                    r-=1
                else: 
                    return False
            return True

        depth=1
        ans=''
        if palCheck(s):
            return s
        while depth<len(s) and ans=="":
            
            for d in range((depth+1)):
                if palCheck(s[d:d+len(s)-depth]):
                    ans=s[d:d+len(s)-depth]
                    return ans
            depth+=1
                





        
              
        
            
        

            