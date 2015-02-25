#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament

import bleach
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    PG = connect()
    cursor = PG.cursor()

    QUERY = "DELETE FROM matches;"

    cursor.execute(QUERY)
    PG.commit()
    PG.close()


def deletePlayers():
    """Remove all the player records from the database."""
    PG = connect()
    cursor = PG.cursor()

    QUERY = "DELETE FROM players;"

    cursor.execute(QUERY)
    PG.commit()
    PG.close()


def countPlayers():
    """Returns the number of players currently registered."""
    PG = connect()
    cursor = PG.cursor()

    QUERY = "SELECT COUNT (*) as totalPlayers FROM players;"

    cursor.execute(QUERY)
    total_players = cursor.fetchall()
    PG.commit()
    PG.close()
    return int(total_players[0][0])



def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    PG = connect()
    cursor = PG.cursor()

    """
     using 'bleach' to clean the data before inserting into the database.
     This ensures attacks such javaScript injections do not get executed. 
    """
    name = bleach.clean(name)

    QUERY = "INSERT INTO players (player_name) VALUES (%s);"
    data = (name,)

    cursor.execute(QUERY, data)
    PG.commit()
    PG.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    PG = connect()
    cursor = PG.cursor()


    """ 
        A subselect query that select player's name and id where 
        the player's id is matched against winner id in matches table
        to return the player's total wins and the player's id is matched
        with winner id and loser id in matches table in order to get the
        total number of matches by the player 
    """
    QUERY = "SELECT players.player_id, players.player_name,\
            (SELECT COUNT(*)\
            FROM matches\
            WHERE matches.winner_id = players.player_id) AS wins,\
            (SELECT COUNT(*)\
            FROM matches\
            WHERE players.player_id in (winner_id, loser_id)) AS matches\
            FROM players\
            ORDER BY wins DESC;"

    cursor.execute(QUERY)
    results = cursor.fetchall()
    PG.commit()
    PG.close()

    standings = [[int(row[0]), str(row[1]), int(row[2]), int(row[3])] for row in results]
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    PG = connect()
    cursor = PG.cursor()

    """
     using 'bleach' to clean the data before inserting into the database.
     This ensures attacks such javaScript injections do not get executed. 
    """
    winner = bleach.clean(winner)
    loser  = bleach.clean(loser)

    """ 
     appropraitely using query parameters to protect the database
     from SQL injection
    """
    QUERY = "INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s);"
    data  = (winner, loser,)

    cursor.execute(QUERY,data)
    PG.commit()
    PG.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    
    """this variable 'stands' is the list of tuples, each of which contains
        (id, name, wins, matches) of players
    """
    stands = playerStandings()

    """
     loop through the tuple pairing up the players and returns a list
     of tuple.
    """
    pairs = [(stands[ x-1 ][0], stands[ x-1 ][1], stands[ x ][0], stands[ x ][1])
            for x in range(1, len(stands), 2)]
    return pairs



