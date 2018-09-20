import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        if not head.next:
            return None
        next_node = head
        length = 1
        while next_node.next:
            length += 1
            next_node = next_node.next
        if length == n:
            return head.next
        next_node = head
        index = 1
        while index < (length - n):
            next_node = next_node.next
            index += 1
        next_node.next = next_node.next.next
        return head

    def removeNthFromEnd_1(self, head, n):
        if not head.next:
            return None
        first = head
        second = head
        for i in range(n):
            first = first.next
        if not first:
            return head.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            line = next(lines)
            n = int(line)

            ret = Solution().removeNthFromEnd_1(head, n)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()