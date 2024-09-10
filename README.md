
The Stellar Journey Game
 
The player controls the USS Endeavour spaceship and has the goal of eliminating all Blingon ships from a sector of the galaxy. The game is played in several turns, as described by the following rules:
1. When the game is started, display the sector of the galaxy according to the following rules:

	a.The game takes place on an 8x8 grid, having marked columns (1-8) and rows (A-H).

	b. Exactly ten stars are randomly placed in the sector, so that no 2 stars overlap, and no 2 stars are adjacent to each other on row, column, or diagonal.

	c. The player's ship, the USS Endeavour starts in a random square of the grid that has no stars. The ship is represented as E.

	d. Three Blingon cruisers are placed randomly on empty squares of the grid. They must not overlap each other, the player's ship, or a star. The player can see only the ships directly adjacent to the 		   Endeavour

2. The game is played in several turns. Each turn, the player can give one of the following commands:

   
	a.warp <coordinate> (e.g., warp G5). Moves the ship to the new coordinate. The new coordinate must be on the same row, column, or diagonal as the starting position (e.g., from A1 you can warp to C3, but not to C4). In case a star is in the way, the program displays an error message, and the ship is not moved. In case Endeavour would land on an enemy ship, the Endeavour is destroyed and the game is over. In case the command format or destination is invalid, an error message is displayed.

	b. fire <coordinate>. Destroy the Blingon ship at the given coordinates (e.g., fire B4). The fire command only works for ships adjacent to the player's ship. If the wrong coordinates are provided, an error message is displayed.

	c. cheat. This displays the playing grid, with remaining Blingon ships revealed.

4. Every time a Blingon ship is destroyed, the remaining ones reposition randomly, making sure that constraints given at 1.d are observed.
5. The player wins by destroying all enemy ships. 


Example commands:
The cheat command reveals enemy ships

a. warp B3, followed by warp E3, followed by warp H6 (if no enemy ships are on those squares)

b. cheat

