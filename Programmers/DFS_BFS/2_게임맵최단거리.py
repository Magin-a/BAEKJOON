from collections import deque


def solution(maps):
    rows, cols = len(maps), len(maps[0])
    if maps[0][0] == 0:
        return -1

    to_move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 1)])  # (행, 열, 시작 칸부터 센 거리)
    maps[0][0] = 0

    while queue:
        row, col, step = queue.popleft()
        if (row, col) == (rows - 1, cols - 1):
            return step

        for dr, dc in to_move:
            nr, nc = row + dr, col + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if maps[nr][nc] == 0:
                continue

            maps[nr][nc] = 0
            queue.append((nr, nc, step + 1))

    return -1
# #DFS
# def solution(maps):
#     rows, cols = len(maps), len(maps[0])
#     best = float("inf")

#     def dfs(row, col, step):
#         nonlocal best

#         if step >= best:
#             return
#         if (row, col) == (rows - 1, cols - 1):
#             best = step
#             return

#         maps[row][col] = 0
#         for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#             nr, nc = row + dr, col + dc
#             if 0 <= nr < rows and 0 <= nc < cols and maps[nr][nc] == 1:
#                 dfs(nr, nc, step + 1)
#         maps[row][col] = 1  # 다른 경로에서도 이 칸을 쓸 수 있게 복구

#     if maps[0][0] == 1:
#         dfs(0, 0, 1)
#     return -1 if best == float("inf") else best


if __name__ == "__main__":
    # 테스트 케이스 1
    print("테스트 케이스 1")
    maps = [[1,0,1,1,1],
            [1,0,1,0,1],
            [1,0,1,1,1],
            [1,1,1,0,1],
            [0,0,0,0,1]]
    result = solution(maps)
    print(result)

    # 테스트 케이스 2
    print("테스트 케이스 2")
    maps = [[1,0,1,1,1],
            [1,0,1,0,1],
            [1,0,1,1,1],
            [1,1,1,0,0],
            [0,0,0,0,1]]
    result = solution(maps)
    print(result)
