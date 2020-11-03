
# 11047번 : 동전 0
def greedy_11047():

  n, k = map(int, input().split())
  arr = [0]*n

  cnt = 0

  for i in range(n):
    arr[i] = int(input())

  arr.sort()
  arr.reverse()  # 내림차순

  for i in range(n):
    cnt += k//arr[i]

    k = k % arr[i]
  print(cnt)


# 11399번 : ATM
def greedy_11399():
  n = int(input())
  arr = list(map(int, input().split()))
  arr.sort()
  time_sum = 0

  for i in range(n):
    time_sum += arr[i] * (n-i)
  print(time_sum)


# 1541번 : 잃어버린 괄호
def greedy_1541():
  input_string = input()
  # input_string = '10+20-30+40+50+60'
  result = 0

  sums = []

  splited_string = input_string.split('-')
  splited_int = []

  if len(splited_string) == 1:
    # nums = list(map(int, splited_string[0].split('+')))
    nums = calc_splited_string(splited_string[0])
    print(sum(nums))
    return

  for temp in splited_string:
    # nums = list(map(int, temp.split('+')))
    nums = calc_splited_string(temp)
    sums.append(sum(nums))

  result += sums[0]
  for i in range(1, len(sums)):
    result -= sums[i]
  print(result)

def calc_splited_string(input_str):
  nums = list(map(int, input_str.split('+')))
  return nums
    

# 1931번 : 회의실 배정
def greedy_1931():
  n = int(input()) #회의 갯수
  meetings = []
  cnt = 0
  end = 0
  start = 0

  for i in range(n):
    tmp = list(map(int, input().split()))
    meetings.append(tmp)

  #끝나는시간으로 정렬후 그 안에서 시작시간으로 정렬
  sorted_m = sorted(meetings, key=lambda x : (x[1], x[0])) 

  b = 0 #before의 b
  a = 1 #after의 a
  while a < n:
    end = sorted_m[b][1] #앞 회의 끝시간
    start = sorted_m[a][0] #뒤 회의 시작시간

    if end <= start:
      cnt += 1
      b = a
      a += 1
    else:
      a += 1

  result = cnt+1 #맨 처음에 들어가는 회의 하나까지 포함해야하므로 +1함
  print(result)