# 백준 1차원 배열
# https://www.acmicpc.net/step/6

# 10818번 : 최소, 최대
def array_10818():
  n = int(input())
  nums_arr = list(map(int, input().split()))

  if len(nums_arr) != n:
    print("다시 입력하세요")
    return
  
  nums_arr.sort() #크기 순 정렬

  print(nums_arr[0], nums_arr[n-1]);


# 2562번 : 최댓값
def array_2562():
  
  nums_arr = []
  for i in range(9):
    nums_arr.append(int(input()))

  compare_arr = []

  for i in range(len(nums_arr)):
    compare_arr.append([i+1,nums_arr[i]])

  compare_arr.sort(key = lambda x:x[1])
  print(compare_arr[-1][1])
  print(compare_arr[-1][0])

#2577번 : 숫자의 개수
def array_2577():
  A = int(input())
  B = int(input())
  C = int(input())

  prod_num = A*B*C

  prod_arr = list(map(int,str(prod_num)))
  # num_arr = [0]*10
  
  for i in range(10):
     cnt = prod_arr.count(i)
     print(cnt)
  #   num_arr[i] = cnt
  
  # for num in num_arr:
  #   print(num)

