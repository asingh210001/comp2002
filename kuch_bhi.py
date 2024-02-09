import numpy as np
import random



size_parameter_and_variable=[0,0]# index zero will store the current size of variable and index one will store the current size of the parameter

#variable = random.randint(0, 99)	
#parameter = random.randint(0,99)

def isEmtpy1(ram):
    i=0
    searching= True
    while i<= ram.len() or searching != False: # add condition for cheaking none
        if ram[i] is None:
            searching=False
        i=+1
    return False

def isEmtpy_variables(ram):
    if ram[63]==None:
        return True
    return False
def isEmpty_parameter():
    if ram[0]==None:
        return True
    return False

    
def allocate_parameter(ram):
    '''i=0
    searching= True
    while i<= 63 and searching != False: # add condition for cheaking none
        if ram[i] is None:
            ram[i]=random.randint(0, 99)
            searching = False
            size_parameter_and_variable[0]=size_parameter_and_variable[0] + 1
        i=+1
    if searching==True: # if no spacee is avialable
            print("no space available")'''
    if ram[size_parameter_and_variable[0]]==None:
        ram[size_parameter_and_variable[0]]= random.randint(0,9)
        size_parameter_and_variable[0]=size_parameter_and_variable[0]+1
    else:
        print("no space available")


def allocate_variable(ram):
    '''i=63
    searching= True
    while i>= 63 and searching != False: # add condition for cheaking none
        if ram[i] is None:
            ram[i]=random.randint(0, 99)
            searching = False
            size_parameter_and_variable[1]=size_parameter_and_variable[1] + 1
        i=-1

    if searching==True: # if no spacee is avialable
            print("no space available")'''
    if ram[63-size_parameter_and_variable[1]]==None:
        ram[63-size_parameter_and_variable[1]]= random.randint(0,9)
        size_parameter_and_variable[1]=size_parameter_and_variable[1]+1
    else:
        print("no space available")

def size_parameter():
    return size_parameter_and_variable[0]
def size_variable():
    return size_parameter_and_variable[1]


'''def free_variable(ram):
    temp = ram[0]
    ram[0]=None
    i=0
    while i<size_variable()-1:
        ram[i]=ram[i+1]
        ram[i+1]= None
        i=+1'''

def free_parameter(ram):
    temp = ram[0]
    ram[0]=None
    i=0
    while i<size_parameter()-1:
        ram[i]=ram[i+1]
        ram[i+1]= None
        i=+1
    size_parameter_and_variable[0]=size_parameter_and_variable[0]-1
    return temp

def free_variable(ram):
    temp = ram[63]
    ram[63]=None
    i=0
    '''i=63
    while i>63-(size_variable()):
        ram[i]=ram[i-1]
        ram[i-1]= None
        i=-1
    size_parameter_and_variable[1]=size_parameter_and_variable[1]-1
    return temp'''
    
    while i<int(size_variable()):
        ram[63-i]=ram[63-i-1]
        ram[63-i-1]=None
        i=i+1
    size_parameter_and_variable[1]=size_parameter_and_variable[1]-1
    return temp

        
def top_variable():
    return ram[0]

def top_parameter():
    return ram[63]

    


ram = np.empty(64, dtype=object) 
#ram[0] = 8
print(ram)
n=63

'''allocate_parameter(ram)
print(ram)
allocate_parameter(ram)
print(ram)
allocate_variable(ram)    
print(ram)
allocate_variable(ram)    
print(ram)
print(top_variable())
print(top_parameter())
free_parameter(ram)
print(ram)
print(size_variable())
free_variable(ram)
print(ram)
print(size_variable())
free_variable(ram) 
print(ram)
print(size_variable())'''

j=0
while j<=61:
    allocate_variable(ram) 
    j=j+1

allocate_parameter(ram)
allocate_parameter(ram)
allocate_parameter(ram)




print(ram)
print(size_parameter())
print(size_variable())
free_parameter(ram)
print(ram)
free_variable(ram)
print(ram)
print(size_variable())
