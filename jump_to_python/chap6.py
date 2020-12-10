#6-2) 3과 5의 배수 합하기
def hap_multiples():
  ans = 0
  for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
      ans += i
  print(ans)


#6-3) 게시판 페이징하기
def getTotalPage(m,n):
  if m % n == 0:
    pages = m // n
  else :
    pages = m // n + 1
  
  return pages

