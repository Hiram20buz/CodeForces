import re

def delete_consecutive_x(string):
    modified_string = list(string)
    i = 0
    while i < len(modified_string) - 2:
        if modified_string[i:i+3] == ['x', 'x', 'x']:
            modified_string.pop(i + 1)  # Delete one 'x' in the group of three consecutive 'x's
        else:
            i += 1

    return ''.join(modified_string)
    
    
n=int(input())
total=input()

print(n - len(delete_consecutive_x(total)))
