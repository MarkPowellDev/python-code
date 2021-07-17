number = 17
green = True
red = False

if number <= 15:
    if green is False:
        if red is True:
            print('Go')
        else:
            print('red is wrong, green is right')
    else:
        print('red is wrong, green is wrong')
else:
    print('red is wrong, green is wrong, number is less than 17')
