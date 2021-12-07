
BOARD_SIZE_LINES = 5

def load(filename):
    with open(filename) as f_obj:
        draw_list_str = f_obj.readline()
        boardlist = []
        current_board = []
        for line in f_obj:
            if len(line) > 1:
                current_board.append(line.strip().split(" "))
            if len(current_board) == BOARD_SIZE_LINES:
                boardlist.append(current_board)
                current_board = []

    draw_list = eval(f"[{draw_list_str}]")
    return draw_list, boardlist

def solve(draw_list, boards):
    pass
