create database match_data;
use match_data;
-- FOUNDATIONAL TABLES (Teams, Coaches, Players, Matches)

-- Table: team
-- Purpose: Stores team information (2 teams per match)
CREATE TABLE team (
    team_id INT PRIMARY KEY AUTO_INCREMENT,
    team_name VARCHAR(100) NOT NULL UNIQUE
);

-- Table: coach
-- Purpose: Stores coach information linked to their team
CREATE TABLE coach (
    coach_id INT PRIMARY KEY AUTO_INCREMENT,
    team_id INT NOT NULL,
    coach_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (team_id) REFERENCES team(team_id) ON DELETE RESTRICT
);

-- Table: player
-- Purpose: Stores player information linked to their team
CREATE TABLE player (
    player_id INT PRIMARY KEY AUTO_INCREMENT,
    team_id INT NOT NULL,
    player_name VARCHAR(100) NOT NULL,
    jersey_num INT NOT NULL,
    primary_position ENUM('GK', 'DEF', 'MID', 'FWD'),
    FOREIGN KEY (team_id) REFERENCES team(team_id) ON DELETE RESTRICT,
    CHECK (jersey_num > 0)
);

-- Table: match_metadata
-- Purpose: Stores match information (venue, competition, teams, timing)
CREATE TABLE match_metadata (
    match_id INT PRIMARY KEY AUTO_INCREMENT,
    home_id INT NOT NULL,
    away_id INT NOT NULL,
    venue VARCHAR(100) NOT NULL,
    competition VARCHAR(100) NOT NULL,
    match_start DATETIME NULL,
    match_end DATETIME NULL,
    FOREIGN KEY (home_id) REFERENCES team(team_id) ON DELETE RESTRICT,
    FOREIGN KEY (away_id) REFERENCES team(team_id) ON DELETE RESTRICT,
    CHECK (home_id != away_id)
);

CREATE TABLE match_sides (
    match_id INT PRIMARY KEY,
    left_team_first_half INT NOT NULL,
    FOREIGN KEY (match_id) REFERENCES match_metadata(match_id),
    FOREIGN KEY (left_team_first_half) REFERENCES team(team_id)
);

-- Table: match_flow
-- Purpose: Stores match timing events (kickoff, halftime, overtime, penalties)
CREATE TABLE match_flow (
    match_id INT PRIMARY KEY,
    kickoff TIMESTAMP NOT NULL,
    halftime TIMESTAMP NOT NULL,
    overtime_1 TIMESTAMP NULL,
    overtime_2 TIMESTAMP NULL,
    pk_shootout TIMESTAMP NULL,
    FOREIGN KEY (match_id) REFERENCES match_metadata(match_id) ON DELETE CASCADE
);

