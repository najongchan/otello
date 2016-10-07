# hongik univ.
# AI work2
# B111066
# Na Jong Chan
import gamePlay
import copy

def calculate_heuristic(board, color):
    player_pieces = 0
    opponent_pieces = 0
    for i in range(8):
        for j in range(8):
            if board[i][j]==color:
                player_pieces += 1
            elif board[i][j]==gamePlay.opponent(color):
                opponent_pieces += 1

    edge_pos = [(0,0), (0,7), (7,0), (7,7)]
    for edge in edge_pos:
        if board[edge[0]][edge[1]] == color:
            player_pieces += 999
        elif board[edge[0]][edge[1]] == gamePlay.opponent(color):
            opponent_pieces += 999

    side_pos = [0,7]
    for side in side_pos:
        for k in range(8):
            if board[side][k] == color:
                player_pieces += 5
            elif board[side][k] == gamePlay.opponent(color):
                opponent_pieces += 5
            elif board[k][side] == color:
                player_pieces += 5
            elif board[k][side] == gamePlay.opponent(color):
                opponent_pieces += 5

    weak_pos= [(1,1),(1,0),(0,1),(6,6),(0,6),(6,0),(1,6),(6,7),(7,6),(6,1),(7,1),(1,7)]
    for weak in weak_pos:
        if board[weak[0]][weak[1]] == color:
            opponent_pieces += 5
        elif board[weak[0]][weak[1]] == gamePlay.opponent(color):
            player_pieces += 5

    count_eval = player_pieces - opponent_pieces
    return  count_eval

def alphabeta(board, alpha, beta, depth, color, player):
    can_moves = []
    for i in range(8):
        for j in range(8):
            if gamePlay.valid(board, player, (i,j)):
                can_moves.append((i,j))

    if depth == 0 or len(can_moves) == 0:
        return calculate_heuristic(board, color)

    if(player == color):#Maximizing
        v = -999999
        for can_move in can_moves:
            temp_board = copy.deepcopy(board)
            gamePlay.doMove(temp_board, player, can_move)
            v = max(v, alphabeta(temp_board, alpha, beta, depth-1, color, gamePlay.opponent(player)))
            alpha = max(alpha, v)
            if(alpha >= beta):
                break

        return v
    else:#Minimizing
        v = 999999
        for can_move in can_moves:
            temp_board = copy.deepcopy(board)
            gamePlay.doMove(temp_board, player, can_move)
            v = min(v, alphabeta(temp_board, alpha, beta, depth-1, color, gamePlay.opponent(player)))
            beta = min(beta, v)
            if (alpha >= beta):
                break

        return v

def nextMove(board, color, time):
    limit_depth = 4
    max_value = -999999
    min_value = 999999
    valid_count = 0
    for i in range(8):
        for j in range(8):
            if gamePlay.valid(board ,color, (i,j)):
                valid_count += 1
                temp_board = copy.deepcopy(board)
                gamePlay.doMove(temp_board, color, (i,j))
                v = alphabeta(temp_board, max_value, min_value, limit_depth-1, color, gamePlay.opponent(color))
                if v >= max_value:
                    next_move = (i, j)
                    max_value = v

    if valid_count == 0:
        return "pass"

    #gamePlay.printBoard(board)
    return next_move

