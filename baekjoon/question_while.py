# 백준 while문
# https://www.acmicpc.net/step/2


# 10952번 : A+B - 5
def while_10952():
  while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
      break
    print(a+b)


# 10951번 : A+B - 4
def while_10951():
  while 1:
    try:
      a, b = map(int, input().split())
      print(a+b)
    except:
      break


# 1110번 : 더하기 사이클
def while_1110():
  n = int(input()) #입력받은 수
  origin_n = n  #원래 숫자를 보관
  cnt = 0

  while 1:
    a = n//10 #앞자리수
    b = n%10  #뒷자리수
    c = (a+b)%10  #합의 뒷자리수
    n = b*10 + c  #새 숫자
    cnt += 1

    if origin_n == n:
      break
  print(cnt)
