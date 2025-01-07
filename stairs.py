def climbStairs(n: int) -> int:
   if n <= 2:
       return n
   
   info = [0] * (n + 1)
   info[1] = 1
   info[2] = 2
   
   for i in range(3, n + 1):
       info[i] = info[i-1] + info[i-2]
   
   return info[-1]
   
   
if __name__ == '__main__':
    data = climbStairs(10)
    print(data)
