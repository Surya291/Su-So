from tkinter import *
#from Sudoku_Solver import
from time import sleep


def Suso (top,sud):
    k = [0,0]
    if(not unassigned(sud,k)):
        return True

    r = k[0]
    c = k[1]
    i = 0
    for num in range(1,10):
        if (is_safe(sud,r,c,num)):
            print("lol")
            sud[r][c] = num
            print_maze(sud)
            top.update()
            top.after(10)
            print("hi")

            if Suso(top,sud):
                return True
            sud[r][c] = 0
    return False

def unassigned(sud,k):
    for r in range(0,9):
        for c in range(0,9):
            if (sud[r][c] == 0):
                k[0] = r
                k[1] = c
                return True
    return False

def check_in_row(sud,r,num):
    for c in range(0,9):
        if(sud[r][c]== num):
            return True
    return False

def check_in_col(sud,c,num):
    for r in range(0,9):
        if(sud[r][c]== num):
            return True
    return False

def check_in_grid(sud,r,c,num):
    row = r -(r%3)
    col = c - (c%3)
    for a in range(row,row+3):
        for b in range(col,col+3):
            if(sud[a][b] == num):
                return True
    return False
def is_safe(sud,r,c,num):
    return (not(check_in_grid(sud,r,c,num))and (not(check_in_row(sud,r,num))) and (not(check_in_col(sud,c,num))))



#######################################################
entries = []

def initialize(top,arr):
    E = entries[0]

    m=1
    for i in range(9):
        for j in range(9):
            if(not E.get()):
                arr[i][j] = 0
            else:
                arr[i][j] = int(E.get())
            if(m<=80):
                E = entries[m]
                m+=1

def print_maze(arr):
    clean_Mess()
    E = entries[0]
    m =1
    for i in range(9):
        for j in range(9):
            if(arr[i][j] != 0):
                E.insert(1,arr[i][j])
            if(m<=80):
                E = entries[m]
                m+=1
def clean_Mess():
    for e in entries:
        e.delete(0,END)
def play_Game(top,maze):
    initialize(top,maze)
    Suso(top,maze)

    if(Suso(top,maze)):
        print_maze(maze)
    else:
        print("Can't find a valid solution!!!")





def createGUI(maze):
    top = Tk()
    top.geometry("550x600")
    var = StringVar()
    label = Label(top, textvariable=var)



    top.title("SuSo a.k.a Sudoku Solver !!!")


    top.configure(background='lightyellow')
    #top.configure(background = 'black')
    canvas = Canvas(top,height=600,width = 550)
    canvas.configure(background = 'cyan')

    createRow(canvas)
    createCol(canvas)
    createEntry(top)
    createButtons(top,maze)
    canvas.pack(side = 'top')
    top.mainloop()


def createEntry(top):
    p,q=  55,55
    for i in range(9):
        for j in range(9):

            E = Entry(top,width = 30,font = 'VarelaRound 20 ')
            E.place(x=p,y = q , height = 40,width= 40)

            #E.pack()
            entries.append(E)

            p+=50
        q+=50
        p = 55


def createRow(canvas):
    i,j = 50,50
    p = 50
    q = 500
    for m in range(10):
        if (m%3 == 0):
            canvas.create_line(i,j,p,q,width = 6)
        else :
            canvas.create_line(i,j,p,q,width = 1.5)
        i+=50
        p+=50

def createCol(canvas):
    i,j=50,50
    p,q=500,50
    for m in range(10):
        if (m%3 == 0):
            canvas.create_line(i,j,p,q,width = 5)
        else :
            canvas.create_line(i,j,p,q,width = 2.5)
        j+=50
        q+=50

def createButtons(top,maze):
    button_solve = Button(top, text="SOLVE", justify='left', default='active', command = lambda: play_Game(top,maze))
    button_reset = Button(top, text="RESET", justify='right', command = lambda: clean_Mess())
    button_solve.place(x=100, y=525, height=50, width=100)
    button_reset.place(x=300, y=525, height=50, width=100)



maze = [[0 for x in range(9)]for y in range(9)]
createGUI(maze)

##############################################################
