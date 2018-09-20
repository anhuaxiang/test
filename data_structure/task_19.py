import itertools


def gen_1(n):
    def generate(a=[]):
        if len(a) == 2 * n:
            if valid(a):
                ans.append(''.join(a))
        else:
            a.append('(')
            generate(a)
            a.pop()
            a.append(')')
            generate(a)
            a.pop()

    def valid(a):
        bal = 0
        for c in a:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return bal == 0
    ans = []
    generate()
    return ans


def gen_2(n):
    def valid(a):
        bal = 0
        for c in a:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return bal == 0

    result = []
    combinations_list = itertools.product(['(', ')'], repeat=2*n)
    for each in combinations_list:
        if valid(list(each)) and ''.join(list(each)) not in result:
            result.append(''.join(list(each)))
    return result


def gen_3(n):
    result = []

    def backtrack(s='', left=0, right=0):
        if len(s) == 2*n:
            result.append(s)
            return
        if left < n:
            backtrack(s+'(', left+1, right)
        if right < left:
            backtrack(s+')', left, right+1)
    backtrack()
    return result

if __name__ == '__main__':
    # print(gen_1(6))
    # print(gen_2(6))
    print(gen_3(3))