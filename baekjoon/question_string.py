# 백준 문자열 단계
# https://www.acmicpc.net/step/7

# 11654 번 : 아스키 코드
def string_11654():
  c = str(input())
  print(ord(c))


# 11720 번 : 숫자의 합
def string_11720():
  n = int(input())
  num = input()

  if len(num) != n:
    print("입력 다시하세요")
  
  num_list = list(map(int, num))
  print(sum(num_list))


# 10809 번 : 알파벳 찾기
def string_10809():
  s = str(input())
  
  ascii_a = ord('a')
  ascii_z = ord('z')


  for i in range(ascii_a, ascii_z+1):
    tmp_s = chr(i)
    print(s.find(tmp_s), end=' ')


# 2675 번 : 문자열 반복
def string_2675():
  t = int(input())
  for _ in range(t):
    r, s = input().split()

    r = int(r)

    answer = ''
    for i in range(len(s)):
      tmp = s[i]
      answer += tmp*r
    print(answer)


# 1157 번 : 단어 공부
def string_1157():
  input_s = input()
  input_s = input_s.upper() #전부 대문자로 만듬
  
  dictS = {}
  for s in input_s:
    if s not in dictS:
      dictS[s] = 1
    else:
      dictS[s] += 1

  s_list = sorted(dictS.items(), key=lambda x:x[1], reverse=True)
  
  if len(input_s)>1 and s_list[0][1] == s_list[1][1]:
    print('?')
  else:
    print(s_list[0][0])

# 1157 번 : 단어 공부
# def string_1157():
#   input_s = input()
#   input_s = input_s.upper() #전부 대문자로 만듬

#   set_s = list(set(input_s))
#   print(set_s)

#   cnt_s = []
#   for s in set_s:
#     cnt_s.append(input_s.count(s))


#   maxcnt = max(cnt_s)
  
#   cnt_s.sort()
#   if cnt_s[0] == cnt_[1]:
#     print('?')
  
#   index = cnt_s.index(maxcnt) #최대값이 들어있는 인덱스

  


# 1152 번 : 단어의 갯수
def string_1152():
  list_input = list(input().split())
  print(len(list_input))


# 2908 번 : 상수
def string_2908():
  n,m = input().split()
  listn, listm = list(n), list(m)

  newn, newm = '', ''

  for i in range(2,-1,-1):
    newn += listn[i]
    newm += listm[i]

  print(max(int(newn), int(newm)))


# 5622 번 : 다이얼
def string_5622():
  s = input()

  dist = 0
  for i in range(len(s)):
    tmp = s[i]
    if tmp in ('A','B','C'):
      dist += 3
    elif tmp in ('D','E','F'):
      dist += 4
    elif tmp in ('G','H','I'):
      dist += 5
    elif tmp in ('J','K','L'):
      dist += 6
    elif tmp in ('M','N','O'):
      dist += 7
    elif tmp in ('P','Q','R','S'):
      dist += 8
    elif tmp in ('T','U','V'):
      dist += 9
    elif tmp in ('W','X','Y','Z'):
      dist += 10
    else:
      dist += 11
  print(dist)


# 2941 번 : 크로아티아 알파벳
# 1트 : dz= 를 고려하지 못해서 실패
# def string_2941():
#   list_s = list(input())

#   cnt = 0
#   for i, s in enumerate(list_s):
#     idx1, idx2 = 0, 0
#     if s in ('=', '-', 'j'):
#       idx2 = i
#       idx1 = i-1
#       # print('indexes... ', idx1, idx2)
#       list_s[idx1] = 0
#       list_s[idx2] = 0
#       cnt += 1
#   cnt += (len(list_s) - list_s.count(0))

#   print(cnt)


# 2941 번 : 크로아티아 알파벳
# 2트
def string_2941():
  s = input()

  chk_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

  for chk in chk_list:
    if chk in s:
      s = s.replace(chk, 'a')
  
  print(len(s))


# 1316 번 : 그룹 단어 체크
def string_1316():
  n = int(input()) #단어 갯수
  list_s = []
  ascii_a = ord('a')
  cnt = 0

  for _ in range(n):
    list_s.append(input())

  for s in list_s:
    alphas = [0]*26
    # print('---------------------------', s)
    for i in range(len(s)-1):
      # print('---------------------', i)

      tmp_ascii = ord(s[i])
      alphas[tmp_ascii - ascii_a] = 1

      if len(s) > 1:
        # print('if탐1')
        nxt_ascii = ord(s[i+1])
        if s[i] == s[i+1]: #두 글자가 연속해서 나오면
          # print('if탐2')
          continue
        else: #다른 글자가 나오면
          # print(tmp_ascii, nxt_ascii, ascii_a)
          if alphas[nxt_ascii - ascii_a] == 1:
            break
    else : cnt += 1
  print(cnt)
  

        
