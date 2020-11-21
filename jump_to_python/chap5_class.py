# 점프 투 파이썬
# 5장 클래스, 모듈, 패키지 실습
# 연습문제 풀이는 하단에 있음

class FourCal:
  # def setData(self, input1, input2):
  #   self.num1 = input1
  #   self.num2 = input2
  #   print(self.num1, self.num2)
  def __init__(self, input1, input2):
    self.num1 = input1
    self.num2 = input2
    print(self.num1, self.num2)

  def add(self):
    print('합 :', self.num1+self.num2)
  def sub(self):
    print('차 :', self.num1-self.num2)
  def prod(self):
    print('곱 :', self.num1*self.num2)
  def div(self):
    print('나누기 :', self.num1/self.num2)

# a = FourCal()
# a.setData(10,2)


# b = FourCal()
# b.setData(12,4)
# b = FourCal(12, 4)
# b.add()
# b.sub()
# b.prod()
# b.div()

class MoreFourCal(FourCal): #상속
  def pow(self):
    print('제곱 :', self.num1 ** self.num2)

# c = MoreFourCal(3, 2)
# c.add()
# c.sub()
# c.prod()
# c.div()
# c.pow()

class safeFourCal(FourCal):
  def div(self): #오버라이딩
    if self.num2 == 0:
      print('0으로 나누는 것은 불가능합니다...', 0)
    else:
      print('나누기 :', self.num1/self.num2)

# d = safeFourCal(4, 0)
# d.add()
# d.sub()
# d.prod()
# d.div()


#===============================================================

# 점프 투 파이썬
# 5장 연습문제
# 클래스 등등

# Q1
class Calculator:
  def __init__(self):
      self.value = 0

  def add(self, val):
      self.value += val
      print(self.value)

class UpgradeCalculator(Calculator):
  def minus(self, val):
    self.value -= val
    print(self.value)

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)


# Q2
class MaxLimitCalculator(Calculator):
  def add(self, val):
    self.value += val
    if(self.value > 99):
      print("100 이상의 숫자는 출력할 수 없습니다")
      return
    print(self.value)

cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)


# Q3
#다음 결과를 예측해보자
#1) False
#2) True


# Q4
# filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
def use_filter():
  num_list = [1, -2, 3, -5, 8, -3]

  def positive(n):
    return n > 0 #양수면 true, 음수면 False

  filtered_list = list(filter(positive, num_list))
  print(filtered_list)


# Q5
# 16진수 문자열 0xea를 10진수로 변경해 보자.
def hex_to_int():
  hex_num = '0xea'
  hex_to_int = int(hex_num, 16)
  print(hex_to_int)

  
# Q6
# map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.
def mul_3():
  num_list = [1,2,3,4]
  new_list = list(map(lambda x:3*x, num_list))
  print(new_list)


# Q7
# 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
def sum_max_min():
  num_list = [-8, 2, 7, 5, -3, 5, 0, 1]
  maxnum = max(num_list)
  minnum = min(num_list)
  print(maxnum + minnum)

# Q8
# 위와 같은 결괏값 5.666666666666667을 소숫점 4자리까지만 반올림하여 표시해 보자.
def cut_decimal():
  result = 17/3
  cut_result = round(result, 4)
  print('%.4f' % result)
  print(cut_result)


# Q9
#chap5_Q9.py 에 작성했음


# Q10
# os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
import os
def use_os_module():
  result = os.popen("dir")
  print(result.read())


# Q11
# glob 모듈을 사용하여 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.
import glob
def use_glob():
  result = glob.glob("jump_to_python/*.py")
  print(result)


# Q12
# time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
import time
def use_time():
  now_time = time.localtime(time.time())
  _time = time.strftime('%Y/%m/%d... %H:%M:%S', now_time)
  print(_time)


# Q13
# random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자(단 중복된 숫자가 있으면 안 됨).
import random
def use_random():
  result = []
  i = 0
  while i < 6:
    num = random.randint(1, 45)
    if not num in result:
      result.append(num)
      i += 1
  print(result)
