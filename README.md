This is an implementation that aims to be faithful to the original version of Hunt the Wumpus.

Here is how you build and run the Docker file:
Build the Docker image:
docker build -t wumpus-game .

Run the container:
docker run -it wumpus-game

There isn't really any sophisticated input validation and you have to rerun it to play again.
