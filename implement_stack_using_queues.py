class MyStack:
   
    
    def __init__(self):
        self.data = []
        
    def push(self, x: int) -> None:
        self.data.append(x)
        return

    def pop(self) -> int:
        val = self.data.pop()
        return val
    
    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:        
        return len(self.data) > 0


# Your MyStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyStack()
    val = obj.empty()
    print(val)
   
   
    