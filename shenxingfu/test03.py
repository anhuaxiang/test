def get_list(string):
    each_check = string.split(',')
    check_list = []
    for i in each_check:
        each_list = i.split('-')
        for j in range(len(each_list)):
            each_list[j] = int(each_list[j])
        check_list.append(each_list)
    return check_list


def check(check_list):
    result = True
    ll = 0
    for i in check_list:
        if len(i) == 2:
            if i[0] > i[1]:
                result = False
                break
            for j in i:
                if not (1 <= j <= 65535):
                    result = False
                    break
            ll = ll + (i[1] - i[0])
        if len(i) == 1:
            if not (1 <= i[0] <= 65535):
                result = False
                break
            ll += 1
    print(ll)
    if result and ll < 1024:
        return 'true'
    return 'false'

if __name__ == '__main__':
    while True:
        string = input()
        print(check(get_list(string)))
