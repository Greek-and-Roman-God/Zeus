# 백준 이분 탐색
# https://www.acmicpc.net/step/5


# 15596 번 : 정수 N개의 합
def solve(a):
    ans = 0
    ans = sum(a)
    return ans


# 4673 번 : 셀프넘버
def def_4673():
  def get_num_hap(n):
    remain = 0
    while n > 0:
      remain += n % 10
      n = n//10
    return remain

  arr_num = [0]*10001

  for i in range(10001):
    hap = get_num_hap(i)    
    tmp = hap + i
    if tmp < 10001:
      arr_num[tmp] = 1

  for i, v in enumerate(arr_num):
    if v == 0:
      print(i)


# 1065 번 : 한수
def def_1065():
  num = int(input()) #입력받은 수
  if num < 100:
    print(num) #두자리수까지는 다 한수임
    return

  def check_han_su(n) :
    str_n = str(n)
    num_arr = []

    #여기는 필요없는 부분이었음!!!!!!!!
    #string에 바로 index 줄 수 있어요
    for i in range(len(str_n)):
      tmp = str_n[i]
      num_arr.append(int(tmp))
    

    cha = num_arr[1] - num_arr[0] #등차 
    for i in range(len(num_arr)-1):
      if num_arr[i+1] == num_arr[i] + cha : #등차라면
        continue
      else : #등차가 아니면
        return 0
    else:
      return 1
    
  result = 99
  
  for i in range(100, num+1):
    answer = check_han_su(i)
    result += answer
  print(result)


  



  
