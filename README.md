## Rock-Paper-Scissors

Simple game of rock-paper-scissors against the computer.

Starts with a simple greeting followed by asking for player input using <b><i>player_pick()</i></b> function to choose between:
* rock
* paper
* scissors

Computer selection is done in the <b><i>computer_pick()</i></b> function where a random number is generated and based on the value of given number one of the choices will be asigned to computer.

## Winning Scenarios
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

If both player and computer have the same choice, it is a draw

## Side note and Ending the game
- <b><i>player_pick()</i></b> function<br>
function will continue to be called if input is not from the 3 choices:
	- rock
	- paper
	- scissors
- <b><i>replay()</b></i><br> 
will provide option to continue playing or to stop<br>
function will continue to be called if input is not:
	- yes
	- no

