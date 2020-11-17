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
      
  