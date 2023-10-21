class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        
        """
        t = temperatures
        ans=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):

            while len(stack)>0 and t > stack[-1][1]:
                stack_i , stack_t = stack.pop()
                ans[stack_i] = i-stack_i
            stack.append([i,t])
        return ans




            