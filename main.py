
from datetime import datetime
from eight_queens import Board
from algorithms import BFS


board = Board([0] * 8)
start_time = datetime.now()
pos = [[0] * 8]
while True:
    res = BFS(board, pos, start_time)
    if len(res) == 1:
        pos = res[0]
    else:
        print(res)
        break
