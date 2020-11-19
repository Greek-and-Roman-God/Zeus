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


#3052번 : 나머지
def array_3052():
  nums_arr = []
  answer = ()
  for i in range(10):
    nums_arr.append( int(input())%42 )
  
  answer_set = set(nums_arr)
  print(len(answer_set))


# 1546번 : 평균
def array_1546():
  score_arr = []
  n = int(input()) #갯수
  score_arr = list(map(int, input().split()))
  
  score_arr.sort(reverse=True) #내림차순 정렬
  max_score = score_arr[0]

  for i in range(n):
    score_arr[i] = (score_arr[i]/max_score)*100
  print(sum(score_arr)/n)
  

#8958번 : OX퀴즈
# def array_8958():
  # n = int(input())
  # nums_arr = []
  # result_arr = []

  # #배열에 넣는 작업
  # for i in range(n):
  #   s = list(input())
  #   nums_arr.append(s)
  # #빼서 계산하는 작업
  # for tmp_s in nums_arr:
  #   tmp_result = 0
  #   score = 1
  #   for i in range(len(tmp_s)-1):
  #     if tmp_s[i] == 'O':
  #       tmp_result += score
  #       if tmp_s[i+1] == 'O':
  #         score += 1
  #         continue
  #       else:
  #         score = 1
  #         continue
  #   if tmp_s[-1] == 'O':
  #     tmp_result += score
  #   result_arr.append(tmp_result)
  # for result in result_arr:
  #   print(result)

def array_8958():
  n = int(input())
  nums_arr = []
  result_arr = []

  #배열에 넣는 작업
  for i in range(n):
    s = list(input())
    nums_arr.append(s)

  for tmp_s in nums_arr:
    cnt = 1
    result = 0
    for s in tmp_s:
      if s == 'X':
        cnt = 1
        continue
      
      result += cnt
      cnt += 1
    print(result)
    


#4344번 : 평균은 넘겠지
def array_4344():
  n = int(input()) #케이스 갯수
  case_arr = []
  result_arr = []

  for i in range(n):
    case = list(map(int, input().split()))
    case_arr.append(case)
  
  for case in case_arr:
    case_cnt = case[0] #인덱스0은 학생 명 수
    score_sum = sum(case) - case_cnt #전체합-명수
    score_avg = score_sum / case_cnt

    over = 0 #평균을 넘는 학생수
    rate = 0
    for i in range(1, len(case)):
      if case[i] > score_avg:
        over += 1
    rate = round(over / case_cnt * 100, 3)
    print(rate)
    result_arr.append(rate)
  for r in result_arr:
    print("%0.3f%%" % r)
