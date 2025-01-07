def mergeTwoLists(list1:object, list2:object) -> list:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
        
    if list1 == None and list2 == None:
        return None
    
    data = [list1, list2]
    info = []
    for i in range(len(data)):
        while data[i]:
            info.append(data[i].val)
            data[i] = data[i].next
            
    info.sort()
    head = ListNode(info[0])
    nodo = head
    for i in range(1, len(info)):
        nodo.next = ListNode(info[i])
        nodo = nodo.next
        
    return head
    

if __name__ == '__main__':
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
            
        def add(self, *value):
            current = self
            for i in range(len(value)):
                while current.next:
                    current = current.next 
                current.next = ListNode(value[i])
            
        def info(self):
            info = []
            current = self
            while current:
                info.append(current.val)
                current = current.next
            print(info)
        
        
    a = ListNode(1)  #[1,2,4]
    a.add(*[2, 4, 5, 6])
    a.info()
    
    b = ListNode(1)   #[1,3,4]
    b.add(*[3, 4, 7, 8])
    b.info()
        
        
    print('----------------------------')
    result = mergeTwoLists(a, b)
    print(result)
    while result:
        print(result.val)
        result = result.next
    
        