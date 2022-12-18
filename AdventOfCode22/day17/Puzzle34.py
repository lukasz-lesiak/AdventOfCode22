from __future__ import print_function
from tqdm import tqdm

def load_rock_pattern(path):
    rocks_patterns = []
    with open(path) as file:
        rocks = file.read().split("\n\n")
        for rock in rocks:
            rock_pattern = []
            rock_lines = rock.split("\n")
            for i in reversed(range(len(rock_lines))):
                rock_pattern.append([*rock_lines[i]])
            rocks_patterns.append(rock_pattern)
        return rocks_patterns


def load_jet_pattern(path):
    with open(path) as file:
        return [*file.read()]

def is_wall_collision(crds):
    for crd in crds:
        if crd[0]>6 or crd[0]<0:
            return True
    return False


def rock_moves(rock,jet, x, y, board):
    # print(f'rock: {rock}, x: {x}, y: {y}')


    if jet == '>':
        # print(f'jet: {jet} = +1')
        predict_side_rock_crd=rock_coordinates(rock, x+1, y)
        if not is_wall_collision(predict_side_rock_crd) and board.isdisjoint(predict_side_rock_crd):
            x +=1
            current_rock_crd = predict_side_rock_crd
            # print('moved right')
        else:
            current_rock_crd = rock_coordinates(rock, x, y)
        #     print('no movement')
    else:
        # print(f'jet: {jet} = -1')
        predict_side_rock_crd=rock_coordinates(rock, x-1, y)
        if not is_wall_collision(predict_side_rock_crd) and board.isdisjoint(predict_side_rock_crd):
            x -=1
            current_rock_crd = predict_side_rock_crd
            # print('moved left')
        else:
            current_rock_crd = rock_coordinates(rock, x, y)
        #     print('no movement')


    # check if move down possible
    # YES calculate crd with -1 to y
    # NO return
    predict_bottom_rock_crd = rock_coordinates(rock, x, y - 1)

    if board.isdisjoint(predict_bottom_rock_crd):
        return True, predict_bottom_rock_crd, x, y - 1
    else:
        return False, current_rock_crd, x, y


def rock_coordinates(rock, left_wall_distance, bottom_distance):
    crd = set()
    # print(f'left distance: {left_wall_distance}; board top point: {bottom_distance};')
    # print(rock)
    rock_y = bottom_distance + 1

    for rock_row in rock:
        # print(rock_row)
        rock_x = left_wall_distance + 1
        for rock_cell in rock_row:
            if rock_cell == '#':
                crd.add((rock_x, rock_y))
            rock_x += 1
        rock_y += 1
    # print(f'crd: {crd}')
    return crd

def trim_board(board):
    new_board = set()
    board_dict = {}
    board_dict[0] = list()
    board_dict[1] = list()
    board_dict[2] = list()
    board_dict[3] = list()
    board_dict[4] = list()
    board_dict[5] = list()
    board_dict[6] = list()
    for crd in board:
        board_dict[crd[0]].append(crd)

    number_of_highest_points = 10

    for x_l in board_dict.values():
        x_l.sort(reverse=True,key=sortFunc)
        new_board = new_board.union(x_l[0:number_of_highest_points])

    return new_board

def trim_board2(board, max_y):
    new_board = set()
    modulo_board = set()
    top_y_rows = 80
    for crd in board:
        if crd[1]+top_y_rows>max_y:
            new_board.add(crd)
            modulo_board.add((crd[0],crd[1]%top_y_rows))
    return new_board,modulo_board


def sortFunc(point):
    return point[1]


if __name__ == '__main__':
    rocks_order = load_rock_pattern('rock_pattern.in')
    # print(*rocks_order, sep='\n')
    # jet_order = load_jet_pattern('test_jet_pattern.in')
    jet_order = load_jet_pattern('jet_pattern.in')
    # print(*jet_order, sep='\n')
    # print(len(jet_order))
    # rock_count = 1000000000000
    # rock_count = 10000000 # 15142861
    # rock_count = 1000000 #1512780
    # rock_count = 100000 # 151434
    # rock_count = 10000 # 151434
    # rock_count = 2022
    rock_count = 1875
    rock_index = 0
    # i = 1
    jet_index = 0
    board = {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)}
    board_top_point = 0

    cycles=[]
    for i in range(len(rocks_order)):
        jets = []
        for j in range(len(jet_order)):
            jets.append([({12,13},14,15)])
        cycles.append(jets)
    print(f"len(cycles): {len(cycles)}")
    print(f"len(cycles[0]): {len(cycles[0])}")
    print(f"len(cycles[0][0]): {len(cycles[0][0])}")
    print(f"len(cycles[0][0][0]): {len(cycles[0][0][0])}")
    print(f"cycles[0][0][0][0]): {cycles[0][0][0][0]}")
    print(f"cycles[0][0][0][1]: {cycles[0][0][0][1]}")


    for rock_index in tqdm(range(rock_count)):
        falling_rock = rocks_order[rock_index % len(rocks_order)]
        # print(f'{rock_index} rock: {falling_rock}')
        x = 1
        y = board_top_point + 3
        # rock_crd = rock_coordinates(falling_rock, x, y)
        rock_moving = True

        while rock_moving:
            # print(f'Rock {rock_index} tries to move')
            jet = jet_order[jet_index % len(jet_order)]
            rock_moving, rock_crd, x, y = rock_moves(falling_rock,jet, x, y, board)
            jet_index+=1
            if not rock_moving:
                # print(f'Rock {rock_index} stoped')
                for crd in rock_crd:
                    if crd[1] > board_top_point:
                        board_top_point = crd[1]
                board = board.union(rock_crd)
                # if rock_index%2 ==0:
                #     board = trim_board(board)
                board,state = trim_board2(board, board_top_point)
                rock_no = rock_index % len(rocks_order)
                jet_no = jet_index % len(jet_order)
                cycles[rock_no][jet_no].append((state,rock_index,board_top_point))
                for k in cycles[rock_no][jet_no]:
                    if k[0] == state:
                        print(f'{rock_no}:{jet_no} SAME STATE: {k[1]}; {rock_index}; {k[2]};')
        rock_index += 1

    print(f'board top point: {board_top_point}')
    print(f"len(cycles[0][0]): {len(cycles[0][0])}")

# 0:1626 SAME STATE: 285; 2020; 456;
# 0:1626 SAME STATE: 2020; 2020; 3176;
# 285 = 456 (455?)
# 1735 = 2720 CYCLE
# 285 +1735 = 2020 (still missing 2)
# 287 = 459
# f(285) + f(1735) + f(287) - f(285) = 3179

# 456 + (1*2720) + =

# f(285) = 456
# (1000000000000 - 285)%1735 = 1590
# 285+1590=1875
# f(1875) = 2929
# 2929-456 = 2473
# (1000000000000 - 1875) / 1735 = 576368875
# 456 + (576368875*2720) + 2473 = 1567723342929