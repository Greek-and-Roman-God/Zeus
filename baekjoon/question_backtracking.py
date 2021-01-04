# 백준 백트래킹 단계
# https://www.acmicpc.net/step/34


# 15649 번 : N과 M (1)
import itertools
def backtracking_15649():
  n, m = map(int, input().split())

  prod_nums = list(itertools.permutations(range(1, n+1), m))
  for prod in prod_nums:
    print(" ".join(str(p) for p in prod))
