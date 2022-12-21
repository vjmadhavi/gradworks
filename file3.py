import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
from datetime import datetime
import time
plt.ion()
#board_history = []
def conway_assignment_two(board):
    N = (board[0:-2, 0:-2] + board[0:-2, 1:-1] + board[0:-2, 2:] +
         board[1:-1, 0:-2] + board[1:-1, 2:] +
         board[2:, 0:-2] + board[2:, 1:-1] + board[2:, 2:])
    birth = (N == 3) & (board[1:-1, 1:-1] == 0)
    survive = ((N == 2) | (N == 3)) & (board[1:-1, 1:-1] == 1)
    board[...] = 0
    board[1:-1, 1:-1][birth | survive] = 1
    #board_history.append(board)
    return board

def grid(n1,n2, n3):
    if n1 == 2:
        a = np.zeros((n2, n2), dtype=bool)
        r = np.random.random((10, 20))

        a[10:20, 10:30] = (r > 0.75)
        board = a.astype(int)
        scatter_plot(board, n2, n3)

    if n1 == 1:
        board = np.zeros((n2, n2), dtype=bool)
        board = board.astype(int)
        for j in range(3, n2-2, 5):
            for i in range(2, n2-1, 5):
                if i+4 <= n2:
                    board[j][i] = 1
                    board[j][i+1] = 1
                    board[j][i+2] = 1

        scatter_plot(board,n2, n3)

    if n1 == 3:
        board = np.zeros((n2, n2), dtype=bool)
        board = board.astype(int)
        coordinates = [(10, 5), (11, 5), (10, 6), (11, 6), (10, 15), (11, 15), (12, 15), (9, 16), (13, 16), (8, 17),
                       (8, 18),
                       (14, 17), (14, 18), (11, 19), (9, 20), (13, 20), (10, 21), (11, 21), (12, 21), (11, 22), (8, 25),
                       (9, 25), (10, 25), (8, 26),
                       (9, 26), (10, 26), (11, 27), (7, 27), (6, 29), (7, 29), (11, 29), (12, 29), (8, 39), (9, 39),
                       (8, 40), (9, 40)]

        for g in coordinates:
            board[g[0]][g[1]] = 1

        scatter_plot(board, n2, n3)
    if n1 ==4:
            board = np.zeros((n2,n2),dtype=bool)
            board = board.astype(int)
            # starting the pattern from the centre of the grid
            half = int(n2/2)
            coordinates = [(half-4, half-1), (half-4, half), (half-4, half+1), (half-4, half+2), (half-4, half+3), (half-4, half+4), (half-5, half-1), (half-5, half+5), (half-6, half-1),
                  (half-7, half), (half-7, half+5), (half-8, half+2), (half-8, half+3),
                  (half, half-3), (half, half-2),
                  (half+1, half-4), (half+1, half-3),(half+1, half-1), (half+1, half), (half+1, half+1), (half+1, half+2), (half+1, half+3), (half+1, half+4), (half+1, half+5),
                  (half+2, half-3), (half+2, half-2), (half+2, half-1), (half+2, half), (half+2, half+1), (half+2, half+2), (half+2, half+3), (half+2, half+4),
                  (half+3, half-2), (half+3, half-1), (half+3, half), (half+3, half+1), (half+3, half+2), (half+3, half+3),
                  (half+5, half+2), (half+5, half+3), (half+6,half), (half+6,half+5), (half+7, half-1), (half+8, half-1), (half+8, half+5),
                  (half+9, half-1), (half+9, half), (half+9, half+1), (half+9, half+2), (half+9, half+3), (half+9, half+4)]
            #the above coordinates are for heavy weight spaceship pattern, looks fine for different grid size.
            for g in coordinates:
                board[g[0]][g[1]] = 1
            # function calling scatter plot
            scatter_plot(board, n2, n3)

def scatter_plot(board, n2, n3):
    a, b = np.meshgrid(np.arange(board.shape[1]) + .5, np.arange(board.shape[0]) + .5)

    fig, axes = plt.subplots(1, 1, figsize=(15, 9),
                             tight_layout=True)

    axes.grid(True, color="k")
    axes.xaxis.set_major_locator(mticker.MultipleLocator())
    axes.yaxis.set_major_locator(mticker.MultipleLocator())
    axes.tick_params(size=0, length=0, labelleft=False, labelbottom=False)
    axes.set(xlim=(0, board.shape[1]), ylim=(board.shape[0], 0),
              aspect="equal")

    plt_u = axes.scatter(a[board == 1],
                           b[board ==1], c='b',
                           marker='x')

    plt.show()
    start_datetime = datetime.now() # start time
    print("the start time is ",start_datetime)


    #for calculating living cells
    last = board
    count = 0
    living_cells = np.count_nonzero(board==1)
    for t in range(1, n3):
        new_board = conway_assignment_two(board)
        if (last==new_board).all():
            count +=1
        if count > 2:
            new_board = board
        last = new_board
        living_cells += np.count_nonzero(new_board==1)
        a, b = np.meshgrid(np.arange(new_board.shape[1]) + .5, np.arange(new_board.shape[0]) + .5)
        update_plot(plt_u, a, b, new_board)
        fig.canvas.draw_idle()
        fig.canvas.draw()
        fig.canvas.flush_events()#clears board
        time.sleep(0.00001)
    # end time
    end_datetime = datetime.now()
    print("The end time is ",end_datetime)
    # calculating time difference
    time_diff = (end_datetime - start_datetime)

    print(time_diff)
    # converting seconds into milliseconds
    execution_time = time_diff.total_seconds() * 1000
    # converting milliseconds to seconds
    p=execution_time/1000
    print("Time in seconds", p)
    print("Number of milliseconds:", execution_time)

    print("Total number of living cells during processing", living_cells)
    #x=n3/time_diff
    print("number of frames per second", n3/p)
    plt.waitforbuttonpress()

def update_plot(plt_u, a, b, grid):
    plt_u.set_offsets(np.c_[a[grid > 0], b[grid > 0]])
# grid(n1,n2,n3)
