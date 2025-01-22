def hasCycle(head:object) -> bool:
    if not head or not head.next:
        return False
    
    address = {}
    pivot = head
    while pivot:
        print(address)
        if id(pivot) in address:
            return True
        
        address.add(id(pivot))
        pivot = pivot.next

    return False
        

if __name__ == '__main__':
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
            
    node = ListNode(3)
    node.next = ListNode(2)
    node.next.next = ListNode(0)
    node.next.next.next = ListNode(-4)
    node.next.next.next.next = node.next
    
    
    result = hasCycle(ListNode(9))
    print(result)