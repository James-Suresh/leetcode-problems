class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        s_arr = s.split()
        first=True
        for item in reversed(s_arr):
            if(first==True):
                first=False
            else:
                output+=" "
            output+=item
            
        return output