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


solution = [0, 0]
for board in boards:
    empty_cols = 0
    columns = {i: '' for i in range(8)}
    for row_id, row in enumerate(board):
        for col_id, col in enumerate(row):
            if col != '.':
                columns[col_id] += col
    
    for column in columns.values():
        if column == '':
            empty_cols += 1

    if empty_cols > solution[1]:
        solution[1] = empty_cols

    if empty_cols:
        solution[0] += 1
