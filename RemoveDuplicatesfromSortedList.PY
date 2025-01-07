# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def deleteDuplicates(head:object) -> object:
    pivot = head
    try:
        while pivot.next:
            first = pivot.val
            second = pivot.next.val
            print(first, second)
            
            if first ==second:
                pivot.next = pivot.next.next
            else:
                pivot = pivot.next
        
        return head
    
    except:
        return
            
    

        

if __name__ == '__main__':
    class Node:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    
    data = [1, 1, 2, 3]
    info = Node(data[0])
    
    for i in range(1, len(data)):
        pivot = info
        while pivot.next:
            pivot = pivot.next
        
        pivot.next = Node(data[i])
    
    
    # while info:
    #     #print(info.val)
    #     info = info.next
    
    result = deleteDuplicates(head=info)
    while result:
        print(result.val)
        result = result.next
        
    