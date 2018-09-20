class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_dict = {'[': ']', '{': '}', '(': ')'}
        s_list = []
        for each in s:
            if s_list and s_dict.get(s_list[-1]) == each:
                s_list.pop(-1)
            else:
                s_list.append(each)
        return not bool(s_list)


def stringToString(input):
    return str(input)


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
            s = stringToString(line)

            ret = Solution().isValid(s)

            out = ret
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()