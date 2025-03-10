class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node 
        
        new_node.next = self.head 
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        tmp = self.head 

        if self.head is None:
            self.head = new_node
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        count = 0
        tmp = self.head

        while tmp is not None and count < position - 1:
            tmp = tmp.next
            count += 1

        if tmp is None:
            raise IndexError("Position out of bounds")

        new_node.next = tmp.next
        tmp.next = new_node

    def remove_at_beginning(self):
        if self.head is None:
            return None 
        
        removed_node = self.head
        self.head = self.head.next 
        removed_node.next = None

        return removed_node.data
    
    def remove_at_end(self):
        if self.head is None:
            return None

        if self.head.next is None:
            removed_node = self.head
            self.head = None
            return removed_node.data

        tmp = self.head
        while tmp.next and tmp.next.next:
            tmp = tmp.next

        removed_node = tmp.next
        tmp.next = None

        return removed_node.data
    
    def remove_at_position(self, position):
        if self.head is None:
            return None

        if position == 0:
            removed_node = self.head
            self.head = self.head.next
            removed_node.next = None
            return removed_node.data

        tmp = self.head
        count = 0
        
        while tmp is not None and tmp.next is not None and count < position - 1:
            tmp = tmp.next
            count += 1

        if tmp is None or tmp.next is None:
            return None

        removed_node = tmp.next
        tmp.next = tmp.next.next
        removed_node.next = None
        
        return removed_node.data

    def traversal(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=' => ' if tmp.next else '')
            tmp = tmp.next

    def recursive_reversal(self, node):
        if node is None or node.next is None:
            return node 
        
        reversed_list_head = self.recursive_reversal(node.next)

        node.next.next = node
        node.next = None

        return reversed_list_head 

    def reverse(self):
        self.head = self.recursive_reversal(self.head)

    def palindrome(self):
        if self.head is None or self.head.next is None:
            return True 
        
        slow = self.head 
        fast = self.head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        prev = None 
        current = slow

        while current:
            next_node = current.next 
            current.next = prev 
            prev = current 
            current = next_node

        first_half = self.head
        second_half = prev 

        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next 
            second_half = second_half.next

        return True
    
    def detect_cycle(self):
        slow = self.head 
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast:
                return True 
        
        return False
