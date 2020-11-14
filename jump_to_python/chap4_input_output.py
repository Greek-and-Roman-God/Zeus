# 점프 투 파이썬
# 4장 연습문제
# 프로그램의 입력과 출력


# Q1 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수 is_odd를 작성해보자
def is_odd():
  n = 13 #주어진 자연수

  result = "짝수"
  if n % 2 != 0 :
    result = "홀수"
  print(result)


# Q2 입력으로 들어오는 모든 수의 평균값을 계산하는 함수 작성
#(입력으로 들어오는 수의 개수는 정해져있지 않음)
def avg_all(*args):
  result = 0
  sum = 0
  for num in args:
    sum += num
  result = sum / len(args)
  print(result)

# Q3 두 수를 입력받아 더해서 돌려주는 프로그램을 작성
def sum_of_two():
  num1 = int(input())
  num2 = int(input())

  print(num1+num2)

# Q4
# 3번이 다르다! 3번만 중간에 띄어쓰기가 들어감


# Q5 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 
#다시 그 파일을 읽어서 출력하는 프로그램이다.
def make_file():
  f1 = open("test.txt", "w")
  f1.write("Life is too short")
  f1.close() #파일을 열어서 썼으면 닫아주어야 다시 열어서 읽던지 할 수 있음

  f2 = open("test.txt", "r")
  print(f2.read())
  f2.close()


# Q6 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. 
# (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
def make_file2():
  f1 = open("test2.txt", "a")
  temp_txt = input()
  f1.write(temp_txt)
  f1.close()

  f2 = open("test2.txt", "r")
  print(f2.read())
  f2.close()


# Q7 다음과 같은 내용을 지닌 파일 test.txt가 있다. 
# 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
def change_file():
  f1 = open("test2.txt", "r")
  text = f1.read()
  f1.close()

  text = text.replace('라라라', '하하하')

  f1 = open("test2.txt", "w")
  f1.write(text)
  f1.close()
