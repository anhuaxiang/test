def letter_com(digits):
    di = {'2': 'abc', '3': 'def', '4': 'ghi',
          '5': 'jkl', '6': 'mno', '7': 'pqrs',
          '8': 'tuv', '9': 'wxyz'}
    char_list = []
    for char in digits:
        char_list.append(di[char])

