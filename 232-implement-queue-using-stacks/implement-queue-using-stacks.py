class MyQueue:

    def __init__(self):
        # Initialize two stacks
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # Push element onto stack1
        self.stack1.append(x)

    def pop(self) -> int:
        # Transfer elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Check if stack2 is still empty
        if self.stack2:
            return self.stack2.pop()
        else:
            raise IndexError("pop from an empty queue")  # Handle case of empty queue

    def peek(self) -> int:
        # Transfer elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Check if stack2 is still empty
        if self.stack2:
            return self.stack2[-1]
        else:
            raise IndexError("peek from an empty queue")  # Handle case of empty queue

    def empty(self) -> bool:
        # Check if both stacks are empty
        return not self.stack1 and not self.stack2

# Instantiate and use the MyQueue class
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())  # Output: 1
print(obj.pop())   # Output: 1
print(obj.empty()) # Output: False
