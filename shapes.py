data = []
with open('data_small.txt', "r") as f:
    line = f.readline()
    while line:
        line = list(line)
        if line[-1] == '\n':
            line.pop()
        data.append(line)
        line = f.readline()

print(len(data),  len(data[0]))
from collections import deque

print(data)
def shapes(data):
    total = 0
    visited = set()
    rows, cols = len(data), len(data[0])

    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    new_r, new_c = row + dr, col + dc #calculating neighbours' indices
                    if ((dr, dc) not in ((-1, -1), (1, 1), (1, -1), (-1, 1))) and 0 <= new_r < rows and 0 <= new_c < cols and data[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "1" and (r, c) not in visited:
                print((r, c))
                total += 1
                bfs(r, c)
            

    return total

print(shapes(data))