-- Table: match_lineup
-- Purpose: Links players to specific matches with their positions
-- Composite Primary Key: (match_id, player_id)
CREATE TABLE match_lineup (
    match_id INT NOT NULL,
    team_id INT NOT NULL,
    coach_id INT NOT NULL,
    player_id INT NOT NULL,
    is_starter BOOL NOT NULL DEFAULT FALSE,
    match_position ENUM('GK', 'DEF', 'MID', 'FWD') NOT NULL,
    PRIMARY KEY (match_id, player_id),
    FOREIGN KEY (match_id) REFERENCES match_metadata(match_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES team(team_id) ON DELETE RESTRICT,
    FOREIGN KEY (coach_id) REFERENCES coach(coach_id) ON DELETE RESTRICT,
    FOREIGN KEY (player_id) REFERENCES player(player_id) ON DELETE RESTRICT
);

CREATE TABLE match_video (
    video_id INT PRIMARY KEY AUTO_INCREMENT,
    match_id INT NOT NULL,
    video_path VARCHAR(500) NOT NULL,
    video_offset_seconds INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (match_id) REFERENCES match_metadata(match_id) ON DELETE CASCADE
);

-- EVENT TRACKING TABLES

-- Table: event
-- Purpose: Central table storing all match events with timestamps and locations
-- Note: This is the parent table for all event types
CREATE TABLE event (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    match_id INT NOT NULL,
    team_id INT NOT NULL,
    player_id INT NOT NULL,
    time TIMESTAMP NOT NULL,
    location_x REAL,
    location_y REAL,
    rating ENUM('F', 'S'),
    FOREIGN KEY (match_id) REFERENCES match_metadata(match_id) ON DELETE RESTRICT,
    FOREIGN KEY (team_id) REFERENCES team(team_id) ON DELETE RESTRICT,
    FOREIGN KEY (player_id) REFERENCES player(player_id) ON DELETE RESTRICT,
    CHECK (location_x IS NULL OR (location_x >= 0 AND location_x <= 100)),
    CHECK (location_y IS NULL OR (location_y >= 0 AND location_y <= 100))
);

-- EVENT CATEGORY TABLES (Disjoint/Complete Classification)

-- Table: ball_played
-- Purpose: Classifies events where a player intentionally plays the ball
-- Note: This is a parent category for pass, shot, cross, set_piece
CREATE TABLE ball_played (
    event_id INT PRIMARY KEY,
    from_open_play BOOL NOT NULL DEFAULT TRUE,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE
);

-- Table: ball_recieved
-- Purpose: Classifies events where a player receives/controls the ball
-- Note: This is a parent category for ball_won, clearance, shot_block, shot_save
CREATE TABLE ball_received (
    event_id INT PRIMARY KEY,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE
);

-- Table: other_ball_action
-- Purpose: Classifies miscellaneous ball actions
CREATE TABLE other_ball_action (
    event_id INT PRIMARY KEY,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE
);

-- BALL_PLAYED SUBTYPES

-- Table: pass
-- Purpose: Stores detailed pass information (subtype of ball_played)
CREATE TABLE pass (
    event_id INT PRIMARY KEY,
    pass_length ENUM('short', 'medium', 'long') NULL,
    pass_height ENUM('high', 'low') NULL,
    assist BOOL NOT NULL DEFAULT FALSE,
    line_split BOOL NOT NULL DEFAULT FALSE,
    into_area BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (event_id) REFERENCES ball_played(event_id) ON DELETE CASCADE
);

-- Table: shot
-- Purpose: Stores detailed shot information (subtype of ball_played)
CREATE TABLE shot (
    event_id INT PRIMARY KEY,
    execution ENUM('right', 'left', 'header', 'other') NULL,
    result ENUM('over', 'over_left', 'over_right', 'wide_left', 'wide_right', 
                'post_left', 'post_right', 'crossbar', 'blocked', 'saved', 'failed', 'goal') NULL,
    FOREIGN KEY (event_id) REFERENCES ball_played(event_id) ON DELETE CASCADE
);

-- Table: cross_played
-- Purpose: Stores detailed cross information (subtype of ball_played)
CREATE TABLE cross_played(
    event_id INT PRIMARY KEY,
    intention ENUM('near_post', 'back_post', 'central', 'other') NULL,
    technique ENUM('inswing', 'outswing', 'other') NULL,
    FOREIGN KEY (event_id) REFERENCES ball_played(event_id) ON DELETE CASCADE
);

-- Table: set_piece
-- Purpose: Stores set piece information (direct event type)
CREATE TABLE set_piece (
    event_id INT PRIMARY KEY,
    type ENUM('throw_in_front', 'throw_in_rear', 'direct', 'indirect', 
              'corner_left', 'corner_right', 'penalty', 'goal_kick') NOT NULL,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE
);

-- BALL_RECEIVED SUBTYPES

-- Table: ball_won
-- Purpose: Stores ball winning events (subtype of ball_recieved)
CREATE TABLE ball_won (
    event_id INT PRIMARY KEY,
    FOREIGN KEY (event_id) REFERENCES ball_received(event_id) ON DELETE CASCADE
);

-- Table: clearance
-- Purpose: Stores defensive clearance events (subtype of ball_recieved)
CREATE TABLE clearance (
    event_id INT PRIMARY KEY,
    FOREIGN KEY (event_id) REFERENCES ball_received(event_id) ON DELETE CASCADE
);

-- Table: shot_block
-- Purpose: Stores shot blocking events (subtype of ball_recieved)
CREATE TABLE shot_block (
    event_id INT PRIMARY KEY,
    shot_event_id INT NULL,
    FOREIGN KEY (event_id) REFERENCES ball_received(event_id) ON DELETE CASCADE,
    FOREIGN KEY (shot_event_id) REFERENCES shot(event_id) ON DELETE RESTRICT
);

-- Table: shot_save
-- Purpose: Stores goalkeeper save events (subtype of ball_recieved)
CREATE TABLE shot_save (
    event_id INT PRIMARY KEY,
    shot_event_id INT NULL,
    FOREIGN KEY (event_id) REFERENCES ball_received(event_id) ON DELETE CASCADE,
    FOREIGN KEY (shot_event_id) REFERENCES shot(event_id) ON DELETE RESTRICT
);

-- SPECIAL EVENT TYPES

-- Table: goal
-- Purpose: Stores goal information linked to the shot that scored
CREATE TABLE goal (
    event_id INT PRIMARY KEY,
    shot_event_id INT NOT NULL,
    goal_zone ENUM('low_right_90', 'upper_right_90', 'lower_left_90', 
                   'upper_left_90', 'central', 'left', 'right') NULL,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE,
    FOREIGN KEY (shot_event_id) REFERENCES shot(event_id) ON DELETE RESTRICT
);

CREATE TABLE own_goal (
    event_id INT PRIMARY KEY,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE
);

-- Table: foul
-- Purpose: Stores foul information
CREATE TABLE foul (
    event_id INT PRIMARY KEY,
    guilty_id INT NULL,
    innocent_id INT NULL,
    reason ENUM('foul', 'unfairness', 'other') NULL,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE,
    FOREIGN KEY (guilty_id) REFERENCES player(player_id) ON DELETE RESTRICT,
    FOREIGN KEY (innocent_id) REFERENCES player(player_id) ON DELETE RESTRICT
);

-- Table: card
-- Purpose: Stores disciplinary card information
CREATE TABLE card (
    event_id INT PRIMARY KEY,
    foul_event_id INT,
    reason ENUM('foul', 'unfairness', 'other') NULL,
    color ENUM('yellow', 'second_yellow', 'red') NOT NULL,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE,
    FOREIGN KEY (foul_event_id) REFERENCES foul(event_id) ON DELETE RESTRICT
);

-- Table: duel
-- Purpose: Stores one-on-one duel information
CREATE TABLE duel (
    event_id INT PRIMARY KEY,
    winner_id INT NULL,
    loser_id INT NULL,
    context ENUM('ground', 'aerial') NULL,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE,
    FOREIGN KEY (winner_id) REFERENCES player(player_id) ON DELETE RESTRICT,
    FOREIGN KEY (loser_id) REFERENCES player(player_id) ON DELETE RESTRICT
);

-- Table: substitution
-- Purpose: Stores player substitution information
CREATE TABLE substitution (
    event_id INT PRIMARY KEY,
    in_player_id INT NULL,
    out_player_id INT NULL,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE,
    FOREIGN KEY (in_player_id) REFERENCES player(player_id) ON DELETE RESTRICT,
    FOREIGN KEY (out_player_id) REFERENCES player(player_id) ON DELETE RESTRICT
);


-- Table: handball
-- Purpose: Stores handball infractions
-- Note: Direct subclass of event (like foul, card, duel)substitution
CREATE TABLE handball (
    event_id INT PRIMARY KEY,
    guilty_id INT NOT NULL,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE,
    FOREIGN KEY (guilty_id) REFERENCES player(player_id) ON DELETE RESTRICT
);

-- Table: offside
-- Purpose: Stores offside infractions
-- Note: Direct subclass of event (like foul, card, duel)
CREATE TABLE offside (
    event_id INT PRIMARY KEY,
    offside_player_id INT NOT NULL,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE,
    FOREIGN KEY (offside_player_id) REFERENCES player(player_id) ON DELETE RESTRICT
);