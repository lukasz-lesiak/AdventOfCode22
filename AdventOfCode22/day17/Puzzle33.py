from __future__ import print_function
import time

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

    current_rock_crd = rock_coordinates(rock, x, y)

    if jet == '>':
        # print(f'jet: {jet} = +1')
        predict_side_rock_crd=rock_coordinates(rock, x+1, y)
        if board.isdisjoint(predict_side_rock_crd) and not is_wall_collision(predict_side_rock_crd):
            x +=1
            current_rock_crd = predict_side_rock_crd
            # print('moved right')
        # else:
        #     print('no movement')
    else:
        # print(f'jet: {jet} = -1')
        predict_side_rock_crd=rock_coordinates(rock, x-1, y)
        if board.isdisjoint(predict_side_rock_crd) and not is_wall_collision(predict_side_rock_crd):
            x -=1
            current_rock_crd = predict_side_rock_crd
            # print('moved left')
        # else:
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
    return board

if __name__ == '__main__':
    start_time = time.time()
    rocks_order = load_rock_pattern('rock_pattern.in')
    # print(*rocks_order, sep='\n')
    jet_order = load_jet_pattern('test_jet_pattern.in')
    # jet_order = load_jet_pattern('jet_pattern.in')
    # print(*jet_order, sep='\n')
    # print(len(jet_order))
    # rock_count = 1000000000000
    rock_count = 2022
    rock_index = 0
    # i = 1
    jet_index = 0
    board = {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)}
    board_top_point = 0
    while rock_index < rock_count:
        if rock_index%1000 ==0:
            print("rock: %s --- %s seconds ---" % (rock_index, (time.time() - start_time)))

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
                    if int(crd[1]) > board_top_point:
                        board_top_point = crd[1]
                board = board.union(rock_crd)
                if rock_index%500 ==0:
                    board = trim_board(board)
        rock_index += 1

    # print(*board, sep='\n')
    print(f'board top point: {board_top_point}')

    # test = {(0,0)}
    # test2 = {(0,1)}
    # print(board.isdisjoint(test))
    # print(board.isdisjoint(test2))
