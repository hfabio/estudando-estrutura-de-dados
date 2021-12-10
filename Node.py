class Node:
  def __init__(self, data=None):
      self.data = data
  
  def getData(self):
    return self.data

  def setData(self, value):
    self.data = value
    return True
  
  def __str__(self):
      return 'Node data -> {}'.format(str(self.data))

"""
node = Node()
print(node)
node.setData(25)
print(node)
"""