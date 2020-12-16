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


# 1929 번 : 소수 구하기
# def math_1929():
#   m, n = map(int, input().split())

#   for i in range(m, n+1):
#     if i == 1 : continue
#     if i == 2 : print(2)
#     cnt = 0
#     j = 0
#     while j**2 <= i:
#       j += 1
#       if i % j == 0:
#         cnt += 1
#         if cnt > 1:
#           break
#     else:      
#       print(i)

def math_1929():
  m, n = map(int, input().split())

  nums = [i for i in range(n+1)]

  for num in range(2, n+1):
    if nums[num] == 0:
      continue
    else:
      for j in range(num*2, n+1, num):
        nums[j] = 0
  
  for i in range(m, n+1):
    if nums[i] != 0 and nums[i]!= 1: print(nums[i])


# 1085 번 : 직사각형에서 탈출하기
def math_1085():
  x,y,w,h = map(int, input().split())
  nums = [x, y, w-x, h-y]
  print(min(nums))


# 3009 번 : 네 번째 점
def math_3009():
  arr_x = []
  arr_y = []
  
  for _ in range(3):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)
  
  ans_x, ans_y = 0, 0

  for i in range(3):
    if arr_x.count(arr_x[i]) == 1:
      ans_x = arr_x[i]
    if arr_y.count(arr_y[i]) == 1:
      ans_y = arr_y[i]
  print(ans_x, ans_y)