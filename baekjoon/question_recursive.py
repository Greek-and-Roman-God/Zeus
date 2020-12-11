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


# 11729 번 : 하노이 탑 이동 순서
def recursive_11729():
  global cnt, ans
  num = int(input()) #원판의 갯수
  cnt = 0
  ans = []

  def hanoi(num, from_n, by_n, to_n):
    global cnt, ans
    cnt += 1
    if num == 1:
      ans.append(str(from_n) + ' ' + str(to_n))
    else:
      hanoi(num-1, from_n, to_n, by_n)
      ans.append(str(from_n) + ' ' + str(to_n))
      hanoi(num-1, by_n, from_n, to_n)
    
  hanoi(num, 1, 2, 3)
  print(cnt)
  for a in ans:
    print(a)