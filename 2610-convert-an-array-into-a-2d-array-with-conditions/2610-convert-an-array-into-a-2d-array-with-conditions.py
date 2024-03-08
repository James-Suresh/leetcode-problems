class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arrlist = [[]]
        
       
        
        def arrcheck(i,j):
            if i not in arrlist[j]:
                arrlist[j].append(i)
            else:
                if len(arrlist)==j+1:
                    arrlist.append([])
                arrcheck(i,j+1)
            
        
        for item in nums:
            arrcheck(item,0)
            
        return arrlist
            
                    