#greedy part3

#Q1 모험가 길드
def grouping_guild():
  num = int(input()) #몇 명의 모험가인지
  adventurer_arr = list(map(int, input().split())) #모험가들의 공포도를 받아 안에 넣음
  adventurer_arr.sort()
  print(adventurer_arr)

  i = 0
  cnt = 0

  while True:
    tmp = num - adventurer_arr[i] - 1
    if i > tmp:
      break

    i += adventurer_arr[i]
    cnt += 1

  print('cnt=====',cnt)

  
#Q2 곱하기 혹은 더하기
def mul_or_plus():
  result = 0
  num_arr = list(map(int,input()))
  size = len(num_arr)

  result += num_arr[0]

  for i in range(size-1):
    tmp = num_arr[i+1]
    if result == 1 or result == 0:
      result += tmp
      continue
    if tmp == 0:
      result += tmp
    else:
      result *= tmp
  print(result)

#Q3 문자열 뒤집기
def flip_string():
  result = 0
  cnt_zero = 0 #0을 뒤집는 횟수
  cnt_one = 0 #1을 뒤집는 횟수

  num_str = input()
  num_arr = list(map(int,num_str))

  for i in range(len(num_arr)-1):
    if num_arr[i] != num_arr[i+1]:
      if num_arr[i+1] == 0:
        cnt_one += 1
      if num_arr[i+1] == 1:
        cnt_zero += 1
  
  if num_arr[-1] == 0:
    cnt_zero += 1
  else:
    cnt_one += 1
  
  result = min(cnt_zero, cnt_one)
  print(result)


#Q4 만들 수 없는 금액
def cannot_make_price():
  n = int(input()) #동전의 갯수
  arr_list = list(map(int, input().split()))
  target = 1
  answer = 0

  if n != len(arr_list):
    print('다시 입력하세요')

  arr_list.sort() #오름차순으로 정렬

  for cur_val in arr_list:
    if target < cur_val:
      answer = target
      break
    target = target + cur_val
    
  print(answer)


#Q5 볼링공 고르기
def choose_ball():
  cnt = 0
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  # print(n,'//',m,'//',arr)

  for i in range(n-1):
    for j in range(i+1, n):
      print(i,'//',j)
      if arr[i] == arr[j]:
        continue
      else:
        cnt += 1
  print(cnt)
