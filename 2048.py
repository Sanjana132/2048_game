import random
import copy
game_size = int(input("what size game of 2048? "))
win_num = int(input("enter the winning number: "))

def power_2(win_num):
  p = 1
  if (win_num and not (win_num & (win_num - 1))):
    return win_num
  while p < win_num:
    p <<= 1
  return p  
    
def display():
  lv = game_board[0][0]
  for row in game_board:
    for value in row:
      if value > lv:
        lv = value

  space = len(str(lv))

  for row in game_board:
    row1 = ""
    for value in row:

      row1 += (" " * (space - len(str(value)))) + str(value) + " "

    print(row1)
  print() 

def left(row): 
  for j in range(game_size - 1):
    for i in range(game_size - 1, 0, -1):
      if row[i - 1] == 0:
        row[i-1] = row[i]
        row[i] = 0
        
  for i in range(game_size - 1):
    if row[i] == row[i+1]:
      if row[i] !=0: 
        row[i] =row[i] + row[i+1]
        row[i+1] = 0

  for i in range(game_size - 1, 0, -1):
    if row[i-1] == 0:
      row[i-1] = row[i]
      row[i] = 0
  return row 

def merge_left(currentboard):
  for i in range(game_size):
    currentboard[i] = left(currentboard[i])

  return currentboard

def reverse(row):
  rev = []
  for i in range(game_size - 1,-1, -1):
    rev.append(row[i])
  return rev

def merge_right(currentboard):
  for i in range(game_size):
    currentboard[i] = reverse(currentboard[i])
    currentboard[i] = left(currentboard[i])
    currentboard[i] = reverse(currentboard[i])

  return currentboard

def transpose(currentboard):
  for j in range(game_size):
    for i in range(j, game_size):
      if i != j:
        temp = currentboard[j][i]
        currentboard[j][i] = currentboard[i][j]
        currentboard[i][j] = temp
  return currentboard

def merge_up(currentboard):
  currentboard = transpose(currentboard)
  currentboard = merge_left(currentboard)
  currentboard = transpose(currentboard)

  return currentboard

def merge_down(currentboard):
  currentboard = reverse(currentboard)
  currentboard = merge_up(currentboard)
  currentboard = reverse(currentboard)

  return currentboard

def add_2():
  return 2

def place_2():
  row2 = random.randint(0, game_size-1) 
  col2 = random.randint(0, game_size-1) 

  while game_board[row2][col2] != 0:
    row2 = random.randint(0, game_size-1) 
    col2 = random.randint(0, game_size-1) 

  game_board[row2][col2] = add_2()  

def win():
  win_1=power_2(win_num)
  for row in game_board:
    if win_1 in row:
      return True
  return False    

def lose():
  temp_board1 = copy.deepcopy(game_board)
  temp_board2 = copy.deepcopy(game_board)

  temp_board1 = merge_up(temp_board1)
  if temp_board1 == temp_board2:
    temp_board1 = merge_left(temp_board1)
    if temp_board1 == temp_board2:
      temp_board1 = merge_down(temp_board1)
      if temp_board1 == temp_board2:
        temp_board1 = merge_right(temp_board1)
        if temp_board1 == temp_board2:
          return True
  return False        

game_board = []
for i in range(game_size):
  row = []
  for j in range(game_size):
    row.append(0)
  game_board.append(row)
  
num = 1
while num > 0:
  row2  = random.randint(0,game_size - 1)
  col2  = random.randint(0,game_size - 1)

  if game_board[row2][col2] == 0:
    game_board[row2][col2] = add_2()
    num = num - 1

print("play 2048")
print()
print("Instructions:Type 'w' to move up , Type 'a' to move left, Type s to move down, Type d to move right. ")
display()

game_end = False

while not game_end:
  move = input("which way do you want to move? ")

  valid = True

  temp_board = copy.deepcopy(game_board)

  if move == "w":
    game_board = merge_up(game_board)
  elif move == "a":
    game_board = merge_left(game_board)
  elif move == "s":
    game_board = merge_down(game_board)
  elif move == "d":
    game_board = merge_right(game_board)
  else:
    valid = False
  
  if not valid:
    print("enter a valid move!!")
  else:
    if game_board == temp_board:
      print("try another direction")
    else:
      if win():
        display()
        print("you won!!!")
        game_end = True
      else:  
        place_2()
        display()  

        if lose():
          print("You lost...")
          game_end = True
      





 

