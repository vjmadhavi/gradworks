import argparse as ap
from file3 import *
import numpy as np


if __name__ == '__main__':
    q = ap.ArgumentParser()
    q.add_argument("option", help="enters an option",type=int)
    q.add_argument("dim", help="dimension",type=int)
    q.add_argument("sml", help="simulations",type=int)
    args = q.parse_args()
    n1=int(args.option)
    print(n1)
    n2=int(args.dim)
    print(n2)
    n3=int(args.sml)
    print(n3)
    while True:
        if n1 == 1:
            print(" You selected Blinker")
            break
        elif n1 == 2:
            print("You selected Random")
            break
        elif n1 == 3:
            print("You selected 'Glider Gun'")
            break
        elif n1 == 4:
            print("You selected '4'")
            break
        else:
            print("Enter a valid option")
            continue
    while True:
        if n3<0:
            print("enter a valid dimension:")
            continue
        else:
            print("the size of grid ", n3)
            break
    while True:
        if n2<0:
            print("enter valid simulations")
            continue
        else:
            print("simulations", n2)
            break
grid(3,100,50)

# def conwoy_assignment_three():
#     board = np.zeros((n2, n2), dtype=bool)
#     board_history=[]
#     for i in range(1,n3):
#         board_history.append(conway_assignment_two(board))
#     print(board_history)
#         #print(conway_assignment_two())
#
#
# conwoy_assignment_three()

def conway_assignment_three(board, n2, n3):
    board.conway_assignment_three()
    count = 0
    last = board
    living_cells = np.count_nonzero(board == 1)
    for t in range(1, n3):
        altered_board = conway_assignment_two(board)
        if (last == new_board).all():
            count += 1
        if count > 2:
            altered_board = board
        last = altered_board
        living_cells += np.count_nonzero(altered_board == 1)

    return altered_board
conway_assignment_three()