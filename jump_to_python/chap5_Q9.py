import sys

numbers = sys.argv[1:]
result = 0
for n in numbers:
  result += int(n)
print(result)