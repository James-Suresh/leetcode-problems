class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for i in tokens:
            if i=="+":
                r=stack.pop()
                l=stack.pop()
                stack.append(l+r)
            elif i=="-":
                r=stack.pop()
                l=stack.pop()
                stack.append(l-r)
            elif i=="/":
                r=stack.pop()
                l=stack.pop()
                ans = float(l)/float(r)
                if ans<0:
                    ans = ans * -1
                    ans = int(ans)
                    ans = ans * -1
                else:
                    ans=int(ans)

                stack.append(ans)
            elif i=="*":
                r=stack.pop()
                l=stack.pop()
                stack.append(l*r)
            else:
                stack.append(int(i))

            
        return stack.pop()