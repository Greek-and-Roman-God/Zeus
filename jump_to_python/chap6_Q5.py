# 점프투파이썬
# 6장
# 6-5 탭을 4개의 공백으로 바꾸기

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

dot_content = tab_content.replace("~", "..")
print(dot_content)

f2 = open(dst, 'w')
f2.write(dot_content)
f2.close