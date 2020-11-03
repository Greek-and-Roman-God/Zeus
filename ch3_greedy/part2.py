#greedy

#3-1 거스름돈
def calc_coin(n):
  cnt = 0
  coins = [500,100,50,10] #동전의 종류

  for coin in coins:
    cnt += n // coin
    n %= coin
  
  print(cnt)


#3-2 실전문제 - 큰수의법칙
def calc_bigger_rule():
  sum = 0
  n, m, k = map(int, input().split())
  num_arr = list(map(int, input().split()))
  # print(num_arr)
  num_arr.sort()
  num_arr.reverse()
  # print(num_arr)

  for i in range(m):
    if((i+1)%(k+1) == 0):
      print('if')
      sum += num_arr[1]
    else:
      print('else')
      sum += num_arr[0]
  print(sum)


#3-3 실전문제 - 숫자카드게임
def calc_card():
  n, m = map(int, input().split())
  row_min_arr = []

  for i in range(n):
    row_arr = list(map(int, input().split()))
    min_num = min(row_arr)
    row_min_arr.append(min_num) #n번의 반복을 돌고나면 각 행의 min이 arr에 들어있음
  result = max(row_min_arr)
  print(result)


#3-4 실전문제 - 1이될때까지
def calc_until_one():
  cnt = 0
  n, k = map(int, input().split())
  # print("n과 k : ",n,k)

  while n >= k:
    if n % k != 0:
      n -= 1
      cnt += 1
    else: #나누어 떨어질때
      n //= k
      cnt += 1

  while n > 1:
    n -= 1
    cnt += 1
  
  print(cnt)


#3-4 실전문제 - 1이될때까지 재풀이
def calc_until_one_re():
  cnt = 0
  n, k = map(int, input().split())
  print("n과 k : ",n,k)

  while True:
    target = (n//k) * k
    cnt += n - target
    n = target

    if n < k:
      break

    n //= k
    cnt += 1

  if n < k:
    cnt += (n-1)

  print(cnt)

  

