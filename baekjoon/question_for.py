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


