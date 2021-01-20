# 백준 백트래킹 단계
# https://www.acmicpc.net/step/34


# 15649 번 : N과 M (1)
import itertools
def backtracking_15649():
  n, m = map(int, input().split())

  prod_nums = list(itertools.permutations(range(1, n+1), m))
  for prod in prod_nums:
    print(" ".join(str(p) for p in prod))



# 15650 번 : N과 M (2)
import itertools
def backtracking_15650():
  n, m = map(int, input().split())

  tmp_list = list(itertools.combinations(range(1, n+1), m ))
  for tmp in tmp_list:
    for t in tmp:
      print(t, end=' ')
    print()


# 14889 번 : 스타트와 링크
import itertools
def backtracking_14889():
  n = int(input())
  table = []
  for _ in range(n):
    table.append(list(map(int, input().split())))

  people = [i for i in range(n)]

  stats = []

  #팀을 나누는 과정
  tmp_team = list(itertools.combinations(range(n), n//2))
  for team in tmp_team:
    start = team
    link = [p for p in people if p not in start]

    hap_start = 0
    hap_link = 0
    for i in start:
      for j in start:
        hap_start += table[i][j]

    for i in link:
      for j in link:
        hap_link += table[i][j]
    
    if abs(hap_start - hap_link) == 0:
      print(0)
      return
    else:
      stats.append(abs(hap_start - hap_link))
    
  print(min(stats))


# 9663 번 : N-Queen
def backtracking_9663():
  global n
  global answer

  n = int(input())
  col = [0] * (n+1)
  answer = 0
  
  #엔퀸 판별하는 함수
  def n_queens(i, col):
    global answer 
    global n

    if promising(i,col): #true가 리턴되면 if를 타게 됨
      if i == n: # i가 끝까지 확인했다는 말이므로 
        answer += 1 # 정답의 갯수를 +1
      else:
        for j in range(1, n+1):
          col[i+1] = j
          n_queens(i+1, col)

  def promising(i,col):
    k = 1
    while k < i :
      #한 줄로 나란히 놓이거나 / 대각선으로 나란히 놓이는 경우
      if col[i] == col[k] or abs(col[i]-col[k]) == (i-k):
        return False #false를 리턴
      k += 1 #k를 늘리면서 계속 확인
    return True #끝까지 돌았을 경우 겹치는게 없다는 뜻이므로 true
  
  n_queens(0, col)
  print(answer)



  # 15651 번 : N과 M (3)
import itertools
def backtracking_15651():
  n, m = map(int, input().split())

  num_list = list(itertools.product(range(1, n+1), repeat = m))
  for nums in num_list:
    tmp_answer = ''
    for n in nums:
      tmp_answer += str(n) + ' '
    print(tmp_answer)



# 15652 번 : N과 M (4) -메모리초과
import itertools
import sys
def backtracking_15652_1():
  n, m = map(int, input().split())

  num_list = list(itertools.product(range(1,n+1), repeat = m))
  
  for num in num_list:
    #앞, 뒤 를 비교해서 모두 앞보다 뒤에가 더 크다면
    if all(num[i] <= num[i+1] for i in range(len(num)-1)):  
      tmp_answer = ''
      for n in num:
        tmp_answer += str(n) + ' '
      sys.stdout.write(tmp_answer + '\n')
    else:
      continue


# 15652 번 : N과 M (4)-2
import itertools
def backtracking_15652():
  n, m = map(int, input().split())

  num_list = list(itertools.combinations_with_replacement(range(1,n+1), m))
  
  for num in num_list:
    tmp_answer = ''
    for n in num:
      tmp_answer += str(n) + ' '
    print(tmp_answer)


# 14888 번 : 연산자 끼워넣기
def backtracking_14888():
  n = int(input())
  num_list = list(map(int, input().split()))
  plus, sub, mul, div = map(int, input().split())

  global max_value, min_value

  max_value = -10**9
  min_value = 10**9

  def calculate(index, p, s, m, d, total):
    global max_value, min_value

    if index == n:
      max_value = max(max_value, total)
      min_value = min(min_value, total)
      return

    if p < plus:
      calculate(index+1, p+1, s, m, d, total+num_list[index])
    if s < sub:
      calculate(index+1, p, s+1, m, d, total-num_list[index])
    if m < mul:
      calculate(index+1, p, s, m+1, d, total*num_list[index])
    if d < div:
      calculate(index+1, p, s, m, d+1, int(total/num_list[index]))

  calculate(1, 0,0,0,0, num_list[0])
  print(max_value, min_value)



# 2580 번 : 스도쿠
import sys
def backtracking_2580():
  sudoku = []
  for _ in range(9):
    row = list(map(int, input().split()))
    sudoku.append(row)

  #가로로 확인
  def chk_garo(x, val):
    if val in sudoku[x]: #그 가로줄 안에 있다면
      return False
    return True #아니면 트루 리턴

  #세로로 확인
  def chk_sero(y, val):
    for i in range(9):
      if val == sudoku[i][y]: #그 세로줄에 같은 값이 있다면
        return False    
    return True #아니면 트루 리턴
  
  #3*3 쪼개서 확인
  def chk_small(x,y,val):
    nx = x//3 * 3 #0, 3, 6
    ny = y//3 * 3 #0, 3, 6
    for i in range(3):
      for j in range(3):
        if val == sudoku[nx+i][ny+j]: #012/345/678로 잘라서 확인가능
          return False #같은게 있으면 False
    return True
  
  def make_sudoku(index):
    if index == len(zeros):
      for row in sudoku:
        for r in row:
          print(r, end = ' ')
        print()
      sys.exit(0) #하나만 출력하면 되므로 종료
    else:
      for i in range(1,10):
        nx = zeros[index][0]
        ny = zeros[index][1]

        if chk_garo(nx, i) and chk_sero(ny, i) and chk_small(nx,ny,i):
          sudoku[nx][ny] = i
          make_sudoku(index+1)
          sudoku[nx][ny] = 0

  zeros = [ (i,j) for i in range(9) for j in range(9) if sudoku[i][j]==0 ]
  make_sudoku(0)


