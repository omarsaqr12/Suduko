I will be adding 
1-) a hint function by modifying solving_gui function
2-) I will modify the very naive genrate_board to a more complex algorithm which creates different level of difficulties using either:
a-)including 10 rules of suduko which determine the difficulty of the puzzle, we will see the minimum number of rules to solve the puzzle, and accordingly we will assign a value
b-) using mathematical models:
i_)
https://www.researchgate.net/publication/41940718_The_Model_and_Algorithm_to_Estimate_the_Difficulty_Levels_of_Sudoku_Puzzles

ii_) https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=D7B836A087983F111392D1E2CA32AB1F?doi=10.1.1.437.9472&rep=rep1&type=pdf

iii_) 
https://www.researchgate.net/publication/261217550_Difficulty_Rating_of_Sudoku_Puzzles_An_Overview_and_Evaluation



Finally, I decided to make the algorithm depend on the number of guesses that the user has to make in order to solve the puzzle. This can be considered an oversimplification, but if we look at it from the point of view of the number of inputs, we will have to study the distribution of the squares, not just the numbers, which will make this more of a mathematical research problem. This is considered an oversimplification for several reasons:
1-) There are difficult puzzles that can be solved without guessing, but you need to know where to start solving which makes this more difficult. Current research estimates how many steps a human solver will need to take to solve a puzzle.
2-) This follows from the previous discussion, but one might take the positioning of the numbers with respect to each other into consideration.