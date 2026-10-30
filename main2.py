scores = [3, 7, 2, 9, 4, 1, 8, 5, 6]

input('List: ' + str(scores)+ '  n = 9  Linear search - checks left to right. press enter')

target = int(input('enter a number to search for:  '))

input('searching for ' + str(target) + '.  press enter to run')
steps = 0
for score in scores:
    steps += 1
    if score == target:
        break
print('  target =', target, ' found at position', steps, ' checks =', steps)

input('compare with worst and best case. press enter to run')
mid = len(scores) // 2
print(' best: 1 check -> 0(1)  Average', mid, 'checks -> 0(n)  Worst: 9 checks -> 0(n)  Yours:', steps)

input('all 3 cases. press enter')
print('  best 0(1) average 0(n)  worst 0(n)  ->  Big-O = worst case = 0(n).')