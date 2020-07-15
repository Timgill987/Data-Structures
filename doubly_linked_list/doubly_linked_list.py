"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #create instance of ListNode with Value
        new_node = ListNode(value, None)
        #increment the DLL length attribute
        self.length +=1

        #check if the dll is empty
        if not self.head:
            #if it is empty
                #set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
            #if not empty
        else:
                # set head's prev to the new node
                # set new node's next to current head
                # set head to the new node
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
                self.head.prev = None
        pass

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value if self.head is not None else None
        self.delete(self.head)
        return value
    # store the value of the head
    #     self.length -=1
    #     current = self.head

    # # decrement the length of the DLL
    #     #if head.next is not None
    #     if self.head.next is not None:
    #         # set head.next's prev to None
    #         #set head to head.next
    #         self.head = self.head.next
    #         self.head.prev = None
    #     # else (if head.next is None)
    #     else:
    #         # set head to None
    #         # set tail to None
    #         self.head = None
    #         self.tail = None
    # delete the head

    # return the value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value, None)
        # increment the DLL length attribute
        self.length +=1
        # if DLL is empty
        if not self.tail:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        #if DLL is not empty
        else:
            # set new node's prev to current tail
            # set tail's next to new node
            # set tail to the new node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        pass

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the head
        value = self.tail.value if self.tail is not None else None
        self.delete(self.tail)
        return value
    # decrement the length of the DLL

    #     # if tail.prev is not None
    #     if self.tail.prev is not None:
    #         # set tail.prev's next to None
    #         # set tail to tail.prev
    #         self.tail = self.tail.prev
    #         self.tail.next = None
    #     # else (if tail.prev is None)
    #     else:
    #         self.head = None
    #         self.tail = None
    #         # set head to None
    #         # set tail to None

    #     del current
    # # return the value
    # # delete the tail

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):

        if node.prev is not None:
            node.prev.next = node.next
        node.next = node.prev
        node.next = self.head #instead of deleting the node, we're reassigning it to the head
        self.head.prev = node
        node.prev = None
        self.head = node

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = node.value
        if self.tail == node:
            return
        if self.head == node:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            node.delete()
            self.length -= 1
            self.add_to_tail(value)

        # if node.next is not None:
        #     node.next.prev = node.prev
        # node.prev = node.next
        # self.tail.next = node
        # node.next = None
        # self.tail = node

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None # do nothing
            return
        if node.prev is not None:
            node.prev.next = node.next # deleting from left to right
        else:
            self.head = node.next
            self.head.prev = None
        if node.next is not None:
            node.next.prev = node.prev # deleting from right to left
        else:
            self.tail = node.prev #deleting from the tail
            self.tail.next = None
        del node
        pass

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
