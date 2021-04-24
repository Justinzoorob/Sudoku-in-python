from Game import *

def afficherGrille(grille):
    '''
    (list) -> None
    Displays the Sudoku game grid
    Preconditions: grille is a reference to a 9x9 matrix which already contains numbers from 1 to 9
    '''
    print("   ", end="")
    col = 0
    while col < len(grille):
      print(col, end="  ")
      col += 1
    print()
    row = 0
    while row < len(grille):
       print(row, end="")
       col = 0
       while col < len(grille[row]):
         print(" ", grille[row][col], end="")
         col += 1
       print()
       row += 1

def jouer(grille, row, col, num):
    '''
    (list, int, int, int) -> Bool
    Play a Sudoku game step
    Preconditions: grille is a reference on a 9x9 list contains only numbers
    grid is modified (an element is added in the grid) if the box is valid is correct.
    '''
    x = False
    if verifierValide(grille, row, col, num) == True:
        grille[row][col] = num
        x = True
    return x


# Main Programme

# Create the game board (9 x 9)
grille = [[5, 3, 8, 6, 9, 1, 0, 4, 7],
          [7, 4, 6, 0, 3, 2, 8, 1, 9],
          [1, 9, 2, 0, 8, 4, 3, 5, 6],
          [8, 7, 1, 2, 6, 3, 4, 9, 5],
          [3, 2, 9, 4, 5, 7, 1, 6, 8],
          [4, 6, 5, 9, 1, 8, 7, 2, 3],
          [0, 0, 4, 3, 7, 9, 5, 8, 2],
          [9, 8, 3, 1, 0, 5, 6, 7, 4],
          [2, 5, 0, 8, 4, 6, 9, 3, 1]]  # the only matrix used in the program.
print("Menu: 1- Start a new game.")
print("     ", "2- Continue the game.")
print("     ", "3- Quit the game.")
choix = int(input("Please enter your choice: 1, 2 ou 3: "))
while choix < 3 and choix > 0:
      if choix == 1:
          # Create the game board (9 x 9)
          grille = [[5, 3, 8, 6, 9, 1, 0, 4, 7],
                    [7, 4, 6, 5, 3, 2, 8, 1, 9],
                    [1, 9, 2, 7, 8, 4, 3, 5, 6],
                    [8, 7, 1, 2, 6, 3, 4, 9, 5],
                    [3, 2, 9, 4, 5, 7, 1, 6, 8],
                    [4, 6, 5, 9, 1, 8, 7, 2, 3],
                    [6, 1, 4, 3, 7, 9, 5, 8, 2],
                    [9, 8, 3, 1, 2, 5, 6, 7, 4],
                    [2, 5, 0, 8, 4, 6, 9, 3, 1]]  # the only matrix used in the program.
      afficherGrille(grille)
      row = int(input("Please enter the row index: "))
      col = int(input("Please enter the Column index: "))
      num = int(input("Please enter the number you would like: "))
      if grille[row][col] == 0:
          ajout = jouer(grille, row, col, num)
          if ajout == True:
              print("Good Job!")
          else:
              print("Failure :(")
      else:
          print("Box already filled")
      afficherGrille(grille)
      if verifierGagner(grille) == True:
          print("Good Job you have Won")
          choix = -1
      else:
        print("Menu: 1- Start a new game.")
        print("     ", "2- Continue the game.")
        print("     ", "3- Quit the game.")
        choix = int(input("Please enter your choice: 1, 2 ou 3: "))
if choix==3:
    print("Goodbye :)")
