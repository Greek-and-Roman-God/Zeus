# 백준 정렬 단계
# https://www.acmicpc.net/step/9


# 2750 번 : 수 정렬하기
def sort_2750():
  n = int(input())
  nums = [int(input()) for _ in range(n)]

  nums.sort()
  for num in nums: print(num)


# 2751 번 : 수 정렬하기 2
# sort쓰면 시간초과
import sys
def sort_2751():
  n = int(input())
  nums = [int(sys.stdin.readline()) for _ in range(n)]

  nums.sort()
  for num in nums: 
    print(num)


# 10989 번 : 수 정렬하기3
import sys
def sort_10989():
  n = int(input())
  nums = [0] * 10001

  for i in range(n):
    tmp = int(sys.stdin.readline())
    nums[tmp] += 1

  for i, cnt in enumerate(nums):
    if cnt != 0:
      for _ in range(cnt):
        print(i)


# 2108 번 : 통계학
import math
import sys
from collections import Counter
def sort_2108():
  n = int(sys.stdin.readline()) #수의 갯수
  nums = [int(sys.stdin.readline()) for _ in range(n)]
  nums.sort()
  avg = round(sum(nums)/n) #1. 산술평균
  center = nums[n//2] #2. 중앙값
  cha = nums[-1] - nums[0] #4. 범위
  #3. 최빈값 구하는 식
  # freq = {}
  # for n in nums:
  #   if n in freq: continue
  #   freq[n] = nums.count(n)
  # s_freq = sorted(freq.items(), key = lambda x: (-x[1], x[0]))
  # freq_num = s_freq[0][0] #최빈값
  # if len(s_freq)!=1 and s_freq[0][1] == s_freq[1][1]: #갯수가 같은게 있다면
  #   freq_num = s_freq[1][0]
  freqs = Counter(nums).most_common()
  print(freqs)
  freq = freqs[0][0]
  if len(freqs) != 1 and freqs[0][1] == freqs[1][1]:
    freq = freqs[1][0]
  print(avg, center, freq, cha, sep='\n')



# 1427 번 : 소트인사이드
import sys
def sort_1427():
  n = sys.stdin.readline().rstrip()
  sorted_n = sorted(list(n), reverse=True)
  print(''.join(sorted_n))


# 11650 번 : 좌표 정렬하기
def sort_11650():
  n = int(sys.stdin.readline()) #좌표의 갯수
  dots = []
  for _ in range(n):
    dots.append(list(map(int, sys.stdin.readline().split())))
  s_dots = sorted(dots, key = lambda x : (x[0], x[1]))
  for x,y in s_dots:
    print(x,y)


# 11651 번 : 좌표 정렬하기2
import sys
def sort_11651():
  n = int(sys.stdin.readline())
  dots = []
  for _ in range(n):
    dots.append(list(map(int, sys.stdin.readline().split())))
  s_dots = sorted(dots, key = lambda x : (x[1], x[0]))
  for x,y in s_dots:
    print(x, y)


# 1181 번 : 단어 정렬
def sort_1181():
  n = int(input())
  words = [0] * n
  for i in range(n):
    words[i] = sys.stdin.readline().rstrip()
    
  s_words = sorted(set(words), key=lambda x:(len(x),x))
  for w in s_words:
    print(w)


# 10814 번 : 나이순 정렬
# 나이를 str 그대로 비교하면 틀리는것같다...
import sys
def sort_10814():
  n = int(sys.stdin.readline())
  people = []
  for _ in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    people.append([int(age), name])
  people.sort(key = lambda x : x[0])
  for x, y in people:
    print(x, y)