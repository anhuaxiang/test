
a = [[1, 3, 5, 9], [8, 1, 3, 4], [5, 0, 6, 1], [8, 8, 4, 0]]


def minSum(list1):
    l1 = len(list1)
    if l1 < 2:
        return list1
    list2 = list1
    for i in range(1, l1):
        list2[0][i] = list1[0][i - 1] + list1[0][i]
        list2[i][0] = list1[i - 1][0] + list1[i][0]
    for i in range(1, l1):
        for j in range(1, l1):
            sum1 = list2[i][j - 1] + list1[i][j]
            sum2 = list2[i - 1][j] + list1[i][j]
            if sum1 < sum2:
                list2[i][j] = sum1
            else:
                list2[i][j] = sum2
    return list2[l1 - 1][l1 - 1]

if __name__ == '__main__':
    input_list = []
    for i in range(4):
        a = []
        for j in range(4):
            x = input()
            a.append(int(x))
        input_list.append(a)
print(minSum(input_list))
