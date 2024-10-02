# Завдання 2
from collections import deque as dq

def is_palindrome(string):
    cleaned_string = string.replace(' ', '').lower()

    dq_string = dq(cleaned_string)

    if not dq_string:
        return False
    if len(dq_string) % 2 != 0:
        center = len(dq_string) // 2
        dq_string.remove(cleaned_string[center])

    while len(dq_string) > 1:
        if dq_string.popleft() != dq_string.pop():
            return False
    return True

def main():
    """
    It asks user for the string and checks if it is a palindrome or not.
    """
    input_string = input('Input a string: ')
    if is_palindrome(input_string):
        print(f'The string << {input_string} >> is a palindrome')
    else:
        print(f'The string << {input_string} >> is not a palindrome')

if __name__ == '__main__':
    main()
