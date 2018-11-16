import random as rd

def create_grid(i): #i:taille de grille#
    game_grid = []
    D=[]
    for j in range (0,i):
        D.append(' ')
    for j in range (0,i):
        H=D[:]
        game_grid.append(H)

    return(game_grid)

def grid_add_new_tile_at_position(grid,x,y):
    new_tile=2*rd.randint(1,2)
    (grid[x][y])=new_tile
    return(grid)

def get_all_tiles(grid):
    tiles=[]
    for i in grid:
        for j in i:
            if j==' ' or j==0:
                tiles.append(0)
            else:
                tiles.append(j)
    return(tiles)

def length(grid):
    return len(grid[0])

def get_empty_tiles_positions(grid):
    empty_tiles=[]
    for longueur in range(0,length(grid)):
        for largeur in range(0,length(grid)):
            if (grid[longueur])[largeur] in (0,' '):
                empty_tiles.append((longueur,largeur))
    return(empty_tiles)


def grid_get_value(grid,x,y):
    if grid[x][y] in (0,' '):
        return(0)
    else:
        return(grid[x][y])

def get_new_position(grid):
    empty_tiles_position=get_empty_tiles_positions(grid)
    position=rd.randint(0,len(empty_tiles_position)-1)
    return(empty_tiles_position[position])

def grid_add_new_tile(grid):
    x,y=get_new_position(grid)
    grid=grid_add_new_tile_at_position(grid,x,y)
    return(grid)

def init_game(n):
    grid=create_grid(n)
    (x,y)=get_new_position(grid)
    grid=grid_add_new_tile_at_position(grid,x,y)
    (x,y)=get_new_position(grid)
    grid=grid_add_new_tile_at_position(grid,x,y)
    return(grid)
