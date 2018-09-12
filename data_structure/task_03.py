class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ptr = []
        max = 0
        for i in s:
            if i not in ptr:
                ptr.append(i)
                max = len(ptr) if len(ptr) > max else max
            else:
                ptr = ptr[ptr.index(i)+1:]
                ptr.append(i)
        return max


def stringToString(input):
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);

            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()