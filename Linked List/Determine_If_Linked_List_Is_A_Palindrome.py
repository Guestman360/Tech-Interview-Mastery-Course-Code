def isListPalindrome(self):
    """ Check if linked list is palindrome and return True/False."""
    node = self.head
    fast = node
    prev = None

    # prev approaches to middle of list till fast reaches end or None 
    while fast and fast.next:
        fast = fast.next.next
        temp = node.next   #reverse elemets of first half of list
        node.next = prev
        prev = node
        node = temp

    if fast:  # in case of odd num elements
        tail = node.next
    else:    # in case of even num elements
        tail = node

    while prev:
        # compare reverse element and next half elements          
        if prev.val == tail.val:
            tail = tail.next
            prev = prev.next
        else:
            return False
    return True