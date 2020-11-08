# 점프 투 파이썬
# 3장 연습문제

# Q1
# 가장 먼저 조건에 맞는 shirt 가 출력됨


# Q2
def while_3multiple():
  n = 3
  while n<1001:
    print(n)
    n += 3
    
# Q3
def while_stars():
  i = 1
  while i <= 5:
    print("*"*i)
    i += 1

# Q4
def for_print_nums():
  for i in range(100):
    print(i+1)

# Q5
def for_avgs():
  scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
  sum = 0
  for score in scores:
    sum += score
  avg = sum / len(scores)
  print(avg)

# Q6
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
def for_list_comprehension():
  numbers = [1, 2, 3, 4, 5]
  result = [n*2 for n in numbers if n%2==1]
  print(result)
