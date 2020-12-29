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

  cnt = len(str(n)) #총 몇자리 숫자인지

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


# 1436 번 : 영화감독 숌
def brute_1436():
  n = int(input())
  cnt = 0
  num = 665
  while cnt < n:
    num += 1
    if str(num).count('666') > 0:
      cnt += 1
  print(num)


# 1018 번 : 체스판 다시 칠하기
def brute_1018():
  n, m = map(int, input().split())

  #chess 입력받는
  chess = []
  for i in range(n):
    line = input()
    if len(line) != m:
      break
    chess.append(line)

  def change_color(color):
    if color == 'B':
      return 'W'
    else:
      return 'B'
  
  def check_chess(a, b): #세로, 가로
    end_a = a+8
    end_b = b+8
    cnt = 0

    first_color = chess[a][b] #첫번째 칸의 색
    for i in range(a, end_a):
      for j in range(b, end_b):
        if chess[i][j] != first_color:
          cnt += 1
        first_color = change_color(first_color)
      first_color = change_color(first_color)
    return(min(cnt, 64-cnt))

  cnts = []
  for i in range(n-7): #세로
    for j in range(m-7): #가로
      cnts.append(check_chess(i,j))
  print(min(cnts))



# 7568 번 : 덩치
def brute_7568():
  n = int(input())
  dict_people = {}
  for i in range(n):
    dict_people[i] = list(map(int, input().split()))


  # n = 5
  # dict_people = {0: [55, 185], 1: [58, 183], 2: [88, 186], 3: [60, 175], 4: [46, 155]}

  sorted_people = sorted(dict_people.items(), key = lambda x:x[1][0] ) #몸무게로 정렬
  dict_big = {}
  
  for i, v in enumerate(sorted_people):
    # print('-----------------------------', i)
    tmp_key = v[0]
    tmp_tall = v[1][1]
    tmp_weight = v[1][0]
    # print('now.......... <',tmp_key,'>...',tmp_weight,tmp_tall)
    cnt = 1 #등수
    for j in range(i+1, n):
      #몸무게로 정렬돼있으니 키 비교함
      tall = sorted_people[j][1][1]
      weight = sorted_people[j][1][0]
      if tmp_tall < tall and tmp_weight < weight: #자기보다 덩치가 큰 사람이 나타나면
        cnt += 1 #순위가 밀림
    dict_big[tmp_key] = cnt
    sorted_big = sorted(dict_big.items())
  for i in range(n):
    print(sorted_big[i][1], end=' ')