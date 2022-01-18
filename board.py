"""
Adnane CHEJJARI
January 2022
"""

class Board():
    def __init__(self):
        self.size = 4
        self.board = [[0 for i in range(self.size)] for i in range(self.size)]
        self.offsetVector = [0 for i in range(self.size)]

    def getSize(self):
        return self.size

    def getBoard(self):
        return self.board
    
    def modifyBoard(self, i,j, sign):
        self.board[i][j] = sign

    def getOffsetVector(self):
        return self.offsetVector

    def offsetRow(self, row, direction):
        self.offsetVector[row]+=direction



class Game():
    def __init__(self):
        self.board = Board()

    def checkRows(self):
        boardToCheck = self.board.getBoard()
        for i in range(self.board.getSize()):
            if len(set(boardToCheck[i])) == 1:
                return True
        return False

    def getBoardOffset(self):
        return self.board.getOffsetVector()
            
    def getBoard(self):
        return self.board.getBoard()
    
    def getBoardSize(self):
        return self.board.getSize()

    def boardWithOffset(self):
        copiedBoard = [[0 for i in range(10)] for i in range(self.size)]
        boundary = 4
        offsetVector = self.getBoardOffset
        for i in range(self.getBoardSize()):
            copiedBoard[i][boundary+offsetVector[i]:boundary+offsetVector[i]+self.getBoardSize()]
        return copiedBoard
        

    def checkColumns(self):
        pass

        
    def checkDiagonals(self):
        pass

    def endGame(self):
        return self.checkRows() and self.checkColumns() and self.checkDiagonals()

