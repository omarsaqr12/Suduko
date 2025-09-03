import pygame as p
from solve import solve, valid,generate_board,find_empty
import time
p.font.init()
class grid:
    def __init__(self,width,height,level):
        self.board=generate_board(level) # we create the board
        self.rows=9
        self.cols=9
        self.width=width
        self.height=height
        self.cubes=[[Cube(self.board[i][j],i,j,width,height) for i in range(9)] for j in range(9)] # we define each cell of the grid as a cube as this will be benificial when we draw the board and change its state
        self.model=None
        self.selected=None
    def update_model(self):
        self.model=[[self.cubes[i][j].value for j in range (self.cols)]for i in range (self.rows)]  # we update the value of the cell
    def place(self,val): # we check if the entered value is valid or not
        row,col=self.selected
        if self.cubes[row][col].value==0:
            self.cubes[row][col].set(val)
            self.update_model()
            if valid(self.model,val,(row,col))and solve(self.model):
                return True
            else: 
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False
    def solve_gui(self,win): # we use this function to alllow the user to view the solution of the engine while stuck
        self.update_model()
        find = find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.model, i, (row, col)):
                self.model[row][col] = i
                self.cubes[row][col].set(i)
                self.cubes[row][col].draw_change(win, True)
                self.update_model()
                p.display.update()
                p.time.delay(100)

                if self.solve_gui(win):
                    return True

                self.model[row][col] = 0
                self.cubes[row][col].set(0)
                self.update_model()
                self.cubes[row][col].draw_change(win, False)
                p.display.update()
                p.time.delay(100)

        return False
    
    def hints(self,win): # we use this function to alllow the user to view the solution of the engine while stuck
        self.update_model()
        solution=[[self.model[i][j] for j in range (9)]for i in range (9)]
        solve(solution)
        find = find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find
        print("yeah")
        self.model[row][col]=solution[row][col]
        self.cubes[row][col].set(solution[row][col])
        self.cubes[row][col].draw_change(win, True)
        self.update_model()
        p.display.update()
        p.time.delay(100)
    
    def sketch(self,val): # this is the initial guess of the user, not the official one
        row,col=self.selected
        self.cubes[row][col].set_temp(val)
    def draw (self,win):
        gap=self.width/9
        for i in range(self.rows+1):
            if i%3==0 and i!=0:
                thick=4 #the boundary between the boxes
            else:
                thick=2 #the bondary between the cells
            p.draw.line(win, (200,1,1), (0, i*gap), (self.width, i*gap), thick) #the horizontal lines
            p.draw.line(win, (100, 0, 0), (i * gap, 0), (i * gap, self.height), thick)#the vertical lines
        for i in range (self.rows):
            for j in range (self.cols):
                self.cubes[i][j].draw(win) #we draw the cubes
    def select(self,row,col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected=False #to make sure only one cube is selected at a time
        self.cubes[row][col].selected=True
        self.selected=(row,col)
    def clear(self):
        row,col=self.selected
        if self.cubes[row][col].value==0:
            self.cubes[row][col].set_temp(0) # if the user deleted a value we want to set the initial guess ie temp to 0


    def click(self,pos):
        if pos[0]<self.width and pos[1]<self.height:
            gap=self.width/9
            x=pos[0]//gap
            y=pos[1]//gap
            return (int(y),int(x))
        else:
            return None
    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value==0:
                    return False
        return True
class Cube:
    rows=9
    cols=9
    def __init__(self,value,row,col,width,height):
        self.value=value
        self.temp=0
        self.row=row
        self.col=col
        self.width=width
        self.height=height
        self.selected=False
    def draw_change(self, win, g=True):
        fnt = p.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        p.draw.rect(win, (255, 255, 255), (x, y, gap, gap), 0)

        text = fnt.render(str(self.value), 1, (0, 0, 0))
        win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        if g:
            p.draw.rect(win, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            p.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set_temp(self,val):
        self.temp=val
    def set(self,val):
        self.value=val

    def draw(self,win):
        fnt=p.font.SysFont("comicsans",40)
        gap=self.width/9
        x=self.col*gap
        y=self.row*gap
        if self.temp!=0 and self.value==0:
            text=fnt.render(str(self.temp),1,(128,128,128))
            win.blit(text,(x+5,y+5))
        elif not(self.value==0):
            text=fnt.render(str(self.value),1,(0,0,0))
            win.blit(text,(x+gap/2-text.get_width()/2,y+gap/2-text.get_height()/2))
        if self.selected:
            p.draw.rect(win,(255,0,0),(x,y,gap,gap),3)

def redraw_window(win,board,time,strikes):
    win.fill((255,255,255))
    fnt=p.font.SysFont("comicsans",40)
    text =fnt.render("Time:"+format_time(time),1,(0,0,0))
    win.blit(text,(540-200,560-30))
    strikes=min(strikes,6)
    text=fnt.render("X "*strikes,1,(255,0,0))
    win.blit(text,(20,530))
    board.draw(win)
def format_time(secs):
    sec=secs%60
    minute=secs//60
    hour=secs//3600
    mat=" "+str(minute)+":"+ str(sec)
    return mat
def main(level):
    win=p.display.set_mode((540,600))
    p.display.set_caption("Sudoku")
    board=grid(540,540,level)
    key=None
    run=True
    start=time.time()
    strikes=0
    while run:
        play_time=round(time.time()-start)
        for event in p.event.get():
            if event.type==p.QUIT:
                run=False
            if event.type==p.KEYDOWN:
                if event.key==p.K_1:
                    key=1
                if event.key==p.K_2:
                    key=2
                if event.key==p.K_3:
                    key=3
                if event.key==p.K_4:
                    key=4
                if event.key==p.K_5:
                    key=5
                if event.key==p.K_6:
                    key=6
                if event.key==p.K_7:
                    key=7
                if event.key==p.K_8:
                    key=8
                if event.key==p.K_9:
                    key=9
                if event.key==p.K_DELETE:
                    board.clear()
                    key=None
                if event.key == p.K_SPACE:
                    board.solve_gui(win)   
                if event.key == p.K_h:
                    board.hints(win)             
                if event.key==p.K_RETURN:
                    i,j=board.selected
                    if board.cubes[i][j].temp!=0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes+=1
                        key=None
                        if board.is_finished():
                            print("Game over")
                            run=False
            if event.type==p.MOUSEBUTTONDOWN:
                pos=p.mouse.get_pos()
                clicked=board.click(pos)
                if clicked:
                    board.select(clicked[1],clicked[0])
                    key=None
        if board.selected and key!=None:
            board.sketch(key)
        redraw_window(win,board,play_time,strikes)
        p.display.update()
p.quit()