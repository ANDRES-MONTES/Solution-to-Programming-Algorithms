def removeElements(head:object, val: int) -> object:
    nodos = []
    pivot = head
    while pivot:
        if pivot.val != val:
            nodos.append(pivot)
        
        pivot = pivot.next
    
    if len(nodos):
        head_2 = nodos[0]
        pivot = head_2
        
        for i in range(1, len(nodos)):
            pivot.next = nodos[i]        
            pivot = pivot.next
            
        pivot.next = None
        return head_2
    else:
        return None
            
            
        


if __name__ == '__main__': 
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next     
        
        def __str__(self):
            return f'{self.val}'
            
    head = ListNode(1)  
    head.next = ListNode(2)  
    head.next.next = ListNode(6)  
    head.next.next.next = ListNode(3)  
    head.next.next.next.next = ListNode(4)  
    head.next.next.next.next.next = ListNode(5)  
    head.next.next.next.next.next.next = ListNode(6)  
    val = 6
    result = removeElements(head, val)
    