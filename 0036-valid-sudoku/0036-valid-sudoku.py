class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r = [[] for _ in xrange(9)]
        c = [[] for _ in xrange(9)]
        sq =[[] for _ in xrange(9)]
        count = 0
        for i in range (len(board)):
            for j in range(len(board[i])):
                sqnum = ((i//3)*3) + (j//3) 
                if (board[i][j] == '.'):
                    continue
                elif (
                    board[i][j] in r[i] or
                    board[i][j] in c[j] or
                    board[i][j] in sq[sqnum]):
                    print sq 
                    return False
                else:
                    r[i].append(board[i][j])
                    c[j].append(board[i][j])
                    sq[sqnum].append(board[i][j])
        return True
