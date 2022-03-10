# pole_chudes
This is a console game called "Field of Dreams"

## Rules
There is a word that you need to guess. You can guess the word itself or all of its letters.
You have several moves (number of letters in the word * 3).

## Game structure
In the beginning of the game and after each move, the word that you need to guess is printed to the console (with "\*" instead of unguessed letters).
In each move, the user inputs a letter or a word with the same number of letters as in the word that the user needs to guess.
The register of the input doesn't matter. If the user has inputted something else, they see a message about it in the console. This action is also a move.
If the user hasn't guessed the letter or the word, they also see a message about it in the console.

If the user has guessed a letter, all the guessed letters in the word open. If the user has guessed the word, they see a win message in the console.

## Commands
The user can also input commands. A command is not a move.

A list of possible commands:
- **!moves** - show the number of moves
- **!left** - show letters that are left in the alphabet
- **!used** - show used letters and words
- **!used_letters** - show used letters
- **!used_words** - show used words
- **!give_up** - give up and show the word
- **!help** - show possible commands
