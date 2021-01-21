'''
크로아티아 알파벳
'''

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

data = input()
i = 0
char = 0

while i < len(data):

    if data[i:i+3] in alpha:
        i += 3
    elif data[i:i+2] in alpha:
        i += 2
    else:
        i += 1
    char += 1

print(char)
    
    