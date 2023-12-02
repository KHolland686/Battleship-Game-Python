import random
import time

class BattleshipGame:
    '''
    Class representing a Battleship game.

    ATTRIBUTES:
        grid_size (int): The size of the game grid.
        num_of_ships (int): The number of ships in the game.
        grid (list): 2D list representing the game grid.

    METHODS:
        drawBoard(): Draws the game board.
        setupBoard(): Sets up the game grid and places ships.
        hitOrMiss(row, col): Checks if the user's shot is a hit or miss.
        isGameOver(): Checks if the game is over.
        play(): Main function to play the Battleship game.
    '''

    Water = ' . |'
    Ship = ' S |'
    Hit = ' X |'
    Miss = ' O |'

    def __init__(self, grid_size = 10, num_of_ships = 5, max_chances = 15, show_ships = False):
        '''
        Initializes a BattleshipGame object.

        PARAMETERS:
            grid_size (int): The size of the game grid.
            num_of_ships (int): The number of ships in the game.
            max_chances (int): The maximum number of chances allowed to the  player.
            show_ships (bool): Whether to show the ship positions on the board.
        '''
        self.grid_size = grid_size
        self.grid = [[' ' + '|' for _ in range(grid_size)] for _ in range       (grid_size)]
        self.num_of_ships = num_of_ships
        self.max_chances = max_chances
        self.show_ships = show_ships
        self.setupBoard()


    def drawBoard(self):
        '''
        Draws the game board.
        '''
        print("  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |")
        print('--+---+---+---+---+---+---+---+---+---+---+')
        row_num = 0
        for row in self.grid:
            if not self.show_ships:
                row = row = [self.Water if cell == self.Ship else cell for cell in row]
            print ("%d |%s" % (row_num, "".join(row)))
            print('--+---+---+---+---+---+---+---+---+---+---+')
            row_num += 1
    

    def setupBoard(self):
        '''
        Sets up the game grid and places ships.

        RETURNS:
            tuple: A tuple containing the count of placed ships and water cells.
        '''
        i = j = 0
        while i < self.grid_size:
            while j < self.grid_size:
                # iterates through each column in a row placing water cells
                self.grid[i][j] = self.Water 
                j += 1
            j = 0
            i += 1
            # resets from the first column and continues on the next row

    
        shipCount = 0
        while shipCount < self.num_of_ships:
            randomRow = random.randint(0, self.grid_size - 1)
            randomCol = random.randint(0, self.grid_size - 1)
            # generate a random row & column for each ship
            if self.grid[randomRow][randomCol] == self.Water:
                self.grid[randomRow][randomCol] = self.Ship
                # sets each generated point up as a ship
                shipCount += 1
            
        waterCount = sum(row.count(self.Water) for row in self.grid)
                            
        return shipCount, waterCount
            

    def hitOrMiss(self, row, col):
        '''
        Checks if the user's shot is a hit or miss.

        PARAMETERS:
            row (int): The row index of the shot.
            col (int): The column index of the shot.

        RETURNS:
            str: 'HIT' if the shot is a hit, 'MISS' if it's a miss, or 'Already Hit' if the cell was already hit.
        ''' 
        if self.grid[row][col] == self.Ship:
            # takes row and column from user input and compares to the existing cell
            self.grid[row][col] = self.Hit
            print('HIT')
            return 'HIT'
        elif self.grid[row][col] == self.Hit:
            print('Already Hit')
            return 'HIT'
        else:
            self.grid[row][col] = self.Miss
            print('MISS')
            return 'MISS'
        

    def isGameOver(self):
        '''
        Checks if the game is over.

        RETURNS:
            bool: True if all ships are shot, False otherwise.
        '''

        count = 0
        for i in self.grid:
            for j in i:
            # nested for loop to check each cell
                if j == self.Ship:
                    count += 1
        if count == 0:
            return True
        else:
            return False


    def play(self):
        '''
        Main funtion to play the game of Battleship.
        '''
        chances = 0
        self.drawBoard()
        # draw the board

        while not self.isGameOver() and chances <= self.max_chances:
            # Gathers and validates user input
            try:
                print(f'Attempt {chances + 1} of {self.max_chances}')
                row = int((input('Enter a row: ')))
                col = int(input('Enter a column: '))

                while not 0 <= row < self.grid_size and 0 <= col < self.grid_size:
                    print("Invalid row or column. Please enter a number within the grid!")
                    row = int((input('Enter a row: ')))
                    col = int(input('Enter a column: '))
                    # makes sure input is within grid and repeats if not


                self.hitOrMiss(row, col)
                # check whether input is a hit or a miss
                self.drawBoard()
                # redraw board
                chances += 1
            except ValueError:
                print("Invalid input! Please enter a valid integer")
            except IndexError:
                print("Please enter numbers within the grid range")

        if self.isGameOver():
        #check game over conditions
            print('Game over! You sunk all the ships!')
        else:
            print('Game over! You ran out of chances.')

            if not self.show_ships:
                print('\nThis is where the ships were located:')
                self.show_ships = True
                self.drawBoard()

if __name__ == '__main__':
    print(f"""
        -------BATTLESHIPS-------
        Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
        How it will work:
        1. A 10x10 grid will have 5 ships randomly placed (default settiings)
        2. You can choose a row and column to indicate where to shoot
        3. For every shot that hits or misses it will show up in the grid
        4. If all ships are shot, game over!
        5. As a default, you will have 15 chances
        6. Ships are hidden as default, and their placement will be shown when game is finished
        
          LEGEND
            "." = water
            "S" = ship position
            "O" = water that was shot with bullet, a miss because it hit no ship
            "X" = ship sunk!
        """)
    time.sleep(5)
    game = BattleshipGame()
    game.play()
