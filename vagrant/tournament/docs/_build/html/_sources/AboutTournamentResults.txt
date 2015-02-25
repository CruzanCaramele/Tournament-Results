About Tournament Results
==============================================
The game tournament uses the Swiss system for pairing up players in each round: players are not eliminated, and each player is paired with another player with the same number of wins, or as close as possible.
In this version , the database only support a single tournament at a time and the number of players in a tournament is an even number.This means that no player will be left out of a round.

Templates
--------------
The template file *tournament.sql* contains the database schema, in the form of SQL create table commands. Tables are given names that make sense in terms of the tournament, and the columns have descriptive names as well.

The template file *tournament.py* contains Python  code comprising several functions.

Finally, the file *tournament_test.py* contains unit tests that test the functions written in tournament.py. All tests pass for this tournament project.