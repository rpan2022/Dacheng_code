"""Homework: Game of Life."""

import copy

## some code and helper functions
DEATH_STATE = 0
LIVE_STATE = 1

def get_cell_state(board: list, i: int, j:int) -> int:
    return board[i][j]

def get_surround_cell_states(board, center_i, center_j) -> list:
    result = []
    
    """
    (center_i-1, center_j-1)|(center_i-1, center_j) | (center_i-1, center_j+1)
    --------------------------------------------------------------------
    (center_i, center_j-1)  |(center_i, center_j)   | (center_i, center_j+1)
    --------------------------------------------------------------------
    (center_i+1, center_j-1)|(center_i+1, center_j) | (center_i+1, center_j+1)
    """
    for row in range(center_i-1, center_i+2):
        for col in range(center_j-1, center_j+2):

            if row == center_i and col == center_j: # avoid the center
                continue

            if row < 0:
                result.append(DEATH_STATE)
            elif row < len(board):
                if col < 0:
                    result.append(DEATH_STATE)
                elif col < len(board[0]):
                    result.append(get_cell_state(board, row, col))
                else:
                    result.append(DEATH_STATE)
            else:
                result.append(DEATH_STATE)

    return result

def set_cell_state(board, i, j, state) -> None:
    board[i][j] = state

def update_current_cell_state(board, old_board, surround_cell_states, i, j) -> None:
    # case 1: if the cell is live and the number of sourround cells equal 2 or 3, then the cell is live
    # case 2: ..., and the number of surround cells small than 2, then the cell is dead
    # case 3: ..., and the number of surround cells larger than 3, then the cell is dead
    # -------------------
    # case 4: cell is dead, and the number of surround cells is exactly equal to 3, then the cell is live
    #

    current_cell = get_cell_state(old_board, i, j)
    live_surround_cells_number = sum(surround_cell_states)

    if current_cell == LIVE_STATE:
        # case 1
        if live_surround_cells_number == 2 or live_surround_cells_number == 3:
            pass
        # case 2 and case 3
        else:
            set_cell_state(board, i, j, DEATH_STATE)
    else:
        if live_surround_cells_number == 3:
            set_cell_state(board, i, j, LIVE_STATE)

def update_board(board: list):
    """Generate the next generation of the board.

    This function performs a single update step according to the Game of Life
    rules [1].

    Args:
        board (list): The current state of the Game of Life board. The data
            structure is a list of lists of zeroes and ones. Each zero or one
            value represents a dead or alive cell respectively. For the sake
            of consistency the elements of the outer list are defined to be
            the rows of the board, indices count from left to right and up to
            down. The the board shall not wrap around. The out of bounds
            neighbors of edge pixels are assumed to be zero.

    Returns:
        The next generation of the board in the same format as the `board`
        input parameter of the function. The output boards shall have the same
        dimensions as the input board.

    Notes: Edit this function to implement the Game of Life update step. Use
        only builtin language features or functions from the Python standard
        library, do not import third-party modules for the logic.

        Hints:

        (1) For debugging purposes it might be very helpful to write a simple
        visualization function that uses the `print` function to properly show
        a board on the CLI to ease visual inspection.

        (2) The `try_update_board` function can be adapted to perform and
        visualize updates in a loop and either use `time.sleep` or `input` to
        slow animation down or make it interactive.

        (3) The Wikipedia page [1] displays some examples that can be used as
        test data for the function.

    """
    rows = len(board)
    cols = len(board[0])
    old_board = copy.deepcopy(board)
    for row in range(0, rows):
        for col in range(0, cols):
            surround_cell_states = get_surround_cell_states(old_board, row, col)
            update_current_cell_state(board, old_board, surround_cell_states ,row, col)

def try_update_board() -> None:
    """Run two update steps on the board and print the results."""
    board = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    print(f"input matrix is {board}")

    update_board(board)
    print(f'After one generation it becomes {board!r}.')

    update_board(board)
    print(f'After two generations it becomes {board!r}.')


if __name__ == '__main__':
    try_update_board()
