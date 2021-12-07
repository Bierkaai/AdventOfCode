from bingoboard import BingoBoard

BOARD_SIZE_LINES = 5

def parse_line(l):
    return [int(x) for x in l.split()]

def load(filename):
    with open(filename) as f_obj:
        draw_list_str = f_obj.readline()
        boardlist = []
        current_board = []
        for line in f_obj:
            if len(line) > 2:
                current_board.append(parse_line(line))
            if len(current_board) == BOARD_SIZE_LINES:
                boardlist.append(current_board)
                current_board = []
    draw_list = eval(f"[{draw_list_str}]")
    return draw_list, boardlist

def solve(draw_list, boards):
    bingoboards = [BingoBoard(b) for b in boards]
    we_have_a_winner = False
    winsum = 0
    while len(draw_list) > 0 and not we_have_a_winner:
        n = draw_list.pop(0)
        for b in bingoboards:
            b.mark(n)
            if b.hasWon:
                we_have_a_winner = True
                win_number = b.sum * n
    return win_number

def find_last_winner(draw_list, boards):
    bingoboards = [BingoBoard(b) for b in boards]
    last_winner = None
    while len(draw_list) > 0 and len(bingoboards) > 0:
        n = draw_list.pop(0)
        print(f"{n} was drawn {len(draw_list)} numbers left")
        for b in bingoboards:
            b.mark(n)
        for b in bingoboards:
            if b.hasWon:
                last_winner = b
                bingoboards.remove(b)
                print(f"This board has won, {len(bingoboards)} boards left:\n{b}")

    return last_winner.sum * n


if __name__ == "__main__":
    draw_list, boards = load("./input/04.txt")
    #print(solve(draw_list, boards))
    print(find_last_winner(draw_list, boards))
