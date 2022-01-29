"""
Programming assessment code for Job Application

I began by drawing out a 3*3 grid in Excel with index numbers.
I used this grid for visualising the functions.
"""

## FUNCTIONS

def grid_init(n):
    """
    Function to initialise a grid string in python

    Parameters
    n - represents the size of the grid
    """

    ## initialise row strings
    even_row = "+"
    odd_row = "|"

    ## Create the rows for grid of size n
    iter1 = 1
    while iter1 < n+1:
        even_row += "--+"
        odd_row += "  |"
        iter1 += 1

    ## Put the rows together in a grid string
    grid_string = even_row + "\n"
    for i in range(n):
        grid_string += odd_row + "\n" + even_row + "\n"

    return(grid_string)


## Define a class for the grid

class Grid:

    ## When the class is called a grid of size n is created
    def __init__(self, n=1) -> None:
        self.grid_str = grid_init(n)
        self.grid_size = n
        self.grid_firstrow = (n * 3) + 1 ## First grid row different as it starts at 0
        self.grid_rowlength = (n * 3) + 2 


    def delete_v(self, i, j):
        """
        Function to remove vertical border

        i - row
        j - column
        """
        
        ## Calculate index of border to remove
        border_rowloc = (j * 3) + 1
        border_strindex = self.grid_firstrow + (self.grid_rowlength * ((i * 2) - 2)) + border_rowloc

        ## Remove border
        ### Use grid defined in class
        grid1 = self.grid_str
        ### replace the border with an empty space
        gridReplace = grid1[:border_strindex] + " " + grid1[border_strindex+1:]
       
        self.grid_str = gridReplace


    def delete_h(self, i, j):
        """
        Function to remove horizontal border

        i - row
        j - column
        """
        
        ## Calculate index of border to remove
        border_rowloc = ((j-1) * 3) + 2
        border_strindex = self.grid_firstrow + (self.grid_rowlength * ((i * 2) - 1)) + border_rowloc

        ## Remove border
        ### Use grid defined in class
        grid1 = self.grid_str
        ### replace the border with an empty space
        gridReplace = grid1[:border_strindex] + "  " + grid1[border_strindex+2:]
       
        self.grid_str = gridReplace

    def delete_corner(self, i, j):
        """
        Function to remove corner

        i - row
        j - column
        """
        
        ## Calculate index of border to remove
        border_rowloc = (j * 3) + 1
        border_strindex = self.grid_firstrow + (self.grid_rowlength * ((i * 2) - 1)) + border_rowloc

        ## Remove border
        ### Use grid defined in class
        grid1 = self.grid_str
        ### replace the border with an empty space
        gridReplace = grid1[:border_strindex] + "  " + grid1[border_strindex+2:]
       
        self.grid_str = gridReplace


    def delete_isec(self, i, j):
        """
        Function to remove intersection

        i - row
        j - column
        """

        ## Call horizontal and vertical functions twice
        self.delete_h(i,j)
        self.delete_h(i,j+1)
        self.delete_v(i,j)
        self.delete_v(i+1,j)
        self.delete_corner(i,j)

        

## MAIN

def main():
    
    ## Exercise A and C
    grid1 = Grid(5)
    #print(grid1.grid_str)
    #print(grid1.grid_size)

    ## Exercise B and C
    grid1.delete_v(2,3)
    #print(grid1.grid_str)

    grid1.delete_h(4,3)
    #print(grid1.grid_str)

    grid1.delete_isec(2,3)
    print(grid1.grid_str)


if __name__ == "__main__":
    main()