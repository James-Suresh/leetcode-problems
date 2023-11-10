class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['A','E','I','O','U','a','e','i','o','u'])
        l=0
        output=list(s)
        r=len(s)-1
        while l<r:
            while s[l] not in vowels and l<r:
                l+=1
            while s[r] not in vowels and l<r:
                r-=1
            output[r],output[l] = output[l],output[r]
            l+=1
            r-=1
            
        return "".join(output)
            
                
                
                
        return s
                
            