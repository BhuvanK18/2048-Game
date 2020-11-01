#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random

#Starts the game by making a null 4x4 matrix

def start_game():
    
    mat = []
    for i in range(4):
        mat.append([0]*4)
    
    return mat

#Randomly places 2 in one of the spaces of the original matrix

def add_new_2(mat):
    
    r = random.randint(0,3)
    c = random.randint(0,3)
    while (mat[r][c] != 0):
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2

def reverse(mat):

    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range (4):
            new_mat[i].append(mat[i][4-j-1])
    
    return new_mat

def transpose(mat):
    
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    
    return new_mat

def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j!=pos:
                    changed = True
                pos+=1
    
    return new_mat,changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j]*2
                mat[i][j+1] = 0
                changed = True
    return mat,changed

#When the user moves up

def move_up(grid):
    
    transposed_grid = transpose(grid)
    new_grid,changed1 = compress(transposed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = transpose(new_grid)
    
    return final_grid,changed

#When the user moves down

def move_down(grid):
    
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    
    return final_grid,changed
                

#When the user moves left

def move_left(grid):
    
    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    
    return new_grid,changed

#When the user moves right

def move_right(grid):
    
    reversed_grid = reverse(grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = reverse(new_grid)
    
    return final_grid,changed

#Provides the info about when to end the game

def get_current_state(mat):
    
    #Check for 2048 in matrix
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048):
                return 'WON'
    
    #Check for 0 in matrix
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0):
                return 'GAME NOT OVER'
    #Check for consecutive similar digits in every row and column except last row and column
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return 'GAME NOT OVER'
    #Check for last row
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'GAME NOT OVER'
        
    #Check for last column
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'GAME NOT OVER'
    #If no matrix satisfies any of the above conditions the game is lost
    return 'LOST'


# In[18]:


mat = start_game()
print(mat)


# In[19]:


add_new_2(mat)
print(mat)


# In[21]:


mat = move_down(mat)
print(mat)


# In[15]:





# In[ ]:




