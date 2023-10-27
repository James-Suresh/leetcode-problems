class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1=[]
        stack2=[]
        for item in s:
            if item == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(item)
        for item in t:
            if item == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(item)
        return stack1 == stack2
