def check_initial_point(grid, )

def find_initial_point(grid, priority):
    row = len(grid)
    col = len(grid[0])
    end = 0
    if (priority % 2):
        for col in reversed(range (len(grid[0]))):
            for row in range(len(grid)):
                if grid[row][col] == 0:
                    r = row
                    c = col
                    end = 1
                if end: break
            if end: break


    else:
        for col in range (len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col] == 0:
                    r = row
                    c = col
                    end = 1
                if end: break
            if end: break

    return r,c

def max_headline(current,total,ah_w, ah_h):
    max_heigth = 0
    max_width = 0
    for i in range(current,total+1):
        if (ah_h[i] >= max_heigth): max_heigth = ah_h[i]
        if (ah_w[i] >= max_width): max_width = ah_w[i]
    return max_width, max_heigth

def barrier(text1,text2):
    column = int(text2/(text2 + text1) * 70
    return column


def headline_placement()


