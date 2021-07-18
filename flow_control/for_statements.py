
# Measure some strings:
words = ['cat', 'window', 'dog']
for w in words:
    print(w, len(w), '<---- The number of chars in the word')

#range with len
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

for i in range(0, 10, 3):
    print(i)


xx = sum(range(4))
print(xx, 'sum of range')
