name = input('Enter your name? ')

if len(name) < 3:
    print('Name Must Be Of Atleast 3 characters')
elif len(name) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('name looks Good!!')