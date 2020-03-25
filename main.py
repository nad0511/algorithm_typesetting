import pandas as pd
import math
import copy
import numpy as np
from scipy.ndimage.measurements import label
from scipy.ndimage.morphology import binary_dilation, binary_fill_holes, binary_closing, binary_erosion

def calculate_parameter_boundary(grid):
    boundary = copy.deepcopy(grid)
    sum = 0
    row = len(boundary)
    col = len(boundary[0])
    k = [[0,1,0],[1,1,1],[0,1,0]]
    #fill hole
    boundary1 = binary_fill_holes(boundary).astype(int)
    #extract boundary
    boundary1 = binary_dilation(boundary1==0,k) & boundary1
    for j in range(row):
        for i in range(col):
            if 0 != boundary1[j][i]:
                sum += 1
    print(boundary1)
    return sum

def gap_detect(grid):
    cp = (copy.deepcopy(grid).astype(bool)).astype(int)
    k = [[1,1,1,1,1]]
    horizontal = binary_dilation(cp,k).astype(int)
    print (horizontal)
    horizontal1 = binary_erosion(horizontal,k)
    gap = horizontal1 - cp
    return gap



def find_empty_hole(grid):
    A= grid
    row=len(A)
    col=len(A[0])
    # structure = np.ones((3, 3), dtype=np.int).astype(int)
    # structure[0][0]=0
    # structure[0][2]=0
    # structure[2][0]=0
    # structure[2][2]=0
    Z = [[0 for x in range(col)] for y in range(row)]
    for r in range(row):
        for c in range(col):
            if A[r][c]==0:
                Z[r][c]=1
    lab, ncom = label(Z)
    #if ncom>1:
    #    indi=1

    empty = ncom
    return lab, empty



def calculator_border_len(grid) -> int:
    n = len(grid)
    m = len(grid[0])
    border = [0 for i in range(m)]
    height = 0

    length = 0
    # search border
    for j in range(m):
        for i in reversed(range(n)):
            if grid[i][j] == 0:
                continue
            border[j] = i
            break
    # calculate length of simple line (ignore hole)
    for j in range(m - 1):
        # add square root to differ convex roughness
        height +=  int(math.sqrt(abs(border[j] - border[j + 1]))*5)
    length = height + len(border)
    print(length)
    #find area of holes
    ext = np.zeros(m,dtype=int)
    extent = copy.deepcopy(grid)

    # extent = np.append(extent, [ext], axis=0 )
    k = [(1, 1 ,1 ,1,1),(1, 1 ,1 ,1,1), (1,1,0, 1, 1),(1, 1 , 1,1,1), (1, 1 , 1,1,1),]
    print("before: ", extent)
    extent = binary_closing(extent,structure=k).astype(int)
    print("after: ",extent)
    lable, empty = find_empty_hole(extent)
    S = [0] * (empty - 1)
    for index in range(1,empty):
        for j in range(m):
            for i in range(n):
                if index == lable[i][j]:
                    S[index-1] += 1
    print(S)
    parameter =  calculate_parameter_boundary(grid)
    print("parameter: ",parameter)
    coe_para_area = int(parameter/(np.amax(S))*100)
    print(coe_para_area)

    empty_hole = (empty-1) *50

    #calculate roughness
    grid_separate_hole = copy.deepcopy(grid)

    # for j in range(m):
    #     for i in reversed(range(n)):
    #         if grid_separate_hole[(i,j)] == 0:
    #             grid_separate_hole[(i,j)] = 1
    #             continue
    #         if grid_separate_hole [(i,j)] != 0:
    #             break

    # lab,ncom = find_empty_hole(grid_separate_hole)
    #
    # roughness = ncom*30
    #
    # length += roughness
    # print(length)

    length += empty_hole + coe_para_area

    return length





mat = pd.read_csv("test.csv")

a = mat.values
print(a)

row=len(a)
col=len(a[0])

gap = gap_detect(a)
print(gap)