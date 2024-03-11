class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        stack=""
        res=""
        for i in command:
            stack = stack+i
            if stack=="G":
                res += "G"
                stack=""
            if stack=="()":
                res += "o"
                stack=""
            if stack=="(al)":
                res += "al"
                stack=""
        
        return res
                
            