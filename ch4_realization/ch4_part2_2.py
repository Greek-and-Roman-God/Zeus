global cur_direc #전역변수로 사용하고싶으면 global 을 붙여줘야한다..!
global turn_cnt

def game_make():
  global cur_direc #함수 안에도 붙여줘야한다. 안붙이면 지역변수로 처리됨!
  global turn_cnt

  map_a, map_b = map(int, input().split()) #맵의 세로길이, 가로길이
  x, y, cur_direc = map(int, input().split()) #캐릭터의 현재 x, y, 보는방향
  maps = []

  cur_direc = 0
  turn_cnt = 0

  for i in range(map_a):
    maps.append(list(map(int, input().split()))) #현재 맵을 받음

  print(maps)

  #테스트용
  # map_a, map_b = 4, 4 #맵의 세로길이, 가로길이
  # x, y, cur_direc = 1, 1, 0 #캐릭터의 현재 x, y, 보는방향
  # maps = [[1, 1, 1, 1],
  #         [1, 0, 0, 1],
  #         [1, 1, 0, 1],
  #         [1, 1, 1, 1]]
  # print(x,y,cur_direc)

  #이런 방문한 문제는 아예 다른 리스트를 하나 만들어서 비교하는게 빠르다고 함
  #visited maps의 약자
  v_maps = [[0]*map_b for _ in range(map_a)]

  v_maps[x][y] = 2 #시작한 위치는 방문했으므로 2로 변경

      #북, 동, 남, 서 이동하는 좌표의 설정 
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]


  while 1:
    rotation() #일단 왼쪽 돌고 시작
    nx = x + dx[cur_direc] #nx, ny는 이동한 위치. 확인용임
    ny = y + dy[cur_direc] #바라보고있는 방향으로 한칸 전진

    #전진할 수 있는 경우
    if maps[nx][ny] == 0 and v_maps[nx][ny] == 0:
      v_maps[nx][ny] = 2 #방문했다고 2로 만들어줌
      x = nx
      y = ny #이동을 확정지어줌
      print('turn cnt ', turn_cnt)
      clear_turnCnt()
      continue
    #앞에가 이미 가봤거나, 바다인 경우 
    else:
      turn_cnt += 1
      print('turn cnt ', turn_cnt)

    if turn_cnt == 4: #4번 돌았는데 갈수없는경우
      nx = x - dx[cur_direc]
      ny = y - dy[cur_direc] #방향은 그대로 바라보면서, 한칸 후진함
      print('turn cnt ', turn_cnt)

      # 뒤로 갈수있다면
      if maps[nx][ny] == 0 :
        v_maps[nx][ny] = 2 #방문했다고 2로 만들어줌
        x = nx
        y = ny
      # 후진하는데 바다여서 못간다!
      else:
        break
      clear_turnCnt()
  
  answer = 0
  for v in v_maps:
    answer += v.count(2)

  print(v_maps)
  print(answer)


def rotation():
  # 회전하는 함수
  # 0북 1동 2남 3서 (북->서->남->동->북)
  global cur_direc
  cur_direc -= 1

  if cur_direc == -1:
    cur_direc = 3

def clear_turnCnt():
  # 이걸 초기화 해주지 않으면 숫자가 마냥 커져서
  # turn_cnt == 4 의 조건문을 계속 타서 틀린 답이 나오게 됨
  global turn_cnt
  turn_cnt = 0
      

