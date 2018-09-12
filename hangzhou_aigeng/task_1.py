import json
import sys


def read_lines():
    for line in sys.stdin:
        yield line.strip('\n')


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    lines = read_lines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)
            line = next(lines)
            target = int(line)

            ret = twoSum(nums, target)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
