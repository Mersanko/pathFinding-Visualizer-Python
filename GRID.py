import pygame

# creating a window of Width=800 title=Visualization Window
width=800
window=pygame.display.set_mode((width,width))
pygame.display.set_caption("Visualization Window")

# Initialize COLORS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# create dataType or class which has row,col,color,x,y,neighbours list, width, totalRow etc variable.
# getPos(), draw(), neighbours() and __lt__() function, where getPos() gives position of object's row and column.
#draw() function draw rectangle according to color, x,y, width which basically represent a cell.
#neighbours() decide which cells are neighbors and then store them.
# __lt__() function just return false when comapring two objects.

class Cell:
    def __init__(self, row, col, width, totalRows):
        self.row=row
        self.col=col
        self.width=width
        self.totalRows=totalRows
        self.x=row*width
        self.y=col*width
        self.color=WHITE
        self.neighbors=[]
        self.visited=False

        

    def getPos(self):
        return self.col, self.row
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))
    
    """ (0,0)


                row-1
        col-1   cell    col+1
                row+1


    (y,x)
    """
    # the condition of being barrier is- color of barrier is always BLACK.
       
    def neighborsOf(self, grid):
        self.nbrs=[]    

        #   upper nbr - row-1
        # if cell has row not 0 then it does not have upper cell
        # if upper cell is not barrier then append the upper cell as neighbour.
        if self.row>0 and not grid[self.row-1][self.col].color == BLACK:
            self.nbrs.append(grid[self.row-1][self.col])

        #   bottom nbr - row+1
        # if cell is not the last row then it has buttom row
        # if bottom cell is not barrier then append the bottom cell as neighbour.
        if self.row< self.totalRows-1 and not grid[self.row+1][self.col].color==BLACK:
            self.nbrs.append(grid[self.row+1][self.col])
        #   left nbr - col-1
        # if cell is not the first col then it has left cell
        # if left cell is not barrier then apend the left cell as neighbour.
        if self.col>0 and not grid[self.row][self.col-1].color==BLACK:
            self.nbrs.append(grid[self.row][self.col-1])
        #   right nbr - col+1
        # if cell is not the last col then it has right cell
        # if right cell is not barrier then apend the right cell as neighbour.
        if self.col < self.totalRows-1 and not grid[self.row][self.col+1].color==BLACK:
            self.nbrs.append(grid[self.row][self.col+1])

    def __lt__(self, other):
        return False

"""
rows=8:-
each cell contains Cell object, each Cell object contains  row,col,color,x,y,neighbours list, width, totalRow etc variables and getPos(), draw(), neighbours() and __lt__() functions.


            0          1          2          3          4         5          6           7
    0-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    1-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    2-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    3-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    4-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    5-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    6-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]
    7-[[cellOBJ0] [cellOBJ1] [cellOBJ2] [cellOBJ3] [cellOBJ4] [cellOBJ5] [cellOBJ6] [cellOBJ7]]

""" 
def twoDmatrix(rows, width):
    grid=[]
    gap=width//rows # integer division
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cellOBJ= Cell(i,j,gap,rows)
            grid[i].append(cellOBJ)
    return grid


def drawGrid(window,grid, rows, width):
    window.fill(WHITE)
    for eachrow in grid:
        for eachcolumn in eachrow:
            eachcolumn.draw(window)# Draw Rectengale

    # Draw lines- Rows and Cols wise on top of - rectengales or cells
    gap=width//rows
    for i in range(rows):
        pygame.draw.line(window, BLACK,(0, i*gap),(width, i*gap))
        for j in range(rows):
            pygame.draw.line(window, BLACK,(j*gap,0),(j*gap, width))
    pygame.display.update()

def cellIndicator(pos, rows, width):
    # Indicate which cell is clicked by Mouse
    # pos contains the x,y coordinate of window.
    gap=width//rows
    y,x=pos
    row=y//gap
    col=x//gap
    return row, col
def algorithmB(drawGrid,grid, start, end):
    ar=[]
    ar.append(start)
    while len(ar)!=0:
        curentCell=ar.pop(0)
        if not curentCell.visited:
            curentCell.visited=True
            if curentCell != end:
                curentCell.color=YELLOW
            for ns in curentCell.nbrs:
                if(ns.visited==False):
                    ar.append(ns)
        drawGrid()



def main(window, width):
    alg="BFS"
    Rows=20
    # 1st step- create the 2D matrix. Each cell contains Cell object
    grid= twoDmatrix(Rows, width)
    #
    start=None
    end=None
    run=True
    while run:
        # 2nd step- draw the Grid
        drawGrid(window, grid, Rows, width)
        # from here we basically create the logics of -how to close window, -mouse clicking events, -key press events -runing the algorithm
        # 3rd step- Events handeling
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run = False

        # Left mouse button press
            if pygame.mouse.get_pressed()[0]:
                positionOfXandY=pygame.mouse.get_pos()# get coordinates
                row, col=cellIndicator(positionOfXandY, Rows, width)# get cell's row and col
                curentCell=grid[row][col]
                # if start and stop are not pointed in grid then first point start then end 
                if not start and curentCell != end:
                    #make curentCell as start
                    start= curentCell
                    # Initialized color ORANGE to start
                    start.color=ORANGE
                elif not end and curentCell != start:
                    #make curentCell as end
                    end= curentCell
                    # Initialized color TURQUOISE to end
                    end.color=TURQUOISE
                # now after start and end is pointed then barriera are pointed
                elif curentCell !=end and curentCell != start:
                    # Initialized color BLACK to curentCell 
                    curentCell.color=BLACK

        # Right mouse button pressed
            elif pygame.mouse.get_pressed()[2]:
                positionOfXandY= pygame.mouse.get_pos()
                row, col= cellIndicator(positionOfXandY, Rows, width)
                curentCell = grid[row][col]
                # just change the color to resetl cell which is initialize before
                curentCell.color= WHITE
                # now after reset modify start and end if the currentcell is start or end
                if curentCell==start:
                    start=None
                elif curentCell==end:
                    end=None

        #Space key pressed        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for eachrow in grid:
                        for eachcolumn in eachrow:
                            eachcolumn.neighborsOf(grid)
                    if "BFS" == alg:
                        algorithmB(lambda: drawGrid(window, grid, Rows, width), grid, start, end)
                    elif "DFS" == alg:
                        algorithmD(lambda: drawGrid(window, grid, Rows, width), grid, start, end)
                    elif "A*" == alg:
                        algorithmA(lambda: drawGrid(window, grid, Rows, width), grid, start, end)

                    
    pygame.quit()
main(window, width)
