#greedy part3

#Q1 모험가 길드
def grouping_guild():
  num = int(input()) #몇 명의 모험가인지
  adventurer_arr = list(map(int, input().split())) #모험가들의 공포도를 받아 안에 넣음
  adventurer_arr.sort()
  print(adventurer_arr)

  i = 0
  cnt = 0

  while True:
    tmp = num - adventurer_arr[i] - 1
    if i > tmp:
      break

    i += adventurer_arr[i]
    cnt += 1

  print('cnt=====',cnt)