This is a simple console based game of Rock, Paper, Scissors. The game will start automatically, type your choice, and the computer will play against you. You will see a scoreboard as well with the score between you and the computer. If you encounter an error saying that there is an EOF error, it is likely because the program is running in non-interactive mode. A method that has worked for me is running this command to start the program when in the project directory: "docker compose run --rm -it --build", where the -it tag is to activate Docker interactive mode in the console.


The URL to the Docker Hub image is the following: https://hub.docker.com/repository/docker/bananapie817/assignment/general
