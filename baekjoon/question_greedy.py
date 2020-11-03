# 11047번 : 동전 0
def greedy_11047():

    n, k = map(int, input().split())
    arr = [0]*n

    cnt = 0

    for i in range(n):
        arr[i] = int(input())

    arr.sort()
    arr.reverse()  # 내림차순

    for i in range(n):
        cnt += k//arr[i]

        k = k % arr[i]
    print(cnt)


# 11399번 : ATM
def greedy_11399():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    time_sum = 0

    for i in range(n):
        time_sum += arr[i] * (n-i)
    print(time_sum)