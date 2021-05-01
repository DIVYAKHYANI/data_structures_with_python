

def deleteNode(head, position):
    current = head
    # next will point to None if there is 
    # not another item in the list
    if position == 0:
        head = head.next
    else:
        # iterate to the right node
        for i in range(position-1):
            current = current.next
        # and alter the next pointer
        current.next = current.next.next
    return head