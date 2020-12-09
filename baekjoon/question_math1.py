# 백준 수학 1
# https://www.acmicpc.net/step/8

# 1712 번 : 손익분기점
def math_1712():
  #a = 고정비용, b = 노트북 한대 만드는 비용, c = 노트북 가격
  a,b,c = map(int, input().split())

  #노트북 만드는데 드는 총 비용 = 총 이익
  # a + (b*cnt) = c*cnt
  # a = c*cnt - b*cnt
  # a = (c-b)cnt 에서 양변을 c-b로 나누면 cnt를 구할 수 있음
  # 근데 이 경우는 이득이 난 게 아니라, 딱 0원인 수준이기 때문에
  # +1을 해서 이익이 나게 만들어야함

  cnt = 0 #노트북의 갯수
  if b >= c :
    print(-1)
  else :
    cnt = a // (c-b) + 1
    print(cnt)


# 2839 번 : 설탕 배달
def math_2839():
  n = int(input())
  
  a = n//5 #5키로의 갯수

  for _ in range(a+1):
    b = (n-(5*a)) // 3 #3키로의 갯수

    # print('-------------', a,b)

    if 5*a + 3*b == n:
      print(a+b)
      break
    else:
      a -= 1
  else :
    print(-1)


# 2292 번 : 벌집
def math_2292():
  n = int(input())

  if n == 1 :
    print(1)
    return

  cnt = 1
  d = 2 #등차를 나타낼 변수
  answer = 2 #각 줄을 카운트 할 변수
  print('cnt :', cnt)
  while cnt*6 + 1 < n: 
    cnt += d
    answer += 1
    print('while탐------------d :',d,'// cnt :',cnt)
    d += 1
  print('while 밖으로 나옴... cnt :',cnt)
  print(answer)


# 1193 번 : 분수찾기
def math_1193():
  n = int(input())

  cnt = 0
  i = 0
  while cnt < n :
    i += 1
    cnt += i
  # print('i, cnt', i, cnt)
  
  if i % 2 == 0 : #짝수 줄이라면 (분모가 증가)
    bunmo = 1 + (cnt - n)
    bunja = (i+1) - bunmo
  else: #홀수줄이라면 (분자가 증가)
    bunja = 1 + (cnt - n)
    bunmo = (i+1) - bunja

  print('{0}/{1}'.format(bunja, bunmo))


# 2869 번 : 달팽이는 올라가고 싶다
def math_2869():
  a, b, v = map(int, input().split())
  day = 1

  day2 = (v-a) // (a-b)
  chk = (v-a) % (a-b)
  if chk == 0 :
    day += day2
  else:
    day += day2 + 1
  print(day)


# 10250 번 : ACM 호텔
def math_10250():
  # 이 문제를 푸는데 중요한 사실!
  # floor = n % h 인데, 만약 나누어 떨어져버리면
  # floor = 0이 돼버린다. 그런 경우에는 h가 층이 될 수 있도록 처리해준다.

  t = int(input())

  for _ in range(t):
    answer = ''
    h, w, n = map(int, input().split())
    floor = 0 #층
    ho = 0 #호수

    floor = n % h 
    ho = n // h
    if floor != 0: #나누어 떨어지지 않으면
      ho += 1
    else : #나누어 떨어지면
      floor = h
    print('{0}{1:02d}'.format(floor, ho))
      

# 1011 번 : Fly me to the Alpha Centauri
import math
def math_1011():
  t = int(input())

  for _ in range(t):
    x, y = map(int, input().split())
    d = y-x #두 점 사이의 거리

    answer = 0

    root = math.floor(math.sqrt(d)) #거리의 제곱근을 소수점 버리고 정수로

    if math.sqrt(d) == root: #d가 제곱수라면
      answer = 2*root - 1
    else: #제곱수가 아니라면
      double1 = root ** 2
      double2 = (root+1) ** 2
      center = math.ceil((double1 + double2) / 2)

      if d >= center: #d가 center보다 같거나 크다면
        answer = 2*root + 1
      else : #d가 center보다 작다면
        answer = root * 2
    print(answer)

    
# 2775 번 : 부녀회장이 될테야
def math_2775():
  t = int(input()) #테케의 수

  def find_people(k, n):
    if k == 0 : #0층이면
      return n

    apt = [ [0 for i in range(15)] for _ in range(15) ]
    apt[0] = [i for i in range(15)] #0층은 1부터 15까지 차례로 들어감

    for i in range(1, k+1):
      for j in range(1, n+1):
        apt[i][j] = apt[i-1][j] + apt[i][j-1]
    print(apt)
    return apt[k][n]

  for _ in range(t):
    k = int(input()) #층
    n = int(input()) #호
    print(find_people(k,n))
    


