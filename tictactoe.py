"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    o_count, x_count = 0, 0
    for row in board:
        for space in row:
            if space == X:
                x_count += 1
            elif space == O:
                o_count += 1

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.append((i, j))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    from copy import deepcopy

    if action not in actions(board):
        raise Exception("That space is taken. Please try again.")
    else:
        i, j = action[0], action[1]
        new_board = deepcopy(board)
        new_board[i][j] = player(new_board)

        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if (board[0][0] == board[0][1] == board[0][2]) and (board[0][0] is not EMPTY):
        return board[0][0]
    elif (board[1][0] == board[1][1] == board[1][2]) and (board[1][0] is not EMPTY):
        return board[1][0]
    elif (board[2][0] == board[2][1] == board[2][2]) and (board[2][0] is not EMPTY):
        return board[2][0]
    elif (board[0][0] == board[1][0] == board[2][0]) and (board[0][0] is not EMPTY):
        return board[0][0]
    elif (board[0][1] == board[1][1] == board[2][1]) and (board[0][1] is not EMPTY):
        return board[0][1]
    elif (board[0][2] == board[1][2] == board[2][2]) and (board[0][2] is not EMPTY):
        return board[0][2]
    elif (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not EMPTY):
        return board[0][0]
    elif (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not EMPTY):
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == X or winner(board) == O:
        return True
    for row in board:
        for space in row:
            if space == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    elif board == initial_state():
        return (0, 0)
    elif player(board) == X:
        return max_value(board)[1]
    elif player(board) == O:
        return min_value(board)[1]


def max_value(board):

    value = -math.inf
    if terminal(board):
        return (utility(board), None)
    for action in actions(board):
        best_value = min_value(result(board, action))[0]
        if best_value > value:
            value = best_value
            optimal_action = action
    return (value, optimal_action)


def min_value(board):

    value = math.inf
    if terminal(board):
        return (utility(board), None)
    for action in actions(board):
        best_value = max_value(result(board, action))[0]
        if best_value < value:
            value = best_value
            optimal_action = action
    return (value, optimal_action)
