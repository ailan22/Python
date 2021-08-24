print(' '*10, end='')
for i in range(0, 10):
    print (f'{i:^4d}', end='')
print(' ')
print(' '*3, '-'*(45))
for x in range(0, 10):
    print(f'{x:>7d}:', end='')
    for y in range(0, 10):
        mul = x * y
        print(f'{mul:>4d}', end='')
    print('')