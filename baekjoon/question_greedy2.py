# 백준 그리디 (다시 풀기)
# https://www.acmicpc.net/step/33


# 11047번 : 동전 0
def greedy2_11047():
  n, k = map(int, input().split())
  coins = [int(input()) for _ in range(n)]

  # n, k = 10, 4790
  # coins = [1,5,10,50,100,500,1000,5000,10000,50000]

  coins.sort(reverse=True) #큰 수부터 내림차순 정렬
  cnt = 0 #동전의 갯수

  for c in coins:
    cnt += k//c
    k %= c
  print(cnt)


# 1931 번 : 회의실배정
def greedy2_1931():
  n = int(input())
  meetings = []

  for _ in range(n):
    s, e = map(int, input().split())
    meetings.append([s,e])
 
  answer = 1

  meetings = sorted(meetings, key = lambda x : (x[1], x[0]) )

  pre = 0 #맨 처음 회의 
  nex = 1 #두번째 회의 

  while nex < n:
    pre_end = meetings[pre][1]
    next_start = meetings[nex][0]

    if pre_end <= next_start: #이전 회의의 종료시간 <= 지금 회의의 시작시간 이라면
      answer += 1
      pre = nex
    nex += 1

  print(answer)
