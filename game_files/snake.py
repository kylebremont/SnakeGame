
# colors
RED = (255,0,0)

# grid variables
GRID_WIDTH = 20
GRID_HEIGHT = 20
GRID_MARGIN = 5
GRID_LENGTH = 10

class Snake:
    
    def __init__(self, row, col):
        self.row_ = row
        self.col_ = col
        self.color_ = RED
        self.direction_ = 'right'
    
    def set_row(self, row):
        if row < GRID_LENGTH and row >= 0:
            self.row_ = row
    
    def set_col(self, col):
        if col < GRID_LENGTH and col >= 0:
            self.col_ = col
    
    def set_direction(self, direction):
        direction = direction.lower()
        directions = ['right', 'left', 'down', 'up']
        if direction in directions:
            self.direction_ = direction
    
    def Move(self):
        if self.direction_ == 'right' and self.col_ < GRID_LENGTH-1:
            self.col_ += 1
        elif self.direction_ == 'left' and self.col_ > 0:
            self.col_ -= 1
        elif self.direction_ == 'down' and self.row_ < GRID_LENGTH-1:
            self.row_ += 1
        elif self.direction_ == 'up' and self.row_ > 0:
            self.row_ -= 1

    def AddSegment(self, new_snake):
        # set direction of segment
        new_snake.set_direction(self.direction_)
        # set row and col of segment
        if self.direction_ == 'right':
            new_snake.set_row(self.row_)
            new_snake.set_col(self.col_ - 1)
        elif self.direction_ == 'left':
            new_snake.set_row(self.row_)
            new_snake.set_col(self.col_ + 1)
        elif self.direction_ == 'down':
            new_snake.set_row(self.row_ - 1)
            new_snake.set_col(self.col_)
        elif self.direction_ == 'up':
            new_snake.set_row(self.row_ + 1)
            new_snake.set_col(self.col_)