
def reverseList(head:object) -> object:
    if not head: return None
    
    vals = []
    pivot = head
    while pivot:
        vals.append(pivot)
        pivot = pivot.next
    
    vals = vals[::-1]
    head = vals[0]
    pivot = head
    for i in range(1, len(vals)):
        pivot.next = vals[i]
        pivot = pivot.next
    
    pivot.next = None
    
    return head
        


if __name__ == '__main__':
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
            
    nodo = ListNode(1)
    nodo.next = ListNode(2)
    nodo.next.next = ListNode(3)
    nodo.next.next.next = ListNode(4)
    nodo.next.next.next.next = ListNode(5)
    result = reverseList(nodo)   
    
    while result:
        print(result.val)
        result = result.next
    