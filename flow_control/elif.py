
x = int(input("Please enter a positive integer: "))

if x < 0:
    x = 0
    print('Not positive')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Thank You for entering a positive interger ->', x)
else:
    print('next')