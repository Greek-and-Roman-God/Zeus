# 점프 투 파이썬
# 2장 연습문제

#Q1
def calc_avg(kor, eng, math):
  avg = (kor + eng + math) / 3
  print(avg)

#Q2
def check_even(num):
  answer = 'even'
  if num % 2 == 1:
    answer = 'odd'
  print(answer)

#Q3
def jumin_slicing(jumin):
  front = jumin[0:6]
  back = jumin[7:14]
  print(front, back)

#Q4
def jumin_gender(jumin):
  gender = jumin[7]
  print(gender)

#Q5
def replace_str(s):
  new_s = s.replace(":", "#")
  print(new_s)

#Q6
def sort_the_list():
  arr = [1,3,5,4,2]
  arr.sort(reverse = True)
  print(arr)

#Q7
def join_the_list():
  arr = ['Life', 'is', 'too', 'short']
  s = " ".join(arr)
  print(s)

#Q8
def add_to_tuple():
  t1 = (1,2,3)
  t2 = (4,) #이거 중요!!!!
  print(t1 + t2)

#Q9
#딕셔너리의 키는 변하는 값을 쓰면 안돼서
#list는 변할수있는 형이기때문에 오류가 발생한다

#Q10
def dict_pop():
  a = {'A':90, 'B':80, 'C':70}
  print(a)
  result = a.pop('B')
  print(a, result)

#Q11
def remove_mul():
  a = [1,1,1,2,2,3,3,3,4,4,5]
  a_set = set(a)
  print(a_set)

#Q12
def mul_values():
  a = b = [1,2,3]
  a[1] = 100
  print(a)
  print(b)
  # 마치 a만 바뀔것같지만 아니다!!
  # a와 b는 같은 리스트 객체를 가리키는 말이기 때문이다!