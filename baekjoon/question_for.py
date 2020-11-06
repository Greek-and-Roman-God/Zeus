# 백준 for문
# https://www.acmicpc.net/step/3

# 2739 번 : 구구단
def for_2739():
  dan = int(input())

  for i in range(1, 10):
    print("{0} * {1} = {2}".format(dan, i, dan*i))

# 10950 번 : A+B -3
def for_10950():
  t = int(input())
  for i in range(t):
    a, b = map(int, input().split())
    print(a+b)

# 8393 번 : 합
def for_8393():
  n = int(input())
  sum = 0
  for i in range(n+1):
    sum += i
  print(sum)

# 15552 번 : 빠른 A+B
import sys

def for_15552():
  t = int(sys.stdin.readline())
  for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

# 2741 번 : N 찍기
def for_2741():
  n = int(input())
  for i in range(n):
    print(i+1)

# 2742 번 : 기찍 N
def for_2742():
  n = int(input())
  for i in range(n):
    print(n-i)

# 11021 번 : A + B - 7
def for_11021():
  n = int(input())
  for i in range(n):
    a, b = map(int, input().split())
    print("Case #{0}:".format(i+1), a+b)

# 11022 번 : A + B - 8
def for_11022():
  n = int(input())
  for i in range(n):
    a, b = map(int, input().split())
    print("Case #{0}: {1} + {2} =".format(i+1, a, b), a+b)

# 2438 번 : 별찍기
def for_2438():
  n = int(input())
  for i in range(n):
    print( "*"*(i+1) )


# 2439 번 : 별찍기 -2
def for_2439():
  n = int(input())
  for i in range(n):
    print( " "*(n-i-1)+"*"*(i+1) )


# 10871 번 : x보다 작은 수
def for_10871():
  n, x = map(int, input().split())
  num_arr = list(map(int, input().split()))
  result = ""

  for i in range(n):
    if num_arr[i] < x:
      result += str(num_arr[i])+" "
  print(result)