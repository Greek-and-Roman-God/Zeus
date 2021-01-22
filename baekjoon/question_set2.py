# BOJ 길라잡이 set2


# 1037 번 : 약수
def set_1037():
  n = int(input())
  nums = list(map(int, input().split()))

  nums.sort()
  original_num = nums[0] * nums[-1]
  
  print(original_num)


# 2609 번 : 최대공약수와 최소공배수
import math
def set_2609():
  n, m = map(int, input().split())

  num_gcd = math.gcd(n, m)
  num_lcd = n*m // num_gcd

  print(num_gcd)
  print(num_lcd)


#6603 번 : 로또
import itertools
def set_6603():
  nums_list = []
  while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1:
      break
    nums_list.append(nums)

  for nums in nums_list:
    num_cnt = nums[0] #숫자의 갯수
    num_list = nums[1:] #입력받은 숫자들

    for comb in itertools.combinations(num_list, 6):
      print(' '.join(str(c) for c in comb))
    print()



# 9095 번 : 1,2,3 더하기
import itertools
def set_9095():
  t = int(input()) #케이스의 갯수
  for _ in range(t):
    n = int(input())
    answer = 0

    num_list = [i for i in range(1, 4)] #1~3의 합으로 이루어져야 하므로
    num_prod = []
    
    for i in range(1, n+1):
      num_prod += list(map(sum, itertools.product(num_list, repeat=i)))
    
    for p in num_prod:
      if p == n:
        answer += 1
    print(answer)