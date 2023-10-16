class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        plist = []
        stack=[]
        def pfunc(popen, pclosed):
            if popen==pclosed==0:
                plist.append("".join(stack))
                return
            if popen>0:
                stack.append("(")
                pfunc(popen-1,pclosed)
                stack.pop()
            if popen<pclosed:
                stack.append(")")
                pfunc(popen,pclosed-1)
                stack.pop()
        pfunc(n,n)
        return plist
                