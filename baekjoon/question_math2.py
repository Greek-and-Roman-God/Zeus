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


# 4948 번 : 베르트랑 공준
def math_4948():
  #체를 미리 선언해놓으면 시간초과가 안남
  #왜냐면 입력받는 숫자의 최댓값이 123456까지라고 돼있어서
  ran = 123456
  arr_nums = [0]*(2*ran+1) #기본 0으로 선언

  for i in range(ran + 1):
    if i == 0 or i == 1:
      arr_nums[i] = 1 #소수가 아니니까 1로 변경
    else:
      for j in range(2*i, 2*ran+1, i):
        arr_nums[j] = 1 #배수들은 소수가 아니니까 1로 변경

  #while문을 돌면서 확인
  while True:
    n = int(input())
    if n == 0: break

    answer = arr_nums[n+1:2*n+1].count(0)

    print(answer)


# 4153 번 : 직각삼각형
def math_4153():
  while True:
    num_arr = list(map(int, input().split()))

    if num_arr[0] == 0: break;

    answer = 'wrong'
    num_arr.sort()

    if num_arr[-1] ** 2 == num_arr[0]**2 + num_arr[1]**2:
      answer = 'right'
    print(answer)


# 3053 번 : 택시 기하학
import math
def math_3053():
  n = int(input())

  u_circle = n*n*math.pi
  t_circle = n*n*2 # 2n * 2n / 2 = 4n^2 / 2 = 2n^2 

  print(u_circle)
  print(t_circle)


# 1002 번 : 터렛
def math_1002():
  t = int(input())

  for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1==x2 and y1==y2: #두 점이 같은 위치
      if r1==r2: #반지름이 같으면 -> 두 원이 완전 일치
        print(-1)
      else : #반지름이 다름 -> 만나지않음
        print(0)
    else: #두 점의 위치가 다를때
      dist = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
      if dist == r1+r2 or dist == abs(r1-r2): #한 점 만남 (외접, 내접)
        print(1)
      elif abs(r1-r2) < dist < r1+r2: #두 점 만남
        print(2)
      elif dist > r1+r2 or dist != abs(r1-r2): #안만남 (밖에서, 안에서)
        print(0)



# 9020 번 : 골드바흐의 추측
def math_9020():
  t = int(input())
  nums = []
  for i in range(t):
    nums.append(int(input()))
  
  che = [0] * (max(nums)+1) #입력받은 수들 중 가장 큰 수까지 체 생성
  che[0], che[1] = 1, 1 #소수가 아니므로 1
  for i in range(2, len(che)//2 + 1): 
    for j in range(2*i, len(che), i):
      che[j] = 1 #소수가 아닌 애들 1로 변경

  for n in nums:
    answer = []
    for a, sosu_a in enumerate(che):
      if sosu_a == 0: #a가 소수일때
        b = n - a 
        # print('--------------', a, b)
        if che[b] == 0 and a <= b: #b도 소수이면
          answer.append([a,b])
    print(answer[-1][0], answer[-1][1])
    
    
    