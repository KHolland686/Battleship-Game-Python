from Battleship import BattleshipGame
import unittest

#arrays to use for testing
testArray = [[' . |'] * 10 for i in range(10)]



testArrayShips = [[' . |'] * 10 for i in range(10)]

testArrayShips2 = [[' . |'] * 10 for i in range(10)]
testArrayShips2[2][2] = ' S |'

testArrayShips3 = [[' . |'] * 10 for i in range(10)]
testArrayShips3[3][3] = ' S |'

#set up the class to create test functinos
class TestBattleship(unittest.TestCase):

    def test_setupBoard(self):
        game = BattleshipGame(grid_size = 10, num_of_ships = 10)
        ship_count, water_count = game.setupBoard()

        # Tests the counted number of placed ships against an array with 10 ships
        self.assertEqual(ship_count, 10)
        
        # Checks that given array has correct amount of 'water' spaces
        self.assertEqual(water_count, 90)
        
     
    def test_hitOrMiss(self):
        game = BattleshipGame(grid_size = 10, num_of_ships = 0)
        game.setupBoard()

        #tests checking a spot in an array with no ship, 
        self.assertEqual(game.hitOrMiss(0, 0), 'MISS')
        
        game2=BattleshipGame(grid_size = 1, num_of_ships = 1)
        game2.setupBoard()
        #tests cheking a spot in an array with a ship
        self.assertEqual(game2.hitOrMiss(0,0), 'HIT')

        game3 = BattleshipGame(grid_size = 1, num_of_ships = 1)
        game3.setupBoard()
        game3.hitOrMiss(0,0)
        self.assertEqual(game3.hitOrMiss(0,0), 'HIT')


    
    def test_isGameOver(self):
        game = BattleshipGame(grid_size = 10, num_of_ships = 0)
        game.setupBoard()
        game.grid[0][0] = game.Ship

       #Tests a board with one ship and returns False
        self.assertIs(game.isGameOver(), False)
       
       #Tests a board with one hit ship and returns True
        game.grid[0][0] = game.Hit
        self.assertIs(game.isGameOver(), True)
        print(game.isGameOver())

       

if __name__ == '__main__':
    unittest.main()
    
