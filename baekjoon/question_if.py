
# 1330번 두 수 비교하기
def compare_two_nums():
  num = list(map(int, input().split()))
  result = '>'

  if num[0] < num[1]:
    result = '<'
  
  if num[0]==num[1]:
    result = '=='
  
  print(result)


# 9498번 시험성적
def test_scores():
  grade = ''
  score = int(input())

  if score >= 90:
    grade = 'A'
  elif score >= 80:
    grade = 'B'
  elif score >= 70:
    grade = 'C'
  elif score >= 60:
    grade = 'D'
  else:
    grade = 'F'
  print (grade)


# 14681번 사분면 고르기
def choose_quadrant():
  x = int(input())
  y = int(input())
  q = 0

  if x>0 and y>0:
    q = 1
  if x>0 and y<0:
    q = 4
  if x<0 and y>0:
    q = 2
  if x<0 and y<0:
    q = 3
  print(q)


# 2884번 알람 시계
def alarm_clock():
  h, m = map(int, input().split())
  result_h, result_m = 0, 0

  if m < 45:
    result_m = m + 60 - 45
    result_h = h-1
    
    if result_h < 0:
      result_h = 23
  else:
    result_h = h
    result_m = m-45

  print(result_h, result_m)