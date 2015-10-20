"""
Clone of 2048 game.
http://www.codeskulptor.org/#user40_Vrx1JxeEW9_32.py
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    tmp = filter(None,line)
    
    for cnt in range(len(tmp)-1):
        if tmp[cnt] == tmp[cnt+1]:
            tmp[cnt]=2*tmp[cnt]
            tmp[cnt+1]=0

    result = filter(None,tmp)
    result = result + [0]*(len(line)-len(result))
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Intialize the class
        """
        self._grid_height=grid_height
        self._grid_width=grid_width
        self.reset()
        initial_up=[(0,col) for col in range(self._grid_width)]
        initial_down=[(self._grid_height-1,col) for col in range(self._grid_width)]
        initial_left=[(row,0) for row in range(self._grid_height)]
        initial_right=[(row,self._grid_width-1) for row in range(self._grid_height)]
        self._initial_tiles={UP:initial_up,DOWN:initial_down,LEFT:initial_left,RIGHT:initial_right}
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)]
                           for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        add_new=False
        for tile in self._initial_tiles.get(direction):
            indices=[]
            values=[]
            if direction == UP or direction == DOWN:
                size=self.get_grid_height()
            else:
                size=self.get_grid_width()
                
            print 'in_til',self._initial_tiles[direction]
            for num in range(size):
                print 'num----',num
                (row,col)=tuple(map(lambda x, y: x + y * num, tile, OFFSETS[direction]))
                print 'row col',(row,col)
                indices.append((row,col))
                values.append(self.get_tile(row,col))
            print indices
        #    print values
            result=merge(values)
            if result != values:
                add_new=True
            for tile_idx in range(len(indices)):
                (irow,jcol)=indices[tile_idx]
        #        print irow,jcol
                self.set_tile(irow,jcol,result[tile_idx])
        if add_new:
            self.new_tile()
            add_new=False
            

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        hel=random.choice([(row,col) for col in range(self._grid_width) for row in range(self._grid_height) if self.get_tile(row,col)==0])
        self.set_tile(hel[0],hel[1],random.choice([2] * 90 + [4] * 10))

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col]=value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

#alok=TwentyFortyEight(4,4)
#alok.move(UP)
#print '-------------'
#alok.move(DOWN)
poc_2048_gui.run_gui(TwentyFortyEight(4, 5))

