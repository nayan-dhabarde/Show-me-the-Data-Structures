class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_elements = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

        self.num_of_elements += 1

    def size(self):
        return self.num_of_elements


def remove_duplicates(linked_list):
    result = LinkedList()
    node = linked_list.head

    if node is None:
        return result
    result.append(node.value)

    while node:
        if not contains(result, node.value):
            result.append(node.value)
        node = node.next

    return result


def contains(linked_list, value):
    current_node = linked_list.head
    while current_node:
        if current_node.value == value:
            return True
        current_node = current_node.next
    return False


def union(llist_1, llist_2):

    if llist_1 is None and llist_2 is None:
        return LinkedList()

    if llist_1 is None:
        return llist_2

    if llist_2 is None:
        return llist_2

    llist_3 = LinkedList()

    current_node = llist_1.head

    # Fill from first
    while current_node is not None:
        llist_3.append(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head

    # Fill from second
    while current_node is not None:
        llist_3.append(current_node.value)
        current_node = current_node.next

    # Remove duplicates
    return remove_duplicates(llist_3)

def intersection(llist_1, llist_2):

    if llist_1 is None or llist_2 is None:
        return LinkedList()

    llist_3 = LinkedList()

    current_node_1 = llist_1.head

    while current_node_1 is not None:

        current_node_2 = llist_2.head
        while current_node_2 is not None:
            if current_node_1.value == current_node_2.value:
                llist_3.append(current_node_1.value)
                break
            current_node_2 = current_node_2.next

        current_node_1 = current_node_1.next

    return remove_duplicates(llist_3)
    pass


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# returns 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11

print (intersection(linked_list_1,linked_list_2))
# returns 4 -> 6 -> 21


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# returns 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21

print (intersection(linked_list_3,linked_list_4))
# returns Nothing as there are no intersections

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# returns Nothing as both arrays are empty

print (intersection(linked_list_3,linked_list_4))
# returns Nothing as both arrays are empty

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# returns 1 -> 7 -> 8 -> 9 -> 11 -> 21

print (intersection(linked_list_3,linked_list_4))
# returns Nothing as both arrays are empty
