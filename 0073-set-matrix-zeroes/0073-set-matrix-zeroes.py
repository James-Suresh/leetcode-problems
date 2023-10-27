class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_arr = [0]*len(matrix[0])
        zero_loc=[]
        for i,m in enumerate(matrix):
            if 0 in m:
                for k,n in enumerate(m):
                    if n == 0:
                        zero_loc.append(k)
                matrix[i]=zero_arr
        for i in range(len(matrix[0])):
            if i in zero_loc:
                for k in matrix:
                    k[i]=0
