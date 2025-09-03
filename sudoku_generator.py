"""
Sudoku Puzzle Generator Module

This module contains the core logic for generating Sudoku puzzles with varying
difficulty levels using advanced backtracking algorithms.

Features:
- Unique solution guarantee
- Difficulty-based generation (Easy, Medium, Hard, Insane)
- Backtracking solver with constraint propagation
"""

import time
import copy
import random


""" [Level of Difficulty] = The permitted levles of difficulty are ‘Easy’ ‘Medium’ ‘Hard’ and ‘Insane’. Outputs a sudoku of desired
        difficulty."""

class cell():
    """ Initilalizes cell object. A cell is a single box of a sudoku puzzle. 81 cells make up the body of a
        sudoku puzzle. Initializes puzzle with all possible answers available, solved to false, and position of cell within the
        sudoku puzzle"""
    def __init__(self, position):
        self.possibleAnswers = [1,2,3,4,5,6,7,8,9]
        self.answer = None
        self.position = position
        self.solved = False
        
    def remove(self, num): # we use this function to exclude emmited answers
        if num in self.possibleAnswers and self.solved == False:
            self.possibleAnswers.remove(num)
            if len(self.possibleAnswers) == 1: # if there is only one possible asnwer, and the puzzle has a solution then this must be the asnwer
                self.answer = self.possibleAnswers[0]
                self.solved = True
        if num in self.possibleAnswers and self.solved == True:
            self.answer = 0

    def solvedMethod(self):
        return self.solved

    def checkPosition(self):
        return self.position

    def returnPossible(self):
        return self.possibleAnswers

    def lenOfPossible(self):
        return len(self.possibleAnswers)

    def returnSolved(self):
        if self.solved == True:
            return self.possibleAnswers[0]
        else:
            return 0
        
    def setAnswer(self, num):
        if num in [1,2,3,4,5,6,7,8,9]:
            self.solved = True
            self.answer = num
            self.possibleAnswers = [num]
        else:
            raise(ValueError)
       
    def reset(self):
        self.possibleAnswers = [1,2,3,4,5,6,7,8,9]
        self.answer = None
        self.solved = False

def emptySudoku():
    ans = []
    for x in range(1,10):
        if x in [7,8,9]:
            intz = 7
            z = 7
        if x in [4,5,6]:
            intz = 4
            z = 4
        if x in [1,2,3]:
            intz = 1
            z = 1
        for y in range(1,10):
            z = intz
            if y in [7,8,9]:
                z += 2
            if y in [4,5,6]:
                z += 1
            if y in [1,2,3]:
                z += 0
            c = cell((x,y,z))
            ans.append(c)
    return ans

def printSudoku(sudoku): # this function returns the generated board
    board = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            board[i][j]=sudoku[i*9+j].returnSolved()
    return board
    


def sudokuGen():
    cells = [i for i in range(81)] ## our cells is the positions of cells not currently set
    sudoku = emptySudoku()
    while len(cells) != 0:
        lowestNum = []
        Lowest = []
        for i in cells:
            lowestNum.append(sudoku[i].lenOfPossible())  ## finds all the lengths of of possible answers for each remaining cell
        m = min(lowestNum)  ## finds the minimum of those
        for i in cells:
            if sudoku[i].lenOfPossible() == m:
                Lowest.append(sudoku[i])
        choiceElement = random.choice(Lowest)
        choiceIndex = sudoku.index(choiceElement) 
        cells.remove(choiceIndex)                 
        position1 = choiceElement.checkPosition()
        if choiceElement.solvedMethod() == False:  ##the actual setting of the cell
            possibleValues = choiceElement.returnPossible()
            finalValue = random.choice(possibleValues)
            choiceElement.setAnswer(finalValue)
            for i in cells:  ##now we iterate through the remaining unset cells and remove the input if it's in the same row, col, or box
                position2 = sudoku[i].checkPosition()
                if position1[0] == position2[0]:
                    sudoku[i].remove(finalValue)
                if position1[1] == position2[1]:
                    sudoku[i].remove(finalValue)
                if position1[2] == position2[2]:
                    sudoku[i].remove(finalValue)

        else:
            finalValue = choiceElement.returnSolved()
            for i in cells:  ##now we iterate through the remaining unset cells and remove the input if it's in the same row, col, or box
                position2 = sudoku[i].checkPosition()
                if position1[0] == position2[0]:
                    sudoku[i].remove(finalValue)
                if position1[1] == position2[1]:
                    sudoku[i].remove(finalValue)
                if position1[2] == position2[2]:
                    sudoku[i].remove(finalValue)
    return sudoku

def sudokuChecker(sudoku):
    for i in range(len(sudoku)):
        for n in range(len(sudoku)):
            if i != n:
                position1 = sudoku[i].checkPosition()
                position2 = sudoku[n].checkPosition()
                if position1[0] == position2[0] or position1[1] == position2[1] or position1[2] == position2[2]:
                    num1 = sudoku[i].returnSolved()
                    num2 = sudoku[n].returnSolved()
                    if num1 == num2:
                        return False
    return True

