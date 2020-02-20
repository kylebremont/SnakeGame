import pygame
import numpy as np
from snake import Snake
from food import Food

# pygame window setup
pygame.init()
WINDOW_WIDTH = 255
WINDOW_HEIGHT = 255
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# grid variables
GRID_WIDTH = 20
GRID_HEIGHT = 20
GRID_MARGIN = 5
GRID_LENGTH = 10
grid = []

# Food
food = Food()

# clock
FPS = 4
clock = pygame.time.Clock()

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_GREY = (211,211,211)
GREEN = (0,255,0)

class DirectionChange:
    def __init__(self, row, col, direction):
        self.row_ = row
        self.col_ = col
        self.direction_ = direction

def CreateGrid(player):
    for row in range(GRID_LENGTH):
        grid.append([])
        for col in range(GRID_LENGTH):
            grid[row].append(0)

    # initialize where snake and food is
    for i in range(len(player)):
        grid[player[i].row_][player[i].col_] = 1
    grid[food.row_][food.col_] = 2

def DisplayBoard(player):
    CreateGrid(player)
    for row in range(GRID_LENGTH):
        for col in range(GRID_LENGTH):
            color = BLACK
            if grid[row][col] == 1:
                color = player[0].color_
            elif grid[row][col] == 2:
                color = food.color_
            pygame.draw.rect(window, color, [(GRID_MARGIN + GRID_WIDTH) * col + GRID_MARGIN, (GRID_MARGIN + GRID_HEIGHT) * row + GRID_MARGIN, GRID_WIDTH, GRID_HEIGHT])
    

def RunProgram():

    # handles direction changes
    dir_changes = []
    remove_dir = 0

    # keep track of the points
    points = 0

    # the snake
    player = []
    player.append(Snake(0,0))

    run = True
    while run:
        # get events in the game
        for event in pygame.event.get():
            # check if exit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # check key presses
            if event.type == pygame.KEYDOWN:
                # left arrow
                if event.key == pygame.K_LEFT:
                    change = DirectionChange(player[0].row_, player[0].col_, 'left')
                    player[0].set_direction('left')
                    dir_changes.append(change)
                # right arrow 
                if event.key == pygame.K_RIGHT:
                    change = DirectionChange(player[0].row_, player[0].col_, 'right')
                    player[0].set_direction('right')
                    dir_changes.append(change)
                # down arrow
                if event.key == pygame.K_DOWN:
                    change = DirectionChange(player[0].row_, player[0].col_, 'down')
                    player[0].set_direction('down')
                    dir_changes.append(change)
                # up arrow
                if event.key == pygame.K_UP:
                    change = DirectionChange(player[0].row_, player[0].col_, 'up')
                    player[0].set_direction('up')
                    dir_changes.append(change)

        # make background light grey
        window.fill(LIGHT_GREY)
        # create and display the board
        DisplayBoard(player)

        # make snake move constantly
        for snake_seg in player:
            temp_row, temp_col = snake_seg.row_, snake_seg.col_
            snake_seg.Move()
            # if the snake actually moved
            if snake_seg.row_ != temp_row or snake_seg.col_ != temp_col:
                grid[temp_row][temp_col] = 0

        # after move check if the head of snake hit food
        if player[0].row_ == food.row_ and player[0].col_ == food.col_:
            points += 1
            snake_length = len(player)
            new_segment = Snake(0,0)
            player[snake_length-1].AddSegment(new_segment)
            player.append(new_segment)
            food.ChangeLocation()
        
        # after move check if snake ran into itself
        if len(player) > 1:
            for i in range(1, len(player)):
                if player[0].row_ == player[i].row_ and player[0].col_ == player[i].col_:
                    run = False

        # check if segment direction needs to change
        for change_class in dir_changes:
            for i in range(len(player)):
                if player[i].row_ == change_class.row_ and player[i].col_ == change_class.col_:
                    # change direction of that segment
                    player[i].set_direction(change_class.direction_)
                    if i == len(player)-1:
                        remove_dir += 1
        # remove the direction from list of directions
        while remove_dir > 0:
            dir_changes.pop(0)
            remove_dir -= 1

        # check if segment direction needs to change
        #for snake_seg in player:
        #    if snake_seg.row_ == row_change and snake_seg.col_ == col_change:
        #        snake_seg.set_direction(dir_change)

        # update the window
        pygame.display.flip()
        # tick the clock
        clock.tick(FPS)

    return points

def Menu(is_end, points):

    run = True
    new_game = False
    end_font = pygame.font.Font('freesansbold.ttf', 25)
    start_font = pygame.font.Font('freesansbold.ttf', 15)
    # start menu text
    start_text = start_font.render('Press Space Bar to Start Game!', True, WHITE)
    start_text_rect = start_text.get_rect()
    start_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    while run:
        # get events
        for event in pygame.event.get():
            # if the x is pressed
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # if a new game is created
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_game = True
                    run = False

        # make background black
        window.fill(BLACK)

        # if the game ended
        if is_end:
            # generate points
            end_points = end_font.render('Points: {}'.format(points), True, WHITE)
            end_points_rect = end_points.get_rect()
            end_points_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)
            # generate play again text
            end_text = start_font.render('Press Space Bar to Play Again!', True, WHITE)
            end_text_rect = end_text.get_rect()
            end_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            # display the points to user
            window.blit(end_points, end_points_rect)
            window.blit(end_text, end_text_rect)
        # if the game hasn't been played yet
        else:
            # display the start menu
            window.blit(start_text, start_text_rect)

        # update the window
        pygame.display.flip()
    
    if new_game:
        points = RunProgram()
        Menu(True, points)


def main():

    Menu(False, 0)
    pygame.quit()

if __name__=='__main__':
    main()
