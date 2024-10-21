class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class MyLinkedList:

    def __init__(self, head=None):
        self.head = head
        self.length = 1 if self.head else 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        curr = self.head

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr:
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)

        self.length += 1


    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            curr = self.head

            while curr.next:
                curr = curr.next

            curr.next = Node(val, None)

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        elif index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            prev = None
            curr = self.head
            while index > 0:
                prev = curr
                curr = prev.next
                index -= 1

            prev.next = Node(val, curr)
            self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            prev = None
            curr = self.head

            while index > 0:
                prev = curr
                curr = curr.next
                index -= 1

            if curr.next == None:
                prev.next = None
            else:
                prev.next = curr.next

            self.length -= 1


    def print_list(self):
        current_node = self.head
        if not current_node:
            print("The linked list is empty.")
            return

        while current_node:
            print(f"{current_node.val} -> ", end="")
            current_node = current_node.next
        print("None")  # End of the linked list


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)