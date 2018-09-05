class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


def find_loop(head):
    slow_p = head
    fast_p = head
    loop_exit = False
    if not head:
        return False
    while fast_p.next is not None and fast_p.next.next is not None:
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            loop_exit = True
            print('存在环结构')
            break
    if loop_exit:
        slow_p = head
        while slow_p != fast_p:
            fast_p = fast_p.next
            slow_p = slow_p.next
        return slow_p


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    print(find_loop(node1).item)