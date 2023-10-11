class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1 = 0
        p2 = len(s) - 1

        while True:
            if p1 >= p2:
                return True
            if not s[p1].isalnum():
                p1 += 1
                
                continue
            if not s[p2].isalnum():
                p2 -= 1
                
                continue
            if s[p1].lower() == s[p2].lower():
                print s[p1] + str(p1)  
                print s[p2] + str(p2)
                p1 += 1
                p2 -= 1
            else:
                return False

                
            
            
            
                       