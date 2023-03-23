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


def pieces_between(axis:str, id:int, board:list, king:str, rooks:tuple):
    if axis == 'x':
        row = board[id]
        for rook_id in rooks:
            king_id = row.find(king)
            #print(row[rook_id], king_id)
            space_between = row[min(rook_id, king_id)+1:max(rook_id, king_id)]
            if row[min(rook_id, king_id)+1:max(rook_id, king_id)] == '.' * len(space_between):
                return True

        
    
    else:
        col = []
        for row in board:
            for col_id, piece in enumerate(row):
                if col_id == id:
                    col.append(piece)
        


    return False



print(pieces_between('y', 1, ['........', 'wP.K....', '...w....'],  'K', (0,6)))
