
 I decided to make the algorithm depend on the number of guesses the user has to make to solve the puzzle. This can be considered an oversimplification, but if we look at it from the point of view of the number of inputs, we will have to study the distribution of the squares, not just the numbers, making this more of a mathematical research problem. This is considered an oversimplification for several reasons:
1-) There are difficult puzzles that can be solved without guessing, but you need to know where to start solving them, which makes this more difficult. Current research estimates how many steps a human solver will need to take to solve a puzzle.
2-) This follows from the previous discussion, but one might consider the positioning of the numbers concerning each other.

Requirements:
pygame installation
Things to add: 
1-)convert this code to the extension, which can be used in the browser to help the users solve their puzzles
2-) For research purposes, we may compare the time of the backtracking solving algorithm on puzzles in old Suduko books where the difficulty level is judged by humans, and compare it to the time the algorithm takes to the puzzles with corresponding difficulties in our program
3-) Also, the generating function can be easily changed to assess the difficulty level of the inputted puzzle, and this assessed difficulty can be compared to the difficulty assigned to the puzzle by the human
4-) The algorithm may also run on graphs with the same number of initial vacant positions but different distribution and measure the time, which can be a project for a math modeling class

sources
i_)
https://www.researchgate.net/publication/41940718_The_Model_and_Algorithm_to_Estimate_the_Difficulty_Levels_of_Sudoku_Puzzles

ii_) https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=D7B836A087983F111392D1E2CA32AB1F?doi=10.1.1.437.9472&rep=rep1&type=pdf

iii_) 
https://www.researchgate.net/publication/261217550_Difficulty_Rating_of_Sudoku_Puzzles_An_Overview_and_Evaluation

iv-) https://github.com/JoeKarlsson/python-sudoku-generator-solver/tree/master, this is the source of generating puzzle with certain difficulty, I wrote the same algorithm, with view changes
v-) this project was inspired by the video of tech with tim, then new functionalities, such as the hint function, generating a suduko puzzle of desired difficulty, and allowing the user to select the desired level of difficulty 

other sources:
https://github.com/RutledgePaulV/sudoku-generator
https://gamedev.stackexchange.com/questions/56149/how-can-i-generate-sudoku-puzzles
https://sites.math.washington.edu/~morrow/mcm/team2306.pdf
https://stackoverflow.com/questions/10488719/generating-a-sudoku-of-a-desired-difficulty

