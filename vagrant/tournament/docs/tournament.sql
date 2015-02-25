-- Table definitions for the tournament project.

-- players table, includes name and id of players

CREATE TABLE players ( player_id SERIAL PRIMARY KEY,
					   player_name TEXT NOT NULL);



-- matches table, includes the matches played, uniquely identified
-- by IDs

-- the IDs of the winners and losers of the
-- individual matches

CREATE TABLE matches ( match_id SERIAL,
					   winner_id INTEGER REFERENCES players(player_id),
					   loser_id INTEGER REFERENCES players(player_id));