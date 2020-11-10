# 이것이 코딩테스트다
# 챕터5 DFS / BFS

# 실전문제 5-1 음료수 얼려먹기
global graph
global n, m

def make_ice():
  global graph 
  global n, m

  m, n = map(int, input().split()) #가로 세로

  graph = []
  for i in range(n):
    tmp_arr = list(map(int, input()))
    if len(tmp_arr) != m :
      print("다시 입력하세요")
      break
    graph.append(tmp_arr)

  
  result = 0 #결과값 넣기위해 선언
  for i in range(n):
    for j in range(m):
      if dfs(i,j) : 
        result += 1
  print(result);
  

def dfs(x,y):
  global graph
  global n, m

  #칸 넘어가면 바로 종료하기
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  
  if graph[x][y] == 0 : #아직 방문하지 않았다면
    graph[x][y] = 1 #방문 도장 찍고

    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1) #현위치를 기준으로 사방을 다 dfs 재귀 돌림
    return True
  return False