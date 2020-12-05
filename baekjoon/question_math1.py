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
  # +1을 해서 이익이 나게 만들어야함a, b, c = map(int, input().split())

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