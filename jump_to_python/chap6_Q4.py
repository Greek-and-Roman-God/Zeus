# 점프투파이썬
# 6장
# 6-4 간단한 메모장 만들기

import sys

option = sys.argv[1]

# print(option)
# print(memo)

if option == '-a':
  memo = sys.argv[2]
  f = open('memo1.txt', 'a')
  f.write(memo)
  f.write('\n')
  f.close()

if option == '-v':
  f = open('memo1.txt')
  read_memo = f.read()
  f.close()
  print(read_memo)