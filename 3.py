from queue import PriorityQueue

class State:
    def __init__(self, board, parent, move):
        self.board = board   # 2d matrix representing the board
        self.parent = parent # Previous state
        self.move = move # For printing up down left etc... Represents the move that resulted in this state

        self.numRows = len(self.board)
        self.numCols = len(self.board[0])

    def __sub__(self, other): # Overloading subtraction so cleaner code. state - goalState gives heuristic
        distance = 0
        for i in range(self.numRows):
            for j in range(self.numCols):
                if self.board[i][j] != other.board[i][j]:
                    distance += 1
        return distance
    
    def __eq__(self, other): # Two states are equal if their boards are equal
        return ((self - other) == 0) 
    
    def __lt__(self, other): # Needed to make PriorityQueue work. When two states have same priority, it does < on state. 
        # By this we're basically saying that when two states have same priority pop any one of them out
        return True 
        
    def getZeroPosition(self): # Returns (i, j) of 0
        for i in range(self.numRows):
            for j in range(self.numCols):
                if (self.board[i][j] == 0):
                    return (i,j)

    
    def getChildrenStates(self): # Get states for left move, right move etc (only if that move is valid)
        (zero_i, zero_j) = self.getZeroPosition()  # row, col
        directions = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]

        children = []
        for dir in directions:
            new_i = zero_i + dir[0]
            new_j = zero_j + dir[1]

            if (0 <= new_i < self.numRows) and (0 <= new_j < self.numCols): # New position inside bounds
                newBoard = [row[:] for row in self.board] # Makes a copy

                newBoard[zero_i][zero_j] = self.board[new_i][new_j] # Swap
                newBoard[new_i][new_j] = 0

                childState = State(newBoard, self, dir[2]) # board, parent, direction
                children.append(childState)

        return children


class Puzzle:
    def __init__(self, initialState, goalState):
        self.initialState = initialState
        self.goalState = goalState    # Although it initially has parent None and dir None, we set this later when we find it by searching

        self.visitedStates = [] # List of visited states

    def heuristic(self, state):
        return state - self.goalState
    
    def isGoalState(self, state):
        return state == self.goalState
    
    def isVisited(self, state):
        for visitedState in self.visitedStates:
            if state == visitedState: # Equality overload
                return True
        return False
        

    def solve(self): # Returns the final state. Follow parent to get path
        queue = PriorityQueue()
        queue.put((0, self.initialState))  # (priority, state)

        while not queue.empty():
            priority, state = queue.get()
            self.visitedStates.append(state) # Mark as visited

            if (self.isGoalState(state)):
                return state
            
            children = state.getChildrenStates() # Puts parent and direction as well
            for child in children:
                if self.isVisited(child):
                    continue

                priority = self.heuristic(child)
                queue.put((priority, child))
                
        return None


if __name__ == "__main__":
    initialState = State([[0, 1, 2], 
                          [3, 4, 5], 
                          [6, 7, 8]], None, None)
    goalState = State([[1, 2, 5], 
                       [3, 0, 8], 
                       [6, 4, 7]], None, None)
    
    
    puzzle = Puzzle(initialState, goalState)
    f = puzzle.solve()

    boards = []
    moves = []
    while f is not None:
        boards.append(f.board)
        moves.append(f.move)
        f = f.parent
    
    boards.reverse()
    moves.reverse()
    print(moves)
    print(boards)