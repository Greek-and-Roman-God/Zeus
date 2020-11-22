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
  

  