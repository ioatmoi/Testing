class Stack:
  def __init__(self, data = None):
    if data == None:
      self.stack = list()
    elif isinstance(data, list):
      self.stack = data
    else:
      raise ValueError('input data should be list')
    return

  def __iter__(self):
    return iter(self.stack)

  def push(self, data):
    self.stack.append(data)
    return

  def pop(self):
    return self.stack.pop()

  def size(self):
    return self.stack.__len__()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.size())