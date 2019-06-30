# Reverses the linked list in groups of size k 
# and returns the pointer to the new head node. 
def reverse(self, k = 1): 
    if self.head is None: 
        return

    curr = self.head 
    prev = None
    new_stack = [] 
    while curr is not None: 
        val = 0
            
        # Terminate the loop whichever comes first 
        # either current == None or value >= k 
        while curr is not None and val < k: 
            new_stack.append(curr.data) 
            curr = curr.next
            val += 1

        # Now pop the elements of stack one by one 
        while new_stack: 
                
            # If final list has not been started yet. 
            if prev is None: 
                prev = Node(new_stack.pop()) 
                self.head = prev 
            else: 
                prev.next = Node(new_stack.pop()) 
                prev = prev.next
                    
    # Next of last element will point to None. 
    prev.next = None
    return self.head