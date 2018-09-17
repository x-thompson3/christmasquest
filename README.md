# Christmas-Quest-2018
Codebase for Christmas Quest 2018, an ARG built for my siblings for Christmas

## General Outline
As part of this Christmas experience, I have designed a Twitter bot that will publish tweets containing puzzles or riddles, and a GameEngine class that will keep track of the "game state" - current puzzle, its solution, and a reference to the files that contain the storyline.

The whole program will be running on a Raspberry Pi, acting as a server for the bot.

### Twitter Bot
The Twitter Bot will be sending tweets from its own account, with each tweet containing the current puzzle/riddle/clue. It is also listening for any tweets that match the following conditions:
1. @ it in the tweet message text
2. Uses one of the following commands somewhere in the tweet text: `!ans` or `!choice`

It will take those tweets and pass the message text and command over to the game engine, then send a tweet with the response (some story text snippet, or another clue, etc).

### Game Engine
The Game Engine will be used to keep track of the state of the game. It holds a reference to the directory of the storyline, and handles all answer-checking and processing of actions. It holds the file index of the current puzzle, as well as the answer set for that puzzle. See the Game Engine class for more in-depth documentation.

## A Brief Note
If you're one of my siblings reading ahead of this to try and get any FUTURE HINTS, nice try! But because I admire your moxy and creativity, keep an eye on the `The_Story_Thus_Far.log` file to track your progress, and maybe another file will pop up as Christmas draws closer!
