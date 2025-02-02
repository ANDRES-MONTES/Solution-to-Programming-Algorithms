def getIntersectionNode(headA:object, headB: object) -> object:
         pivot_a = headA
         pivot_b = headB
         
         while pivot_a != pivot_b:
             pivot_a = pivot_a.next  if pivot_a else headB
             pivot_b = pivot_b.next  if pivot_b else headA
             
         return pivot_a
        

    
if __name__ == '__main__':
    class ListNode:
        def __init__(self, x):
             self.val = x
             self.next = None
             
             
    c = ListNode('c1')
    c.next = ListNode('c2')
    c.next.next = ListNode('c3')
    
    a = ListNode('a1')
    a.next = ListNode('a2')
    a.next.next = c
    

    b = ListNode('b1')
    b.next = ListNode('b2')
    b.next.next = ListNode('b3')
    b.next.next.next = c
    
    
    result = getIntersectionNode(a, b)
    print(result.val)
    
    
    
    
    