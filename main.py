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


    print("The value of the best Move is :", bestVal)
    print()
    return bestMove


# Driver code
board = [
    ['o', 'o', '_', 'x'],
    ['_', 'o', 'x', '_'],
    ['x', 'x', 'x', '_'],
    ['o', 'o', 'o', 'x']
]

bestMove = findBestMove(board)

print("The Optimal Move is :")
print("ROW:", bestMove[0], " COL:", bestMove[1])