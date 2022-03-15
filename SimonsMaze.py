adj = []
s = ['+++++++++++++++++++++++',
     'S     +      +        +',
     '+ +++ + ++++ + ++++++ +',
     '+ +   +    +   + +    +',
     '+ ++++++++ +++ + + ++++',
     '+    +   +   +   + + ++',
     '++++ + +++ + +++++ +  +',
     '+      +   +    +     +',
     '+ ++++++ + ++++++ +++++',
     '+        +    +       +',
     '+++++++++++++++++++++F+']

for t in s:
    adj.append(list(t))

print(adj)
col = len(adj[0])
row = len(adj)
print('Row = %d' % row)
print('Column = %d' % col)

queue = []


def stringify(i, j):
    s = ''
    s = s + str(i) + '-' + str(j)
    return s


def maze():
    i = 0
    while i < len(adj):
        for j in range(len(adj[i])):
            print(adj[i][j], end=" ")
        print()
        i += 1


def maze_solver(i, j):
    maze()
    print()
    print()
    # print('Remaining Path Options => %s' % queue)
    adj[i][j] = '.'
    count = 0
    record = []
    if adj[i + 1][j] == ' ':
        count += 1
        record.append(stringify(i + 1, j))

    if adj[i - 1][j] == ' ':
        count += 1
        record.append(stringify(i - 1, j))

    if adj[i][j + 1] == ' ':
        count += 1
        record.append(stringify(i, j + 1))

    if adj[i][j - 1] == ' ':
        count += 1
        record.append(stringify(i, j - 1))

    if adj[i + 1][j] == 'F':
        adj[i + 1][j] = 'X'
        maze()
        print('We Have Reached in Our Destination (%d, %d)' % (i + 1, j))
        quit()

    if adj[i - 1][j] == 'F':
        adj[i - 1][j] = 'X'
        maze()
        print('We Have Reached in Our Destination (%d, %d)' % (i - 1, j))
        quit()

    if adj[i][j + 1] == 'F':
        adj[i][j + 1] = 'X'
        maze()
        print('We Have Reached in Our Destination (%d, %d)' % (i, j + 1))
        quit()

    if adj[i][j - 1] == 'F':
        adj[i][j - 1] = 'X'
        maze()
        print('We Have Reached in Our Destination (%d, %d)' % (i, j - 1))
        quit()

    if count == 1:
        l = record[0].split('-')
        r, s = (int(l[0]), int(l[1]))
        maze_solver(r, s)

    if count > 1:
        queue.extend(record)
        l = queue.pop(0).split('-')
        r, s = (int(l[0]), int(l[1]))
        maze_solver(r, s)

    else:
        l = queue.pop(0).split('-')
        r, s = (int(l[0]), int(l[1]))
        maze_solver(r, s)


print('Initial Stage')
p = 0
while p < len(adj):
    for q in range(len(adj[p])):
        if adj[p][q] == 'S':
            print('Fun Begins at (%d, %d)' % (p, q))
            maze_solver(p, q)
        else:
            pass

    p += 1
