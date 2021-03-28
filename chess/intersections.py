from pprint import pprint

def parseFen(position):
    board = [['X' for file in range(0, 12)] for rank in range(0, 12)]
    ranks = reversed(position.split('/'))
    for r, rank in enumerate(ranks, start=2):
        f = 2
        for piece in rank:
            if piece.isdigit():
                count = int(piece)
                board[r][f : f+count] = [' '] * count
                f += count
            else:
                board[r][f] = piece
                f += 1
    return board

def printBoard(position):
    pprint(parseFen(position)[::-1])

def getPiece(board, r, f):
    return board[r + 2][f + 2]

def addIntersection(state, dr, df):
    board, intersections, piece, r, f = state
    tr, tf = r+dr, f+df
    if getPiece(board, tr, tf) != 'X':
        intersections[tr][tf].append('%s%d%s' % (piece, r + 1, chr(ord('a') + f)))

def addUntilCollision(state, dr, df):
    board, intersections, piece, r, f = state
    i = 1
    while True:
        tr, tf = r + i*dr, f + i*df
        target = getPiece(board, tr, tf)
        if target == 'X':
            break # Ran off the board, so don't count this square
        intersections[tr][tf].append('%s%d%s' % (piece, r + 1, chr(ord('a') + f)))
        if target != ' ':
            break # Collided with a piece
        i += 1

startBoard = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

def findIntersections(position):
    board = parseFen(position)
    intersections = [[[] for file in range(0, 8)] for rank in range(0, 8)]
    for r in range(8):
        for f in range(8):
            piece = getPiece(board, r, f)
            print(r, f)
            if piece == ' ' or piece == 'X':
                continue
            state = (board, intersections, piece, r, f)
            if piece == 'P':
                addIntersection(state,  1, -1)
                addIntersection(state,  1,  1)
            elif piece == 'p':
                addIntersection(state, -1, -1)
                addIntersection(state, -1,  1)
            elif piece == 'N' or piece == 'n':
                addIntersection(state,  2,  1)
                addIntersection(state,  2, -1)
                addIntersection(state,  -2,  1)
                addIntersection(state,  -2, -1)
                addIntersection(state,  1,  2)
                addIntersection(state,  1, -2)
                addIntersection(state, -1,  2)
                addIntersection(state, -1, -2)
            elif piece == 'K' or piece == 'k':
                addIntersection(state,  1,  1)
                addIntersection(state,  1,  0)
                addIntersection(state,  1, -1)
                addIntersection(state,  0,  1)
                #addIntersection(state,  0,  0)
                addIntersection(state,  0, -1)
                addIntersection(state, -1,  1)
                addIntersection(state, -1,  0)
                addIntersection(state, -1, -1)
            else:
                if piece == 'B' or piece == 'b' or piece == 'Q' or piece == 'q':
                    addUntilCollision(state,  1,  1)
                    addUntilCollision(state,  1, -1)
                    addUntilCollision(state, -1,  1)
                    addUntilCollision(state, -1, -1)
                if piece == 'R' or piece == 'r' or piece == 'Q' or piece == 'q':
                    addUntilCollision(state,  0,  1)
                    addUntilCollision(state,  0, -1)
                    addUntilCollision(state,  1,  0)
                    addUntilCollision(state, -1,  0)
    return intersections

def printIntersections(position):
    pprint(findIntersections(position)[::-1])

if __name__ == '__main__':
    printBoard(startBoard)
    
    printIntersections(startBoard)

