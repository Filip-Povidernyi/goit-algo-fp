class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next

    def search_element(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=', ')
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)

        return result

    def merge_sort(self, head=None):
        if head is None:
            head = self.head

        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)

        return sorted_list

    def sort(self, desc=False):
        if desc:
            self.head = self.merge_sort(self.head)
            self.reverse()
        else:
            self.head = self.merge_sort(self.head)

    def merge_sorted_lists(self, other):

        result = LinkedList()
        result.head = self.sorted_merge(self.head, other.head)

        return result


if __name__ == '__main__':
    llist = LinkedList()
    llist_other = LinkedList()

    llist_other.insert_at_beginning(3)
    llist_other.insert_at_beginning(12)
    llist_other.insert_at_beginning(19)
    llist_other.insert_at_end(24)
    llist_other.insert_at_end(35)

    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    print("Оригінальний список:")
    llist.print_list()

    print("\nОригінальний список 2:")
    llist.print_list()

    llist.reverse()
    print("\nПісля реверсування:")
    llist.print_list()

    llist.sort(desc=True)
    print("\nСортування за спаданням:")
    llist.print_list()

    llist.sort()
    print("\nСортування за зростанням:")
    llist.print_list()

    llist_other.sort()
    print("\nВідсортований список 2:")
    llist_other.print_list()

    merge = llist.merge_sorted_lists(llist_other)
    print("\nОб'єднаний відсортований список:")
    merge.print_list()
