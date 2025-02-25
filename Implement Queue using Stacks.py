class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)
        

    def pop(self) -> int:
        return self.data.pop(0)
        

    def peek(self) -> int:
        return self.data[0]
        

    def empty(self) -> bool:
        if len(self.data):
            return False
        else:
            return True
        


x = 2
obj = MyQueue()
obj.push(x)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_4)