import copy
grid=[['.','.','.','.','.','.'],
      ['.','0','0','.','.','.'],
      ['0','0','0','0','.','.'],
      ['0','0','0','0','0','.'],
      ['.','0','0','0','0','0'],
      ['0','0','0','0','0','.'],
      ['0','0','0','0','.','.'],
      ['.','0','0','.','.','.'],
      ['.','.','.','.','.','.'],
     ]
newgrid=copy.deepcopy(grid)
for i in range(0,len(newgrid)-3):
    for j in range(0,len(newgrid[i])+3):
        print(newgrid[j][i],end=' ')
    print()
