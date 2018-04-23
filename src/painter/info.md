the BasePainter class consists of 4 different functions:
- draw_current_state
- draw_win_state
- draw_lose_state
- get_new_guess

The draw_current_state function provides the terminal with the different figures. These figures are determined by the number of faults a player has made, numFails. The numFails used in this function should be the max number of fails - 1, as the final fail will invoke the draw_lose_state function.

The draw_win_state function is called when a player has guessed the word correctly. this function draws a win figure and outputs a congratulation together with the word.

The draw_lose_state function is called when the max number of fails is reached, this number of fails is recorded by the controller. When the function is called it outputs the final figure together with the word which had to be guessed.

The get_new_guess function gets called after every turn and prints a line in which the player is asked for his next guess.  

Furthermore there exists multiple painters which should be separately called from the controller based on the choice the player has made. these choices are:
- difficulty, easy, standard, hard
- alternatives, e.g. spaceman

for the difficulty the standard game of hangman consists of a maxNumFails of 8. the easy game has 12 maxNumFails and the hard game has only 6 maxNumFails.

alternatives could also make use of the difficulty but for now are implemented with the standard game in mind. The alternatives print different figures than the standard hangman game.
