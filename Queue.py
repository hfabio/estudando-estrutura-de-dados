# coding utf-8

class Queue:
  def __init__(self, *args):
      self.first = None
      self.last = None
      self.queue = []
      self.size = 0
      if args:
        self.first = args[0]
        for arg in args:
          self.add(arg)

  def add(self, *args):
    if args:
      self.last = args[-1]
      for value in args:
        self.queue.append(value)
        self.size += 1

  def remove(self):
    if self.size > 0:
      if len(self.queue) == 1:
        self.last = self.queue[0]
        self.first = self.queue[0]
      else:
        self.first = self.queue[1]
      self.size -= 1
      return self.queue.pop(0)
    self.last = None
    self.first = None
    self.size = 0
    return None

  def values(self):
    return self.queue

  def __str__(self):
      return 'Queue -> [{}] (size = {})'.format(', '.join([str(x) for x in self.queue]), self.size)

  def __len__(self):
      return self.size
"""
query = Queue(1, 2, 3, 4, 5, 0)
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
"""