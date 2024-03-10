class TicTacToe:
    INFINITY = 10000
    COMPUTER = 'X' # Maximising player
    PLAYER = 'O'   # Minimising player
    BOARD_SIZE = 9 # 3x3 is represented as a 1d array of size 9 (for simplicity)

    def __init__(self):
        self.board = [' ' for _ in range(self.BOARD_SIZE)]
        
    def evaluate(self):
        scores = {
            self.COMPUTER : 1,
            self.PLAYER : -1
        }
        # I cant be bothered to make this work for all board sizes. It works for only 3x3 for now
        directions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for dir in directions:
            if self.board[dir[0]] == self.board[dir[1]] == self.board[dir[2]] != ' ':
                winner = self.board[dir[0]]
                return scores[winner]

        return 0
    
    def isBoardFull(self):
        if self.board.count(' ') == 0:
            return True
        else:
            return False
        
    # Only returns the evaluation. getComputerMove is doing the actual move selection
    def miniMax(self, player):
        if self.evaluate() !=0:
            return self.evaluate()
        
        if self.isBoardFull():
            return 0
        
        if player == self.COMPUTER:
            bestScore = - self.INFINITY
            for i in range(self.BOARD_SIZE):
                if self.board[i] != ' ':
                    continue

                # Make move
                self.board[i] = self.COMPUTER

                score = self.miniMax(self.PLAYER)
                bestScore = max(bestScore, score) # Maximising

                # Unmake move
                self.board[i] = ' '
        
        else:
            bestScore = self.INFINITY
            for i in range(self.BOARD_SIZE):
                if self.board[i] != ' ':
                    continue

                # Make move
                self.board[i] = self.PLAYER

                score = self.miniMax(self.COMPUTER)
                bestScore = min(bestScore, score) # Minimising
                
                # Unmake move
                self.board[i] = ' '
        return bestScore

    def getComputerMove(self):
        bestMove = None
        bestScore = - self.INFINITY  # Since computer is maximising
        for i in range(self.BOARD_SIZE):
            if self.board[i] != ' ':
                continue
            
            # Make move
            self.board[i] = self.COMPUTER

            score = self.miniMax(self.PLAYER)
            if score > bestScore:
                bestScore = score
                bestMove  = i

            # Unmake move
            self.board[i] = ' '

        return bestMove


    def printBoard(self):
        # Cant be bothered to make it work for all sizes
        for i in range(self.BOARD_SIZE):
            print(self.board[i],  end="|") # end= prevents new line after every print call

            if (i+1) % 3 == 0:
                print("")

    def checkForWins(self):
        if (self.evaluate() == 1):
            print("You really lost tic tac toe huh? Your parents must be proud...")
            exit(0)
        
        if (self.evaluate() == -1):
            print("There's no way your stupid ass is winning. Idek why this print statement is here")
            exit(0)
        
        if self.isBoardFull():
            print("Wow a tie! How interesting....")
            exit(0)

if __name__ == "__main__":
    ai = TicTacToe()

    while(True):
        ai.printBoard()
        userMove = int(input("Enter an index (0 to 8): "))

        if userMove< 0 or userMove > 8 or ai.board[userMove] != ' ':
            print("YOU STOOPID FAILURE")
            continue

        ai.board[userMove] = ai.PLAYER
        ai.checkForWins()

        computerMove = ai.getComputerMove()
        ai.board[computerMove] = ai.COMPUTER
        ai.checkForWins()

        print("************************************")