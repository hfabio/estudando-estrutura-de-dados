NONETYPE='root'
from Queue import Queue
from random import sample, seed

class TreeNode:
  def __init__(self, value=None, nodeLeft=None, nodeRight=None):
      self.data = value
      self.nodeLeft = nodeLeft
      self.nodeRight = nodeRight
  
  def getData(self):
    return self.data
  
  def setData(self,value):
    self.data = value
    return True

  def getLeft(self):
    return self.nodeLeft

  def getRight(self):
    return self.nodeRight

  def setLeft(self, node=None):
    self.nodeLeft = node
    return True

  def setRight(self, node=None):
    self.nodeRight = node
    return True

  def __str__(self):
    if self.nodeLeft or self.nodeRight:
      tmp = Tree(root=self)
      return tmp.print()
    return f'Node value -> {self.data}'

class Tree:
  def __init__(self, *args, root=None):
    self.root = root
    self.size = 0
    if args:
      for value in args:
        self.add(value)

  def add(self, value, start=None):
    if start is None:
      if self.root is None:
        self.root = TreeNode(value)
        self.size += 1
      else:
        self.add(value, self.root)
    elif start:
      if value > start.getData():
        if start.getRight():
          self.add(value, start.getRight())
        else:
          start.setRight(TreeNode(value))
          self.size += 1
      elif value < start.getData():
        if start.getLeft():
          self.add(value, start.getLeft())
        else:
          start.setLeft(TreeNode(value))
          self.size += 1
    
  def __PreOrder(self, subtree=None):
    data = []
    if subtree is None:
      if self.root is None:
        return data
      subtree = self.root
    if subtree.getLeft():
      data = [*data, *(self.__PreOrder(subtree.getLeft()))]
    data.append(subtree)
    if subtree.getRight():
      data = [*data, *(self.__PreOrder(subtree.getRight()))]
    return data #[str(x) for x in data]

  def __PostOrder(self, subtree=None):
    data = []
    if subtree is None:
      if self.root is None:
        return data
      subtree = self.root
    if subtree.getRight():
      data = [*data, *(self.__PostOrder(subtree.getRight()))]
    data.append(subtree)
    if subtree.getLeft():
      data = [*data, *(self.__PostOrder(subtree.getLeft()))]
    return data #[str(x) for x in data]
  
  def __Order(self, subtree=None):
    data = []
    queue = Queue()
    if subtree is None:
      if self.root is None:
        return Queue.values()
      subtree = self.root
    queue.add(subtree)
    while len(queue):
      node = queue.remove()
      data.append(node)
      if node.getLeft():
        queue.add(node.getLeft())
      if node.getRight():
        queue.add(node.getRight())
    return data #[str(x) for x in data]

  def getPreOrder(self, tree=None):
    return [x.getData() for x in self.__PreOrder(tree)]

  def getPostOrder(self, tree=None):
    return [x.getData() for x in self.__PostOrder(tree)]

  def getOrder(self, tree=None):
    return [x.getData() for x in self.__Order(tree)]

  def find(self, value):
    if self.root is None:
      return None
    if self.root.getData() == value:
      return self.root
    else:
      node = self.root
      while node is not None and node.getData() != value:
        if value > node.getData():
          node = node.getRight()
        else:
          node = node.getLeft()
      return node

  def __str__(self):
      # return 'Order tree: {}'.format(self.getOrder())
      return str(self.getOrder())
  
  def print(self, subtree=None):
      # return 'Order tree: {}'.format(self.getOrder(subtree))
      return str(self.getOrder(subtree))

"""
          25
        /   \
      3       92
    /   \     /
  1       5   54
            \
              6

Pre-order -> 1, 3, 5, 6, 25, 54, 92
Order -> 25, 3, 92, 1, 5, 54, 6
Post-order -> 92, 54, 25, 6, 5, 3, 1
"""

"""
# tree = Tree(25,3,1,92,54,5,6)
# tree = Tree(61,89,66,43,51,16,55,11,79,77,82,32)
tree = Tree()
seed(10)
values = sample(range(1,100), 20)
for i in values:
  tree.add(i)

print('-'*5)
print('Pre-order  ',tree.getPreOrder())
print('Order      ',tree.getOrder())
print('Post-order ',tree.getPostOrder())
print('-'*5)
print('Print tree: ', tree)
print('-'*5)
print('Print tree find (66)',tree.find(66))
"""