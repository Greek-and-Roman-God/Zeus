# 백준 재귀
# https://www.acmicpc.net/step/19


# 10872 번 : 팩토리얼
def recursive_10872():
  n = int(input())

  def factorial(n):
    if n == 1 or n == 0:
      return 1
    return n*factorial(n-1)

  print(factorial(n))


# 10870 번 : 피보나치 수 5
def recursive_10870():
  n = int(input())

  def pibo(n):
    if n == 0:
      return 0
    if n == 1:
      return 1

    return pibo(n-1)+pibo(n-2)

  print(pibo(n))

