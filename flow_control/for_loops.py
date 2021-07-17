
import math

print(f'pi = {math.pi:.3f}.')

for y in range(1, 11):
    print('{} '.format(y))

for b in range(1, 11):
    print('b',b)



count = 1
for a in range(1, 11):
    print(f'a', "_", count)
    count += 1

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:6d}'.format(x, x*x, x*x*x))

for c in range(1, 11, -1):
    print('c', c)

 #   message1 = 'Hello Again {} ({})'.format(name, age)

