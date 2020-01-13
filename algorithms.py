
import sys
from datetime import datetime


def BFS(board, parent_pos, start_time):

    print(sys.getsizeof(parent_pos))

    new_ppos = []
    for p in range(len(parent_pos)):
        null, child_count = divmod(p, 8)
        for i in range(child_count, 8):
            new_pos = parent_pos[p].copy()
            new_pos[i] += 1
            new_ppos.append(new_pos)

            # print(new_pos)

            if new_pos[i] == 8:
                new_pos[i] = 0
            board.set_pos(new_pos)
            if board.is_done():
                return [new_pos, sys.getsizeof(parent_pos), datetime.now() - start_time]
    del parent_pos
    return [new_ppos]
