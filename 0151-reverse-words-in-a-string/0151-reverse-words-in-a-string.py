class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        s_arr = s.split()
        output = " ".join(reversed(s_arr))    
        return output