string_a = input()

def is_palindrome(string):
    string_reverse = string[-1::-1]
    if string == string_reverse:
        print('Yes')
    else:
        print('No')

is_palindrome(string_a)