class Node:
    def __init__(self,data):
        self.next = None 
        self.data = data 
        self.prev = None

class DoublyLinkedLists:
    def __init__(self, data):
        self.head = None
        self.data = data 

    def add_at_beginning(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return 

        new_node.next = self.head 
        self.head.prev = new_node
        self.head = new_node 

    def add_at_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return  
        
        tmp = self.head 

        while tmp.next:
            tmp = tmp.next 

        tmp.next = new_node 
        new_node.prev = tmp 


    def insert_at_point(self, data, position):

        new_node = Node(data)
        count = 0 

        if self.head is None:
            self.head = new_node
            return 
        
        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        tmp = self.head 

        while tmp is not None and count < position - 1:
            tmp = tmp.next 
            count += 1

        if tmp is None:
            raise IndexError("Position out of bounds")
        
        new_node.next = tmp.next
        new_node.prev = tmp 
        tmp.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def remove_at_beginning(self):

        if self.head is None:
            return None 

        removed_node = self.head 
        self.head = self.head.next

        if self.head is not None:  # If there's a new head, update its prev pointer
            self.head.prev = None  

        removed_node.next = None  # Disconnect the removed node
        return removed_node.data  # Return the removed data


    def remove_at_end(self):

        if self.head is None:
            return None 
        
        tmp = self.head 

        if tmp.next is None:  # Only one node in list
            removed_node = tmp
            self.head = None
            return removed_node.data


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

        while tmp is not None and count < position - 1:
            tmp = tmp.next
            count += 1

        if tmp is None or tmp.next is None:
            return None
        
        removed_node = tmp.next  # Node to be removed
        tmp.next = removed_node.next  # Bypass the removed node

        if removed_node.next is not None:  # Only update prev if not the last node
            removed_node.next.prev = tmp  

        removed_node.next = None  # Disconnect removed node
        removed_node.prev = None  

        return removed_node.data 
        

    def traversal(self, direction=0):  # 0 = Forward, 1 = Backward
        if self.head is None:  # Handle empty list case
            print("List is empty")
            return

        if direction == 1:  # Backward Traversal
            tmp = self.head
            while tmp.next is not None:  # Move to last node
                tmp = tmp.next
            
            while tmp is not None:  # Traverse backwards
                print(tmp.data, end=" <= ")
                tmp = tmp.prev

        else:  # Forward Traversal (default)
            tmp = self.head
            while tmp is not None:
                print(tmp.data, end=" >= ")
                tmp = tmp.next

        print("None")  # Indicate the end of the list


