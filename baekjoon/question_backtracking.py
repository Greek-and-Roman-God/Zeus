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
    # print('--------------------------')
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