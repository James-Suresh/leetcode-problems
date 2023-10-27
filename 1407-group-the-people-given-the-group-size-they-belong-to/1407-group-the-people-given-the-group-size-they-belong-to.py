class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        hm={}
        res=[]
        for i in range(len(groupSizes)):
            if groupSizes[i] == 1:
                res.append([i])
            elif groupSizes[i] in hm:                
                hm[groupSizes[i]].append(i)
                if len(hm[groupSizes[i]])==groupSizes[i]:
                    res.append(hm[groupSizes[i]])
                    hm[groupSizes[i]]=[]
            else:
                hm[groupSizes[i]] = [i]
        return res
        
