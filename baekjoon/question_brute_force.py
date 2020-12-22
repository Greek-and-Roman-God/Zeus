# 백준 브루트 포스
# https://www.acmicpc.net/step/22


# 2798 번 : 블랙잭
import itertools
def brute_2798():
  n, m = map(int, input().split())
  cards = list(map(int, input().split()))

  groups = list(sum(n) for n in itertools.combinations(cards, 3))
  
  chas = {}
  for num in groups:
    cha = abs(num - m)

    if cha == 0:
      print(num)
      return
    else:
      chas[num] = cha #dict에 추가
  
  chas = sorted(chas.items(), key = lambda x:x[1])
  for cha in chas:
    if cha[0] <= m:
      print(cha[0])
      return
    else: continue