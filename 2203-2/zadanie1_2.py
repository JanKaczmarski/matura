white_piecies = 'WSGHKP'
black_piecies = 'wsghkp'

with open('Dane_2203-2/szachy.txt', "r") as file:
    boards = []
    new_board = True
    for line in file:
        if line == '\n':
            new_board = True
            continue

        if new_board:
            boards.append([])
            new_board = False
        boards[-1].append(line[:-1])


solution = [0,64]

for board in boards:
    white_ob = []
    black_ob = []
    for row in board:
        for col in row:
            if col in white_piecies:
                white_ob.append(col)
            elif col in black_piecies:
                black_ob.append(col)
    
    if len(black_ob) == len(white_ob):
        for piece in black_ob:
            if piece.lower() in white_ob:
                white_ob.remove(piece.lower())
            else:
                continue
        if solution[1] > len(black_ob)*2:
            solution[1] = len(black_ob)*2
        solution[0] += 1


print(solution)









