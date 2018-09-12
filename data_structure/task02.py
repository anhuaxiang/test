import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        ptr = 0
        while l1 and l2:
            if l1.val + l2.val + ptr > 9:
                result.append(l1.val + l2.val + ptr - 10)
                ptr = 1
            else:
                result.append(l1.val + l2.val + ptr)
                ptr = 0
            l1 = l1.next
            l2 = l2.next
        while l1:
            if l1.val + ptr > 9:
                result.append(l1.val + ptr - 10)
                ptr = 1
            else:
                result.append(l1.val + ptr)
                ptr = 0
            l1 = l1.next
        while l2:
            if l2.val + ptr > 9:
                result.append(l2.val + ptr - 10)
                ptr = 1
            else:
                result.append(l2.val + ptr)
                ptr = 0
            l2 = l2.next
        if ptr == 1:
            result.append(1)
        return stringToListNode(str(result))


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
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line)
            line = next(lines)
            l2 = stringToListNode(line)
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()