# coding utf-8

class Stack:
  def __init__(self, *args):
      self.first = None
      self.last = None
      self.stack = []
      self.size = 0
      if args:
        self.first = args[0]
        for arg in args:
          self.add(arg)

  def add(self, *args):
    self.first = args[-1]
    for value in args:
      self.stack.append(value)
      self.size += 1

  def remove(self):
    if self.size > 0:
      if len(self.stack) == 1:
        self.last = self.stack[-1]
        self.first = self.stack[-1]
      else:
        self.last = self.stack[-2]
      tmp = self.stack.pop(-1)
      self.size -= 1
      return tmp
    self.last = None
    self.first = None
    self.size = 0
    return None

  def __str__(self):
      return 'Stack -> [{}] (size = {})'.format(', '.join([str(x) for x in self.stack]), self.size)

  def __len__(self):
      return self.size

query = Stack(1, 2, 3, 4, 5, 0)
query.add(1,2)
print(query.first)
print(query.last)
print(query.size)
print(query)
print('-'*5)
print(query.remove())
print('-'*5)
print(query.first)
print(query.last)
print(query.size)
print(query)
for i in range(0,10):
  print(query.remove())
  print(query)
print(query.first)
print(query.last)
print(query.size)
print(query)
