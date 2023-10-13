class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        start=False
        for i in range(len(s)):
            if s[i].isalnum() and start==False:
                start=True
                count=1
            elif s[i].isalnum() and start==True:
                count+=1
            if not s[i].isalnum():
                start=False
            
        return count 

            

        return count
        