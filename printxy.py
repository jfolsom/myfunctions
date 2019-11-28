row1 = list('..00.00..')
row2 = list('.0000000.')
row3 = list('.0000000.')
row4 = list('..00000..')
row5 = list('...000...')
row6 = list('....0....')
picture = [row1, row2, row3, row4, row5, row6]

# print a list of lists
def printxy(listoflists):
    for y in range(len(picture)):
        for x in range(len(row1)):
            print(picture[y][x], end='')
        print('\n')