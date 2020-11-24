# 백준 이분 탐색
# https://www.acmicpc.net/step/29


# 1920번 : 수 찾기
def binary_search_1920():
  n = int(input())
  A = list(map(int, input().split()))
    
  m = int(input())
  n_arr = list(map(int, input().split()))

  # n = 5
  # A = [4,1,5,2,3]
  # m = 5
  # n_arr = [1,3,7,9,5]

  A.sort()

  if len(A) != n or len(n_arr) != m:
    print("다시 입력하세요")
    
  
  for tmp_n in n_arr:
    start = 0
    end = len(A)-1 #A의 마지막 인덱스
    
    while 1:
      center = (start+end) // 2
      # print(start, end, center)

      if tmp_n == A[center]:
        print(1)
        break
      elif tmp_n < A[center]:
        end = center-1
      elif tmp_n > A[center]:
        start = center+1
      
      if start > end:
        print(0)
        break


# 10816번 : 숫자카드 1트
def binary_search_10816():
  _ = int(input())
  N = list(map(int, input().split()))
    
  _ = int(input())
  M = list(map(int, input().split()))

  # N = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
  # M = [10, 9, -5, 2, 3, 4, 5, -10]

            #   0   1   2  3  4  5  6  7   8   9
  N.sort() # [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
  # print(N)

  setN = set(N)

  result_arr = []

  def find_start(s,e,m):
    start = 0
    while 1:
      c = (e+s) // 2

      if m == N[c] :
        if N[c-1] == N[c]:
          e = c - 1
        elif N[c-1] != N[c]:
          start = c
          break 
      elif m < N[c]:
        e = c - 1
      elif m > N[c]:
        s = c + 1

      if s > e:
        start = e
        break
    return start

  def find_end(s,e,m):
    end = 0
    while 1:
      c = (e+s) // 2

      if m == N[c] :
        if N[c+1] == N[c]:
          s = c + 1
        elif N[c+1] != N[c]:
          end = c
          break 
      elif m < N[c]:
        e = c - 1
      elif m > N[c]:
        s = c + 1

      if s >= e:
        end = e
        break
    return end

  for m in M:
    s = 0
    e = len(N)-1 
    # print(m)

    if m not in setN:
      result_arr.append(0)
      continue

    st = find_start(s,e,m)
    ed = find_end(s,e,m)

    result_arr.append(ed-st+1)
  print(' '.join(str(r) for r in result_arr))   



# 10816번 : 숫자카드 2트
def binary_search_10816_2():
  _ = int(input())
  N = list(map(int, input().split()))
    
  _ = int(input())
  M = list(map(int, input().split()))

  # N = [6, 2, 2, 2, 3, 2, 10, 10, 10, 10, 10, -10, -10, 7, 3]
  # M = [10, 9, -5, 2, 3, 4, 5, -10]

            #   0   1   2  3  4  5  6  7   8   9
  N.sort() # [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
  # print(N)

  dictN = {}

  for n in N:
    if n in dictN:
      dictN[n] += 1
    else:
      dictN[n] = 1
  
  # print(dictN)
  
  for m in M:
    if m not in dictN:
      print(0, end=' ')
    else:
      print(dictN.get(m), end=' ')

  
# 1654번 : 랜선자르기
def binary_search_1654():
  k, n = map(int, input().split())
  lan_wires = []
  for _ in range(k):
    lan_wires.append(int(input()))

  # k, n = 4, 11
  # lan_wires = [802, 743, 457, 539]

  longest = max(lan_wires)

  left = 1
  right = longest
  result = 0

  while left <= right :
    center = (left + right) // 2
    # print('center=====', center)
    hap = 0

    for cm in lan_wires:
      hap += cm // center #쪼갠 랜선의 갯수의 합
    
    if hap < n:
      right = center -1 #길이를 작게만들어서 갯수가 늘어나게
    elif hap >= n :
      if center > result :
        result = center 
      left = center +1 #길이를 키워서 갯수가 줄어들게

  print(result)
  

# 2805 번 : 나무 자르기
def binary_search_2805():
  n, m = map(int, input().split())
  trees = list(map(int, input().split()))

  # n = 4
  # m = 7
  # trees = [20, 15, 10, 17]

  s = 0
  e = max(trees)
  answer = 0

  while s <= e :
    c = (s+e) // 2
    # print('s,e,c====', s,e,c)

    hap = 0
    for t in trees:
      if t >= c:
        tmp = t - c
        hap += tmp
        # print('tmp, hap', tmp, hap)
    
    if hap < m : #길이가 모자람
      e = c - 1
    elif hap >= m : #길이가 넘침
      s = c + 1
      answer = c 
  print(answer)



# 2110 번 : 공유기 설치
def binary_search_2110():
  # n, c = map(int, input().split())
  # house = []
  # for _ in range(n):
  #   house.append(int(input())) #집의 좌표를 입력받음

  n = 5
  c = 3
  house = [1,2,8,4,9]

  house.sort() #1,2,4,8,9

  e = house[-1] - house[0] #첫집에서 끝집까지의 거리 : 간격중 최대 간격
  s = 1 #간격중 최소간격 (최소간격이 될수있는건 1임. 중복 좌표가 없다고 했으니 0 불가) 


  while s <= e :
    cnt = 0
    dist = (e+s) // 2 #공유기를 설치하기위해 각재는 거리
    print('dist-------------------------------------', dist)
  
    prev_house = house[0]
    cnt += 1 #맨 첫집에 공유기 하나 설치
    print('cnt ---', cnt)

    for i in range(1, len(house)):
      print('---------------------------i ', i)
      tmp_house = house[i]
      d = tmp_house - prev_house #두 집 사이의 거리
      print('tmp_house...', tmp_house, '// d...' ,d)
      
      if d >= dist :
        cnt += 1
        prev_house = tmp_house
        print('cnt ---', cnt)
      else :
        continue

    if cnt < c : #설치한 공유기가 모자르다면(간격이 너무 넓어서)
      e = dist - 1 #거리를 줄이자
    else : #공유기가 딱맞거나 or 너무많이 설치됐다면 (간격이 촘촘해서) 
      s = dist + 1 #거리를 늘리자
      answer = dist
  print(answer)



    