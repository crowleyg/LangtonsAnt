# Author: Garrett Crowley
# Date: 08/03/21
# Description: main() takes input from user to create a class called Ant capable of
# running Langton's Ant simulation and returning final game board

class Ant:
    """ Represents a Ant with methods to run Langton's Ant simulation  """

    def __init__(self, row, col, direction, board_size):
        """ Creates an Ant object with starting row and column, direction and board size"""

        self._row = row
        self._col = col
        self._direction = direction
        self._board_size = board_size

    def _game_board(self, board_size):
        """ Creates the game board for Langton's Ant to move on"""

        game_grid = []
        for num in range(0, board_size):
            game_grid.append([])
        for row in game_grid:
            for col in range(0, board_size):
                row.append("_")
        return game_grid

    def _change_color(self, grid, row, col):
        """ Changes the color of space after ant leaves space"""

        if grid[row][col] == '#':   #black space
            grid[row][col] = '_'   #white space
        else:
            grid[row][col] = '#'   #black space

    def _change_direction(self, grid):
        """ Changes direction of ant based off color of space ant is located on"""

        if grid[self._row][self._col] == '#':
            self._direction = ((self._direction - 1) % 4)
        else:
            self._direction = ((self._direction + 1) % 4)


    def _change_position(self, direction):
        """ Changes position of ant on game board based off current direction """

        if direction == 0:
            self._row = (self._row - 1)
        if direction == 1:
            self._col = (self._col + 1)
            if self._col > (self._board_size - 1):
                self._col = 0
        if direction == 2:
            self._row = (self._row + 1)
            if self._row > (self._board_size - 1):
                self._row = 0
        if direction == 3:
            self._col = (self._col - 1)

    def _print_board(self, game_grid):
        """ Returns the final game board"""

        temp_str = ''
        for row in range(0, self._board_size):
            for col in range(0, self._board_size):
                temp_str += game_grid[row][col]
            print(temp_str)
            temp_str = ''

    def run_simulation(self, num_of_steps):
        """ Runs the Langton's Ant simulation and returns the final game board """

        game_grid = self._game_board(self._board_size)
        steps_taken = 0

        while steps_taken < num_of_steps:
            self._change_direction(game_grid)
            self._change_color(game_grid, self._row, self._col)
            self._change_position(self._direction)
            steps_taken += 1
        game_grid[self._row][self._col] = '8'
        self._print_board(game_grid)


def main():
    """ Returns the result of Langton's Ant simulation """

    print("Welcome to Langton's ant simulation!")
    print("First, please enter a number no larger than 100 for the size of the square board:")
    board_size = int(input())
    print("Choose the ant's starting location, please enter a number as the starting row number (where 0 is the first row from the top):")
    start_row = int(input())
    print("Please enter a number as the starting column number (where 0 is the first column from the left):")
    start_col = int(input())
    print("Please choose the ant's starting orientation, 0 for up, 1 for right, 2 for down, 3 for left:")
    start_direction = int(input())
    new_ant = Ant(start_row, start_col, start_direction, board_size)
    print("Please enter the number of steps for the simulation:")
    num_of_steps = int(input())
    new_ant.run_simulation(num_of_steps)

main()