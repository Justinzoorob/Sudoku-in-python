def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Check if the box to add does not exist on the line.
        Preconditions: grille is a reference to a 9x9 matrix which already contains numbers from 1 to 9
    '''
    x = -1
    for i in grille:
        x += 1
        if x == row:
            if num not in i: 
                z = True
            else: 
                z = False
            break
    return z

def verifierCol(grille, col, num):
    '''
        (list, int, int) -> Bool
        Check if the box to add does not exist on the column.
        Preconditions: grille is a reference to a 9x9 matrix which already contains numbers from 1 to 9   
    '''
    x = -1
    for i in grille:
        x += 1
        z = True
        if grille[x][col] == num:
            z = False
            break
    return z


def verifierSousGrille(grille, row, col, num):
    '''
        (list, int, int, int) -> Bool
        Check if the box to add does not exist on the sub-grid.
        Preconditions: grille is a reference to a 9x9 matrix which already contains numbers from 1 to 9
    '''
    ls = []
    x = False
    if row < 3 and col < 3:
        for i in range(0,3):
            for k in range(0,3):
                ls.append(grille[i][k])
        if num not in ls:
            x = True

    elif  row < 3 and 3 <= col < 6:
        for i in range(0,3):
            for k in range(3,6):
                ls.append(grille[i][k])
        if num not in ls:
            x = True

    elif row < 3 and 6 <= col:
        for i in range(0,3):
            for k in range(6,9):
                ls.append(grille[i][k])
        if num not in ls:
            x = True

    elif 3 <= row < 6 and col < 3:
        for i in range(3,6):
            for k in range(0,3):
                ls.append(grille[i][k])
        if num not in ls:
            x = True

    elif 3 <= row < 6 and 3 <= col < 6:
        for i in range(3,6):
            for k in range(3,6):
                ls.append(grille[i][k])
        if num not in ls:
            x = True

    elif 3 <= row < 6 and 6 <= col:
        for i in range(3,6):
            for k in range(6,9):
                ls.append(grille[i][k])
        if num not in ls:
            x = True

    elif 6 <= row and col < 3:
        for i in range(6,9):
            for k in range(0,3):
                ls.append(grille[i][k])
        if num not in ls:
            x = True

    elif 6 <= row and 3 <= col < 6:
        for i in range(6,9):
            for k in range(3,6):
                ls.append(grille[i][k])
        if num not in ls:
            x = True

    elif 6 <= row and 6 <= col:
        for i in range(6,9):
            for k in range(6,9):
                ls.append(grille[i][k])
        if num not in ls:
            x = True

    return x

    
def verifierGagner(grille):
    '''(list) ->  bool
    * Preconditions: grille is a reference to a 9x9 matrix which already contains numbers from 1 to 9
    * Checks if the grid is completely filled.
    '''
    x = True
    for i in grille:
        for k in i:
            if k == 0:
                x = False
    return x 
  
def verifierValide(grille, row, col, num):
   ''' (list, int, int, int) ->  bool
   * Checks if the proposed number is correct on the row and column and the sub-grid given in parameter.
   * Preconditions: grille is a reference to a 9x9 matrix which already contains numbers from 1 to 9
   '''
   if verifierLigne(grille, row, num) == True and verifierCol(grille, col, num) == True and verifierSousGrille(grille, row, col, num) == True:
       x = True
   else:
        x = False
   return x
    
   

