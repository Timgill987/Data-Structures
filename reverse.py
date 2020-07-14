def reverse_ll(ll)
    """Recieve a linkedlist as an input and returns a reversed order ll"""
"""

    Steps:
    1. Each node needs to point at the prev_node
    2. head and tail pointers need to be flipped

    reverse_ll(LinkedList())
    return the empty list

    Cases:
    1. If the linkedlist is empty return the original that is passed in


    reverse_ll()
    """
    #if LL is empty, return

    if ll.head is None:
        return ll

    #if ll has one node
    if ll.head is ll.tail:
        return ll

    #if ll has more than one node
        current = ;;/head
        previous = None
        next_node = None
        while current is not None:
            # store a pointer to the current next value
            next_node = current.get_next()

            # switch current's next pointer to the previous
            current.set_next(previous)

            #increment logic
            previous = next_node
            current = next_node
