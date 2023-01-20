import numpy as np

def intro_array():
    array = np.array([[0,0,0],[0,0,0],[0,0,0]])
    #
    for x in range(0,3):
        for y in range(0,3):
            if x == y:
                array[x][y] = 1
            else:
                array[x][y] = 0

    #Outputting 1
    print(array)
    print("\n")

    for x in range(0,3):
        for y in range(0,3):
            if x == y:
                array[x][y] = 1
            else:
                array[x][y] = 3

    #Outputting 2
    print(array)
    print("\n")

    #Outputting 3
    array = np.delete(array, 2, 1)
    print(array)

if __name__ == "__main__":
    intro_array()