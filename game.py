import pygame
import random
import time

from classes.shape import shape
from classes.shape_strategy import *

pygame.font.init()

play_width = 300
play_height = 600
block_size = 30

top_left_x = (800 - 300) // 2
top_left_y = 700 - 600

def create_grid(used_coordinates={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in used_coordinates:
                coordinate = used_coordinates[(j,i)]
                grid[i][j] = coordinate
    return grid

def convert_shape_format(shape):
    positions = []
    format = shape.shape_space[shape.rotation % len(shape.shape_space)]
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions

def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    coordinates = convert_shape_format(shape)

    for pos in coordinates:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def draw_text_middle(text, size, colour, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, colour)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y + play_height/2 - label.get_height()/2))

def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical lines

def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1

            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape_space[shape.rotation % len(shape.shape_space)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.colour, (sx + j*30, sy + i*30, 30, 30), 0)

    surface.blit(label, (sx + 10, sy- 30))

def draw_window(surface, grid):
    surface.fill((0,0,0))
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (255,255,255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)

    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)

def shape_locked(shape_pos, used_coordinates, shape_list, current_shape, next_shape):
    for pos in shape_pos:
        p = (pos[0], pos[1])
        used_coordinates[p] = current_shape.colour
    current_shape = next_shape
    current_shape.y = 0
    next_shape = shape().get_shape(shape_strategy= random.choice(shape_list))
    change_piece = False
    return current_shape, next_shape, change_piece

def update_grid(shape_pos, grid, current_shape):
    for i in range(len(shape_pos)):
        x, y = shape_pos[i]
        if y > -1:
            grid[y][x] = current_shape.colour
    return grid

def move_down(current_shape, grid):
    current_shape.y += 1
    if not valid_space(current_shape, grid):
        current_shape.y -= 1

def rotate_shape(current_shape, grid):
    current_shape.rotation = current_shape.rotation + 1 % len(current_shape.shape_space)
    if not valid_space(current_shape, grid):
        current_shape.rotation = current_shape.rotation - 1 % len(current_shape.shape_space)

def check_move_shape(event, current_shape, grid):
    if event.key == pygame.K_LEFT:
        current_shape.x -= 1
        if not valid_space(current_shape, grid):
            current_shape.x += 1

    elif event.key == pygame.K_RIGHT:
        current_shape.x += 1
        if not valid_space(current_shape, grid):
            current_shape.x -= 1

def check_events(current_shape, grid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            check_move_shape(event, current_shape, grid)
            if event.key == pygame.K_UP:
                rotate_shape(current_shape, grid)

            if event.key == pygame.K_DOWN:
                move_down(current_shape, grid)

def set_up_clock():
    clock = pygame.time.Clock()
    fall_speed = 0.27
    fall_time = 0
    return clock, fall_speed, fall_time

def set_up_screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("Tetris")
    return screen

def main():
    screen = set_up_screen()
    clock, fall_speed, fall_time = set_up_clock()

    shape_list = [S_strategy(), Z_strategy(), I_strategy(), O_strategy(), J_strategy(), L_strategy(), T_strategy()]
    current_shape = shape().get_shape(shape_strategy= random.choice(shape_list))
    next_shape = shape().get_shape(shape_strategy= random.choice(shape_list))

    used_coordinates = {}

    change_piece = False
    run = True

    while run:
        grid = create_grid(used_coordinates)
        fall_time += clock.get_rawtime()
        clock.tick()

        # Shape falling
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_shape.y += 1

            if not (valid_space(current_shape, grid)) and current_shape.y > 0:
                current_shape.y -= 1
                change_piece = True

        check_events(current_shape, grid)
        shape_pos = convert_shape_format(current_shape)

        grid = update_grid(shape_pos, grid, current_shape)

        if change_piece:
            current_shape, next_shape, change_piece = shape_locked(shape_pos, used_coordinates, shape_list, current_shape, next_shape)
            clear_rows(grid, used_coordinates)

        draw_window(screen, grid)
        draw_next_shape(next_shape, screen)
        pygame.display.update()

        # Check if user lost
        if check_lost(used_coordinates):
            run = False

    draw_text_middle("You Lost", 40, (255,255,255), screen)
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()