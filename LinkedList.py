class LinkedNode:
  def __init__(self, value=None, nextNode=None):
      self.data = value
      self.nextNode = nextNode

  def setNextNode(self, node=None):
    self.nextNode = node
  
  def removeNextNode(self):
    self.nextNode = None
  
  def next(self):
    return self.nextNode
  
  def getData(self):
    return self.data

  def setData(self, value):
    self.data = value
    return True
  
  def __str__(self):
      return 'Node data -> {}'.format(str(self.data))

class LinkedList:
  def __init__(self, *args):
      if args:
        self.root = LinkedNode(args[0])
        self.size = 1
        for value in args[1:]:
          self.add(value)
      else:
        self.size = 0
        self.root = LinkedNode()
  
  def add(self, value):
    tmp = self.root
    if tmp:
      while tmp.next() is not None:
        tmp = tmp.next()
      tmp.nextNode = LinkedNode(value)
    else:
      self.root = LinkedNode(value)
    self.size += 1
  
  def remove(self, value):
    if self.root.getData() == value:
      if self.root.next():
        self.root = self.root.next()
      else:
        self.root = None
      self.size -= 1
      return True
    before = self.root
    tmp = before.next()
    while tmp.next() is not None and tmp.getData() != value:
      before = tmp
      tmp = tmp.next()
    if tmp.getData() == value:
      self.size -= 1
      if tmp.next() == None:
        before.removeNextNode()
      else:
        before.setNextNode(tmp.next())
      return True
    else:
      return False

  def find(self, index):
    if index == 0:
      return self.root.getData()
    else:
      tmp = self.root
      count = 0
      while tmp and count < index:
        tmp = tmp.next()
        count += 1
      if tmp:
        return tmp.getData()
      else:
        return None

  def values(self):
    values = []
    tmp = self.root
    while tmp:
      values.append(tmp.getData())
      tmp = tmp.next()
    return values

  def __str__(self):
      values = [str(x) for x in self.values()]
      return 'LinkedList -> [{}] (size = {})'.format(', '.join(values), self.size)
  
  def __len__(self):
      return self.size

"""
list = LinkedList(1,2,3,4,5,9,8,7,6)
print(list)
for i in range(0,10):
  print(f'searching index {i}', list.find(i))
print(list.values())
print(list)
list.remove(3)
print(list)
list.remove(4)
print(list)
list.remove(2)
print(list)
list.remove(1)
print(list)
list.remove(5)
print(list)
list.remove(9)
print(list)
list.remove(8)
print(list)
list.remove(7)
print(list)
list.remove(6)
print(list)
list.add(25)
print(list)
"""