from draw import draw


def main():

    cube_size = 3
    cubes_per_tile_side = 5
    tile_size = cube_size * cubes_per_tile_side
    rows = 40
    cols = 40

    width = cols * tile_size
    height = rows * tile_size


    # Draw a black square of size 1920x1080 with a tile in the center
    draw(width, height, cube_size, cubes_per_tile_side, rows, cols)

if __name__ == '__main__':
    main()


