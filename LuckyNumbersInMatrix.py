import sys
class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        minrow, maxcol = [],[]
        for i in range(len(matrix)):
            minrowval = matrix[i][0]
            for j in range(len(matrix[0])):
                if(matrix[i][j]<minrowval):
                    minrowval = matrix[i][j]
            minrow.append(minrowval)
        for i in range(len(matrix[0])):
            maxcolval = matrix[0][i]
            for j in range(len(matrix)):
                if(matrix[j][i]>maxcolval):
                    maxcolval = matrix[j][i]
            maxcol.append(maxcolval)
        result=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] in minrow and matrix[i][j] in maxcol):
                    result.append(matrix[i][j])
        return result

                


                
        