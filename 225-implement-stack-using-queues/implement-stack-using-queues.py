from collections import deque
class MyStack:

    def __init__(self):
        self.queue1=deque()
        self.queue2=deque()
    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while(len(self.queue1)>1):
            self.queue2.append(self.queue1.popleft())
        popped_element=self.queue1.popleft()    
        self.queue1,self.queue2=self.queue2,self.queue1
        return popped_element
    def top(self) -> int:
          while(len(self.queue1)>1):
            self.queue2.append(self.queue1.popleft())
          topped_element=self.queue1.popleft()
          self.queue2.append(topped_element)
          self.queue1,self.queue2=self.queue2,self.queue1
          return topped_element
    def empty(self) -> bool:
        return not self.queue1 and not self.queue2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()