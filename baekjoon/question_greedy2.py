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
