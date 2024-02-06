from typing import List

import pygame
from tile import Tile, random_tile

import random


def get_none_grid(rows, cols):
    grid = []
    for row in range(rows):
        new_row = []
        for col in range(cols):
            new_row.append(None)
        grid.append(new_row)

    return grid


def get_frontier(grid, filled_coordinates):
    frontier = list()

    for filled_coordinate in filled_coordinates:
        row, col = filled_coordinate
        if row > 0 and grid[row - 1][col] is None and (row - 1, col) not in frontier:
            frontier.append((row - 1, col))
        if row < (len(grid) - 1) and grid[row + 1][col] is None and (row + 1, col) not in frontier:
            frontier.append((row + 1, col))
        if col > 0 and grid[row][col - 1] is None and (row, col - 1) not in frontier:
            frontier.append((row, col - 1))
        if col < (len(grid[0]) - 1) and grid[row][col + 1] is None and (row, col + 1) not in frontier:
            frontier.append((row, col + 1))

    return frontier


def random_index_of_none(lst):
    """
    Return a random index of a None value in the list.

    :param lst: The list to search for None values.

    :return: Index of a None value, or None if there are no None values.
    """
    none_indices = [i for i, val in enumerate(lst) if val is None]
    if none_indices:
        return random.choice(none_indices)
    else:
        return None


class Grid:

    def __init__(self, cube_size: int, cubes_per_tile_side: int):
        self.cube_size = cube_size
        self.cubes_per_tile_side = cubes_per_tile_side
        self.tile_size = cube_size * cubes_per_tile_side
        self.grid = None

    def set(self, coordinates, tile):
        self.grid[coordinates[0]][coordinates[1]] = tile

    def fill_grid(self, screen, rows: int, cols: int):
        self.grid = get_none_grid(rows, cols)

        first_tile = random_tile(self.cube_size, self.cubes_per_tile_side)
        self.grid[0][0] = first_tile

        filled_coordinates = [(0, 0)]
        frontier = get_frontier(self.grid, filled_coordinates)

        while frontier:
            frontier = get_frontier(self.grid, filled_coordinates)
            random_frontier_coordinates = frontier.pop(
                random.randint(0, len(frontier) - 1))

            suitable_orientation = self.find_suitable_orientation(random_frontier_coordinates)
            suitable_tile = Tile(suitable_orientation, self.cube_size, self.cubes_per_tile_side)
            self.set(random_frontier_coordinates, suitable_tile)

            filled_coordinates.append(random_frontier_coordinates)
            self.draw(screen)

        pass

    def draw(self, screen: pygame.Surface):
        x_pos, y_pos = 0, 0

        for row in self.grid:
            for tile in row:
                if tile:
                    tile.draw(screen, x_pos, y_pos)
                x_pos += self.tile_size
            y_pos += self.tile_size
            x_pos = 0

    def find_suitable_orientation(self, coordinates) -> List[bool]:
        grid = self.grid
        row, col = coordinates

        above = grid[row - 1][col] if row > 0 else None
        right = grid[row][col + 1] if col < (len(grid[0]) - 1) else None
        below = grid[row + 1][col] if row < (len(grid) - 1) else None
        left = grid[row][col - 1] if col > 0 else None

        up = above.down if above else None
        right = right.left if right else None
        down = below.up if below else None
        left = left.right if left else None

        result = [up, right, down, left]

        while None in result:
            random_bool = random.choice([True, False])

            count_true = result.count(True)

            if count_true > 1:
                for i in range(len(result)):
                    if result[i] is None:
                        result[i] = random_bool
            else:
                none_index = random_index_of_none(result)
                result[none_index] = True

        return result
