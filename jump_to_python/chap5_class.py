class FourCal:
  # def setData(self, input1, input2):
  #   self.num1 = input1
  #   self.num2 = input2
  #   print(self.num1, self.num2)
  def __init__(self, input1, input2):
    self.num1 = input1
    self.num2 = input2
    print(self.num1, self.num2)

  def add(self):
    print('합 :', self.num1+self.num2)
  def sub(self):
    print('차 :', self.num1-self.num2)
  def prod(self):
    print('곱 :', self.num1*self.num2)
  def div(self):
    print('나누기 :', self.num1/self.num2)

# a = FourCal()
# a.setData(10,2)


# b = FourCal()
# b.setData(12,4)
# b = FourCal(12, 4)
# b.add()
# b.sub()
# b.prod()
# b.div()

class MoreFourCal(FourCal): #상속
  def pow(self):
    print('제곱 :', self.num1 ** self.num2)

# c = MoreFourCal(3, 2)
# c.add()
# c.sub()
# c.prod()
# c.div()
# c.pow()

class safeFourCal(FourCal):
  def div(self): #오버라이딩
    if self.num2 == 0:
      print('0으로 나누는 것은 불가능합니다...', 0)
    else:
      print('나누기 :', self.num1/self.num2)

# d = safeFourCal(4, 0)
# d.add()
# d.sub()
# d.prod()
# d.div()
