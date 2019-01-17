ALIVE = 1
DEAD = 0

board = [
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
]

#next_gen_twod_array = [
#    [0, 0, 0, 0, 0, 0],
#    [0, 0, 1, 1, 1, 0],
#    [0, 0, 1, 1, 1, 0],
#    [0, 0, 0, 0, 0, 0],
#]


def find_neighbors(board, x, y):
    # returns count of neighbors that are alive
    # how to find neighbors. including edge cases

    # +/- of every x/y position as long as it doesn't exceed boundaries
    neighbor_identity_matrix = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    neighbors = []
    for x_op, y_op in neighbor_identity_matrix:
        new_pos = (x + x_op, y + y_op)

        # Remove bad neighbors by evaluating < len
        if new_pos[0] < 0 or new_pos[1] < 0:
            continue
        elif (new_pos[1] >= len(board[0])) or (new_pos[0] >= len(board)):
            continue

        neighbors.append(new_pos)
    return neighbors

def alive_neighbors(board, neighbors, x, y):
    cell_status = {}
    for neighbor in neighbors:
        cell_status[neighbor] = board[neighbor[0]][neighbor[1]]
    return cell_status


def should_live(currently_alive, cell_status): #check parameters
    # implementaiton of the rules
    # #   Rules:
    # #     1. Any live cell with fewer than two live neighbors dies.
    # #     2. Any live cell with two or three live neighbors lives on to the next generation.
    # #     3. Any live cell with more than three live neighbours dies.
    # #     4. Any dead cell with exactly three live neighbors becomes a live cell.
    alive_neighbors = sum(cell_status.values())
    if currently_alive:
        if alive_neighbors < 2:
            return False
        elif (alive_neighbors == 2) or (alive_neighbors == 3):
            return True
        else:
            return False
    # Is dead
    if alive_neighbors == 3:
        return True
    return False


def next_board(current_board):
    next_board = []
    for x, row in enumerate(current_board):
        next_row = []
        for y, cell_value in enumerate(row):
            neighbors = find_neighbors(current_board, x, y)
            cell_status = alive_neighbors(current_board, neighbors, x, y)
            lives = should_live(cell_value, cell_status)
            next_row.append(1 if lives else 0)
        next_board.append(next_row)
    return next_board

#print(find_neighbors(board, 0, 5))

board = next_board(board)
for row in board:
    print(row)
