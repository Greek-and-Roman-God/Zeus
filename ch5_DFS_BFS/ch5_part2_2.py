# 이것이 코딩테스트다
# 챕터5 DFS / BFS

# 실전문제 5-2 미로탈출
from collections import deque

global graph
global n, m
global dx, dy

def maze_run():
  global graph
  global n, m
  global dx, dy

  n, m = map(int, input().split()) #그래프의 세로, 가로
  graph = []

  for _ in range(n):
    tmp_arr = list(map(int,input()))
    if len(tmp_arr) != m:
      print("다시 입력하세요")
      break
    graph.append(tmp_arr) # 그래프 작성

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  print(dfs(0,0))


def dfs(x, y):
  global graph
  global n, m
  global dx, dy

  que = deque()
  que.append((x, y))

  while que:
    x, y = que.popleft()

    for i in range(4): #4가지 방향으로 검사
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= m or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0: 
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        que.append((nx, ny))
  
  return graph[n-1][m-1]
