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
