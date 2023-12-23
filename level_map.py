def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        f = [line.strip() for line in mapFile]
    board=[]
    for i in range(len(f)):
        s = [j for j in f[i]]
        board.append(s)
    return board
#подгрузка уровня из текстового файла