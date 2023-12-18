player, opponent = 'x', 'o'
INFINITY = float('inf')
NEG_INFINITY = float('-inf')


def isMovesLeft(board):
    for i in range(4):
        for j in range(4):
            if (board[i][j] == '_'):
                return True
    return False


def evaluate(b):
    l_shapes = [((0, 0), (1, 0), (1, 1)), ((0, 1), (1, 1), (1, 2)),
                ((0, 2), (1, 2), (1, 3)), ((1, 0), (2, 0), (2, 1)),
                ((1, 1), (2, 1), (2, 2)), ((1, 2), (2, 2), (2, 3)),
                ((2, 0), (3, 0), (3, 1)), ((2, 1), (3, 1), (3, 2)),
                ((2, 2), (3, 2), (3, 3))]

    for shape in l_shapes:
        cells = [b[row][col] for row, col in shape]
        if all(cell == player for cell in cells):
            return 10
        if all(cell == opponent for cell in cells):
            return -10

    return 0



def minimax(board, depth, isMax, alpha,beta):
    score = evaluate(board)

    if score == 10:
        return score

    if score == -10:
        return score

    if not isMovesLeft(board):
        return 0

    if isMax: #TURNO MAXIMIZADOR
        max_eval = NEG_INFINITY
        for i in range(4):
            for j in range(4):
                if board[i][j] == '_':
                    board[i][j] = player
                    eval = minimax(board, depth + 1, not isMax, alpha,beta)
                    max_eval = max(max_eval, eval)
                    board[i][j] = '_'

                    # poda alfa beta
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break

        return max_eval

    else: #TURNO MINIMIZADOR
        min_eval = INFINITY
        for i in range(4):
            for j in range(4):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    eval = minimax(board, depth + 1, not isMax, alpha,beta )
                    min_eval = min(min_eval, eval)
                    board[i][j] = '_'

                    # poda alfa beta
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break

        return min_eval

def findBestMove(board):
    bestVal = NEG_INFINITY
    bestMove = (-1, -1)

    for i in range(4):
        for j in range(4):
            if (board[i][j] == '_'):
                board[i][j] = player
                moveVal = minimax(board, 0, False, NEG_INFINITY, INFINITY)
                board[i][j] = '_'

                #Si el valor del nuevo movimiento analizado es mayor, se actualiza
                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove



class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        tablero = [["_" for _ in range(4)] for _ in range(4)]
        return tablero

    def print_board(self):
        for fila in self.board:
            print(fila)

    def add_player(self,  row, column, player):
        if self.board[row][column] == "_":
            self.board[row][column] = player
            return True
        else:
            print("Celda ocupada. Intente de nuevo.")
            return False

    def turn_player(self, player):
        while True:
            row = int(input("Ingrese la fila (0-3)"))
            column = int(input("Ingrese la columna (0-3)"))
            if row < 0 or row > 3 or column < 0 or column > 3:
                print("Coordenadas inválidas. Intente de nuevo.")
                continue

            if self.add_player(row, column, player):
                break

    def verify_winner(self, player):
        for row in range(3):
            for column in range(3):
                if (self.board[row][column] == player and
                     self.board[row + 1][column] == player and
                     self.board[row + 1][column + 1] == player):
                         return True

        return False

    def play_optimal_move(self, player):
        if player == 'x':
            best_move = findBestMove(self.board)
            self.add_player(best_move[0], best_move[1], player)
            return best_move


game = Board()

b = game.create_board()
game.print_board()
while True:
    game.turn_player('o')
    game.print_board()


    if game.verify_winner('o'):
        print("¡El jugador 'o' ha ganado!")
        break

    print("Turno del pc (x)...")
    best_move = game.play_optimal_move('x')
    game.print_board()


    if game.verify_winner('x'):
        print("¡La IA ('x') ha ganado!")
        break




