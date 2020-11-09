# 이것이 코딩테스트다
# 챕터4 구현(realization)

# 예제 4-1 상하좌우
def up_down_left_right():
  n = int(input()) #사각형의 크기 n*n
  plans = input().split() #이동할 계획이 띄워쓰기로 구분되어 입력됨
  print(plans)
  # n = 5
  # plans = 'R R R U D D'.split()

  x = 1
  y = 1

  move_type = ['L', 'R', 'U', 'D']
  move_x = [-1, 1, 0, 0] # 가로 이동
  move_y = [0, 0, -1, 1] # 세로 이동

  temp_x = 0
  temp_y = 0

  for p in plans: # 들어온 플랜을 순서대로 하나씩 돌면서
    for i in range(len(move_type)):
      if p == move_type[i]:
        temp_x = x + move_x[i]
        temp_y = y + move_y[i]

        print('test1===', p, '// temp x, y==', temp_x, temp_y, '// x,y', x, y)
    
    if temp_x < 1 or temp_x > n or temp_y < 1 or temp_y > n:
      print('if탐')
      continue
        
    x = temp_x
    y = temp_y
    print('test2===', x, y)

  print(y, x) #출력 순서에 유의하기. (세로, 가로) 순서로 돼있음을 확인하기


# 예제 4-2 시각
# 12분 / 15분
def calc_times():
  n = int(input()) #입력받는 수
  cnt = 0

  for i in range(n+1):
    for j in range(60):
      for k in range(60):
        target = str(i)+str(j)+str(k)
        if '3' in target:
          cnt += 1
  print(cnt)


  # 실전문제 2 ) 왕실의 나이트
  #  31분 / 20분
def knight_in_castle():
  now_loc = input()
  # now_loc = "a1"

  x = now_loc[0]
  y = now_loc[1]

  alpha_dic = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
  }

  now_x = alpha_dic[x]
  now_y = int(y)

  move_x = [1, -1, 2, 2, 1, -1, -2, -2]
  move_y = [-2, -2, -1, 1, 2, 2, 1, -1]

  temp_x = 0
  temp_y = 0
  cnt = 0

  for i in range(len(move_x)):
    temp_x = now_x + move_x[i]
    temp_y = now_y + move_y[i]

    if temp_x < 1 or temp_x > 8 or temp_y < 1 or temp_y > 8:
      continue
    cnt += 1
  print(cnt)
  





