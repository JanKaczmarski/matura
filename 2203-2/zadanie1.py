with open("Dane_2203-2/szachy_przyklad.txt", "r") as file:
    boards = [[]]
    for line in file:
        if line == '\n':
            boards.append([])
            continue
        boards[-1].append(line[:-1])

sol_empty_lines = []

#i = 0
half_empty_boards = 0
most_empty_board = 0
for board in boards:
    empty_col = 0
    #if i == 1: break
    rows = {i+1:'' for i in range(8)}
    empty_rows = [True for _ in range(8)]
    
    for row_id, row in enumerate(board):
        rows[row_id+1] += row
        
    for j, item in enumerate(rows.items()):
        for file in item[1]:
            if file != '.':
                empty_rows[j] = False
        if empty_rows[j]:
            empty_col += 1
    
    if empty_col > most_empty_board:
        most_empty_board = empty_col
        
    if empty_col != 0:
        half_empty_boards += 1
            
    
            
    #i += 1
            
print(half_empty_boards, most_empty_board)
        
        