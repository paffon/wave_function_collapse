from dataclasses import dataclass
from typing import List
import pygame

import random


@dataclass
class Cube:
    size: int
    color: str


def random_tile_orientations():
    options_for_true_values = [
        [False, False, False, False],
        [True, True, False, False],
        [True, True, True, False],
        [True, True, True, True],
    ]
    random_choice = random.choice(options_for_true_values)
    random.shuffle(random_choice)

    return random_choice


def random_tile(cube_size: int, cubes_per_tile_side: int):
    return Tile(random_tile_orientations(), cube_size, cubes_per_tile_side)



class Tile:
    def __init__(self, up_right_down_left: List[bool], cube_size: int, cubes_per_tile_side: int):
        self.up = up_right_down_left[0]
        self.right = up_right_down_left[1]
        self.down = up_right_down_left[2]
        self.left = up_right_down_left[3]
        self.center = any(up_right_down_left)

        if cubes_per_tile_side % 2 == 0:
            raise ValueError('Cubes per grid side must be odd')

        def cube_color(bool_value: bool) -> str:
            return '#050505' if bool_value else '#773344'

        self.cubes_grid = []
        for row in range(cubes_per_tile_side):
            new_row = []
            for col in range(cubes_per_tile_side):
                if row < (cubes_per_tile_side - 1) / 2:
                    if col != (cubes_per_tile_side - 1) / 2:
                        new_row.append(Cube(cube_size, cube_color(False)))
                    else:
                        new_row.append(Cube(cube_size, cube_color(self.up)))
                elif row == (cubes_per_tile_side - 1) / 2:
                    if col < (cubes_per_tile_side - 1) / 2:
                        new_row.append(Cube(cube_size, cube_color(self.left)))
                    elif col == (cubes_per_tile_side - 1) / 2:
                        new_row.append(Cube(cube_size, cube_color(self.center)))
                    else:
                        new_row.append(Cube(cube_size, cube_color(self.right)))
                else:
                    if col != (cubes_per_tile_side - 1) / 2:
                        new_row.append(Cube(cube_size, cube_color(False)))
                    else:
                        new_row.append(Cube(cube_size, cube_color(self.down)))
            self.cubes_grid.append(new_row)

    def draw(self, screen: pygame.Surface, x_pos: int, y_pos: int):
        cube_size = self.cubes_grid[0][0].size
        for row in self.cubes_grid:
            x_pos_updating = x_pos
            for cube in row:
                pygame.draw.rect(screen, cube.color, (x_pos_updating, y_pos, cube_size, cube_size))
                x_pos_updating += cube_size
            y_pos += cube_size

        pygame.display.flip()  # Update the display

    def __repr__(self):
        return f'Tile[{self.up},{self.right},{self.down},{self.left}]'
