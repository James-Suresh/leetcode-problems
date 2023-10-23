class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int

        """
        pos_speed = list(zip(position,speed))
        pos_speed.sort(reverse=True)
        stack=[]
        res=0

        for i,p in enumerate(pos_speed):
            t = float(target - p[0])/float(p[1])
            print t
            if stack and stack[-1]>=t:
                continue
            else:
                stack.append(t)
                res+=1
      
        return res

        