def perfectSudoku():
    result = False
    while result == False:
        s = sudokuGen()
        result = sudokuChecker(s)
    return s

def solver(sudoku, f = 0):
   
    if f > 900:
        return False
    guesses = 0
    copy_s = copy.deepcopy(sudoku)
    cells = [i for i in range(81)] ## our cells is the positions of cells not currently set
    solvedCells = []
    for i in cells:
        if copy_s[i].lenOfPossible() == 1:
            solvedCells.append(i)
    while solvedCells != []:
        for n in solvedCells:
            cell = copy_s[n]
            position1 = cell.checkPosition()
            finalValue = copy_s[n].returnSolved()
            for i in cells:  ##now we itterate through the remaing unset cells and remove the input if it's in the same row, col, or box
                position2 = copy_s[i].checkPosition()
                if position1[0] == position2[0]:
                    copy_s[i].remove(finalValue)
                if position1[1] == position2[1]:
                    copy_s[i].remove(finalValue)
                if position1[2] == position2[2]:
                    copy_s[i].remove(finalValue)
                if copy_s[i].lenOfPossible() == 1 and i not in solvedCells and i in cells:
                    solvedCells.append(i)
                ##print(n)
            solvedCells.remove(n)
            cells.remove(n)
        if cells != [] and solvedCells == []:
            lowestNum=[]
            lowest = []
            for i in cells:
                lowestNum.append(copy_s[i].lenOfPossible())
            m = min(lowestNum)
            for i in cells:
                if copy_s[i].lenOfPossible() == m:
                    lowest.append(copy_s[i])
            randomChoice = random.choice(lowest)
            randCell = copy_s.index(randomChoice)
            randGuess = random.choice(copy_s[randCell].returnPossible())
            copy_s[randCell].setAnswer(randGuess)
            solvedCells.append(randCell)
            guesses += 1
    if sudokuChecker(copy_s):
        if guesses == 0:
            level = 'Easy'
        elif guesses <= 2:
            level = 'Medium'
        elif guesses <= 7:
            level = 'Hard'
        else:
            level = 'Insane'
        return copy_s, guesses, level
    else:
        return solver(sudoku, f+1)
    
def solve(sudoku, n = 0):
    """ Uses the solver method to solve a puzzle. This method was built in order to avoid recursion depth errors. Returns True if the puzzle is solvable and
        false if otherwise"""
    if n < 30:
        s = solver(sudoku)
        if s != False:
            return s
        else:
            solve(sudoku, n+1)
    else:
        return False
    
def puzzleGen(sudoku):
    """ Generates a puzzle with a unique solution. """
    cells = [i for i in range(81)]
    while cells != []:
        copy_s = copy.deepcopy(sudoku)
        randIndex = random.choice(cells)
        cells.remove(randIndex)
        copy_s[randIndex].reset()
        s = solve(copy_s)
        if s[0] == False:
            f = solve(sudoku)
            print("Guesses: " + str(f[1]))
            print("Level: " + str(f[2]))
            return printSudoku(sudoku)
        elif equalChecker(s[0],solve(copy_s)[0]):
            if equalChecker(s[0],solve(copy_s)[0]):
                sudoku[randIndex].reset()
        else:
            f = solve(sudoku)
##            print("Guesses: " + str(f[1]))
##            print("Level: " + str(f[2]))
            return sudoku, f[1], f[2]

def equalChecker(s1,s2):
    """ Checks to see if two puzzles are the same"""
    for i in range(len(s1)):
        if s1[i].returnSolved() != s2[i].returnSolved():
            return False
    return True

def main(leve):
    level=leve
    print(level)

    t1 = time.time()
    n = 0
    if level == 'Easy':
        p = perfectSudoku()
        s = puzzleGen(p)
        if s[2] != 'Easy':
            return main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return printSudoku(s[0])
    if level == 'Medium':
        p = perfectSudoku()
        s = puzzleGen(p)
        while s[2] == 'Easy':
            n += 1
            s = puzzleGen(p)
            if n > 50:
                return main(level)
        if s[2] != 'Medium':
            return main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return printSudoku(s[0])
    if level == 'Hard':
        p = perfectSudoku()
        s = puzzleGen(p)
        while s[2] == 'Easy':
            n += 1
            s = puzzleGen(p)
            if n > 50:
                return main(level)
        while s[2] == 'Medium':
            n += 1
            s = puzzleGen(p)
            if n > 50:
                return main(level)
        if s[2] != 'Hard':
            return main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return printSudoku(s[0])
    if level == 'Insane':
        p = perfectSudoku()
        s = puzzleGen(p)
        while s[2] != 'Insane':
            n += 1
            s = puzzleGen(p)
            if n > 50:
                return main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return printSudoku(s[0])
    else:
        raise(ValueError)


