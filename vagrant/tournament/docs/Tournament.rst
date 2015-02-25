Tournament  module (tournament.py)
==============================================
This is the Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.
This module contains several functions used to query the database. Below are the modules and the descriptions:


Functions in tournament.py
--------------------------------------
**registerPlayer(name)**

Adds a player to the tournament by putting an entry in the database. The database assigns an ID number to the player. Different players may have the same names but will receive different ID numbers.

**countPlayers()**

Returns the number of currently registered players. This function gets the database to count the players.

**deletePlayers()**

Clears out all the player records from the database.

**reportMatch(winner, loser)**

Stores the outcome of a single match between two players in the database.

**deleteMatches()**

Clears out all the match records from the database.

**playerStandings()**

Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

**swissPairings()**

Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function returns four pairings. This function uses playerStandings to find the ranking of players.