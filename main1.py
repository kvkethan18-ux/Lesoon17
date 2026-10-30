n = int(input('Enter any n try(5, 10, or 50): '))

input('One loop runs per item. enter to run')
for i in range(n):
    pass
print('  n =', n, 'steps =', n, '  -> 0(n) linAR time')

input('two nested loops - run n x n timess. Press enter to run')
for i in range(n):
    for j in range(n):
        pass
print('  n =', n, 'steps =', n, '  -> 0(n^2) quadratic time')

input('Rule: count the loops. press enter')
print('  0 loops -> 0(1) 1 loop -> 0(n) 2 nested -> 0(n^2)')