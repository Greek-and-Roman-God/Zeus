# 백준 수학2
# https://www.acmicpc.net/step/10


# 1978 번 : 소수 찾기
def math_1978():
  n = int(input()) #입력받을 갯수
  nums = list(map(int, input().split()))

  answer = 0

  for num in nums:
    if num == 1: 
      continue
    else:
      i = 1
      cnt = 0
      while 2*i <= num: 
        if num % i == 0:
          cnt += 1
        i += 1
      
      if cnt == 1:
        answer += 1
  print(answer)


# 2581 번 : 소수
def math_2581():
  m = int(input())
  n = int(input())

  answers = []

  for i in range(m, n+1):
    if i == 1: continue
    elif i == 2: 
      answers.append(i) 
      continue

    cnt = 0
    j = 0
    while j*2 <= i:
      j += 1
      if i % j == 0:
        cnt += 1
        if cnt > 1: break
    if cnt == 1:
      answers.append(i)
  
  if len(answers) == 0:
    print(-1)
    return

  print(sum(answers))
  print(answers[0])