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