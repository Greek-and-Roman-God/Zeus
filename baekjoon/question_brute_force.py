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


# 2231 번 : 분해합
def brute_2231():
  n = int(input())

  cnt = 0 #총 몇자리 수인지
  n_copy = n #n을 그냥 나눠버리니까 밑에서 못쓰므로...
  while n_copy > 0: #자릿수를 구하는 while
    n_copy //= 10
    cnt += 1

  startnum = n - (9*cnt) 
  #가장 작은 생성자를 구하라고 했으므로 각 자리수를 최대(9)라고 생각함
  #예를들어 216이라고 치면
  #생성자의 각 자리수가 999라고 생각 -> 3*9를 216에서 빼줌
  #189부터 for문을 돌기 시작함
  #189+1+8+9 / 190+1+9+0 / 191+1+9+1 / 192+1+9+2 ... 이런식으로 돌다가
  #if를 타면 출력하고 종료함

  for i in range(startnum, n+1, 1):
    nums = [] #각 자리 숫자
    i_copy = i

    while i_copy > 0:
      nums.append(i_copy%10)
      i_copy //= 10

    if sum(nums) + i == n:
      print(i)
      break
  else:
    print(0)
