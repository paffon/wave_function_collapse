from grid import Grid
import pygame


def draw(width: int, height: int, cube_size: int,
         cubes_per_tile_side: int, rows: int, cols: int):
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((width, height))  # Create a display surface
    screen.fill((0, 0, 0))  # Fill the screen with black color

    grid = Grid(cube_size, cubes_per_tile_side)
    grid.fill_grid(screen, rows, cols)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
