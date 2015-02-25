# Tournament Results

## Table of contents

- [About Tournament Results](#About)
- [Requirements to Run the Tournament Results](#Requirements to Run the Tournament Results)
- [Run the Tournament Results](#documentation)
- [Successful tests output](#Successful tests output)
- [Documentation](#Documentation)
- [Author](#Author)

## About Tournament Results Project
This project uses a Python module which in turn uses the PostgreSQL database to keep track of players and matches in a game tournament.
The game tournament uses the [Swiss system](https://en.wikipedia.org/wiki/Swiss-system_tournament) for pairing up players in each round: players are not eliminated, and each player is paired with another player with the same number of wins, or as close as possible.

### Requirements to Run the Tournament Results
- Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
	- Follow the guidelines [here](https://www.udacity.com/wiki/ud197/install-vagrant) to set up the virtual environment
- Clone this repository [here](https://github.com/CruzanCaramele/Tournament-Results.git) from GitHub

### Running the Tournament Results
The aim for this is to run tournament_test.py file which contains unit tests that will test the functions within tournament.py file

- Launch the terminal program on your computer e.g git bash on Windows
- Navigate to the Vagrant folder from the terminal:
	- hp (master *) vagrant $

- type in the command " vagrant up ":
	- hp (master *) vagrant $ vagrant up
		- Once this is up, you'll get the message: "Machine booted and ready!"

- type in the command " vagrant ssh "
	- hp (master *) vagrant $ vagrant ssh

- change directory to the tournament folder:
	- vagrant@vagrant-ubuntu-trusty-32:~$ cd /vagrant/tournament
	- vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$

- finally to run the unti tests on the database, type in " python tournament_test.py":
	- vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
	
- a sample successful output of the tests is:

#### Successful tests output :
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
-  Old matches can be deleted.
-  Player records can be deleted.
-  After deleting, countPlayers() returns zero.
-  After registering a player, countPlayers() returns 1.
-  Players can be registered and deleted.
-  Newly registered players appear in the standings with no matches.
-  After a match, players have updated standings.
-  After one match, players with one win are paired.

Success!  All tests pass!


## Documentation
For complete Documentation on the Tournament Results project, click [here]()
This includes details on:
	- Code templates
	- the databse design
	- Python functions used in the code template


## Author

**Hamza Yahaya**

- <https://github.com/cruzancaramele>
