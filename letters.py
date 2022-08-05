
#%% LETTER M
letter=""  
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
            letter=letter+"* "    
        else:      
            letter=letter+"  "    
    letter=letter+"\n"    
print(letter)


#%% LETTER S
letter="" 
for row in range(0,7):    
    for column in range(0,7):     
        if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or (column == 1 and (row == 1 or row == 2 or row == 6)) or (column == 5 and (row == 0 or row == 4 or row == 5))):  
            letter=letter+"*"    
        else:      
            letter=letter+" "    
    letter=letter+"\n"    
print(letter)

#%% LETTER D
letter=""
for row in range(0,8):
    for column in range(0,8):
        if (column == 0 or (column == 2 and (row == 0 or row == 7)) or (column == 4 and (row == 1 or row == 6)) or (column == 6  and (row == 2 or row == 5)) or (column == 7 and (row > 2 and row < 5))):
            letter=letter+"*"    
        else:      
            letter=letter+" "    
    letter=letter+"\n"    
print(letter)            