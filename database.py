# database.py
# Database handler for match data

import mysql.connector
from datetime import datetime
from config import DB_CONFIG
from datetime import datetime, timedelta


class MatchDatabase:
    """Handles all database operations for match data"""
    
    def __init__(self):
        """Initialize database connection configuration"""
        self.config = DB_CONFIG
    
    def get_connection(self):
        """Create and return a database connection"""
        return mysql.connector.connect(**self.config)
    
    def get_or_create_team(self, conn, team_name):
        """
        Get team_id for a team, or create it if it doesn't exist
        
        Args:
            conn: Database connection
            team_name: Name of the team
            
        Returns:
            team_id: The ID of the team
        """
        cursor = conn.cursor()
        
        # Check if team exists
        cursor.execute("SELECT team_id FROM team WHERE team_name = %s", (team_name,))
        result = cursor.fetchone()
        
        if result:
            team_id = result[0]
        else:
            # Create new team
            cursor.execute("INSERT INTO team (team_name) VALUES (%s)", (team_name,))
            team_id = cursor.lastrowid
        
        cursor.close()
        return team_id
    
    def get_team_on_left(self, conn, match_id, event_time_seconds):
        """
        Determine which team is on the left side at a given time.
        
        Args:
            conn: Database connection
            match_id: The match ID
            event_time_seconds: Event time in seconds
        
        Returns:
            team_id of team currently on left side
        """
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT ms.left_team_first_half, m.home_id, m.away_id
            FROM match_sides ms
            JOIN match_metadata m ON ms.match_id = m.match_id
            WHERE ms.match_id = %s
        """, (match_id,))
        result = cursor.fetchone()
        cursor.close()
        
        if not result:
            return None
        
        left_first = result['left_team_first_half']
        home_team = result['home_id']
        away_team = result['away_id']
        
        # Determine right team
        right_first = away_team if left_first == home_team else home_team
        
        # Determine period and return appropriate team
        if event_time_seconds < 2700:  # 0-45 min (first half)
            return left_first
        elif event_time_seconds < 5400:  # 45-90 min (second half)
            return right_first
        else:  # 90+ min (overtime - switches back)
            return left_first
    
    def get_or_create_coach(self, conn, team_id, coach_name):
        """
        Get coach_id for a coach, or create if doesn't exist
        
        Args:
            conn: Database connection
            team_id: ID of the team
            coach_name: Name of the coach
            
        Returns:
            coach_id: The ID of the coach
        """
        cursor = conn.cursor()
        
        # Check if coach exists for this team
        cursor.execute(
            "SELECT coach_id FROM coach WHERE team_id = %s AND coach_name = %s",
            (team_id, coach_name)
        )
        result = cursor.fetchone()
        
        if result:
            coach_id = result[0]
        else:
            # Create new coach
            cursor.execute(
                "INSERT INTO coach (team_id, coach_name) VALUES (%s, %s)",
                (team_id, coach_name)
            )
            coach_id = cursor.lastrowid
        
        cursor.close()
        return coach_id
    
    def get_or_create_player(self, conn, team_id, player_name, jersey_num, position):
        """
        Get player_id for a player, or create if doesn't exist
        
        Args:
            conn: Database connection
            team_id: ID of the team
            player_name: Name of the player
            jersey_num: Jersey number (as string from form)
            position: Position ('GK', 'DEF', 'MID', 'FWD') or None
            
        Returns:
            player_id: The ID of the player
        """
        cursor = conn.cursor()
        
        # Convert jersey_num to int, handle empty strings
        try:
            jersey_number = int(jersey_num) if jersey_num else 0
        except ValueError:
            jersey_number = 0
        
        # Check if player exists with same name and jersey number for this team
        cursor.execute(
            "SELECT player_id FROM player WHERE team_id = %s AND player_name = %s AND jersey_num = %s",
            (team_id, player_name, jersey_number)
        )
        result = cursor.fetchone()
        
        if result:
            player_id = result[0]
        else:
            # Create new player
            cursor.execute(
                "INSERT INTO player (team_id, player_name, jersey_num, primary_position) VALUES (%s, %s, %s, %s)",
                (team_id, player_name, jersey_number, position)
            )
            player_id = cursor.lastrowid
        
        cursor.close()
        return player_id
    
    def create_match_metadata(self, conn, home_id, away_id, venue, competition, date_str):
        """
        Create match metadata record
        
        Args:
            conn: Database connection
            home_id: Home team ID
            away_id: Away team ID
            venue: Venue name
            competition: Competition name
            date_str: Date string in format dd/mm/yy
            
        Returns:
            match_id: The ID of the created match
        """
        cursor = conn.cursor()
        
        # Parse date from dd/mm/yy format
        # %y automatically interprets 2-digit year as 20XX
        try:
            match_date = datetime.strptime(date_str, '%d/%m/%y')
        except ValueError:
            # If parsing fails, try with 4-digit year
            try:
                match_date = datetime.strptime(date_str, '%d/%m/%Y')
            except ValueError:
                raise ValueError(f"Invalid date format: {date_str}. Expected dd/mm/yy or dd/mm/yyyy")
        
        # Insert match metadata (with NULL for match_start and match_end for now)
        cursor.execute(
            """INSERT INTO match_metadata 
               (home_id, away_id, venue, competition, match_start, match_end) 
               VALUES (%s, %s, %s, %s, NULL, NULL)""",
            (home_id, away_id, venue, competition)
        )
        match_id = cursor.lastrowid
        
        cursor.close()
        return match_id
    
    def insert_lineup_entry(self, conn, match_id, team_id, coach_id, player_id, is_starter, position):
        """
        Insert a lineup entry for a player in a match
        
        Args:
            conn: Database connection
            match_id: Match ID
            team_id: Team ID
            coach_id: Coach ID
            player_id: Player ID
            is_starter: Boolean - True if starter, False if substitute
            position: Match position ('GK', 'DEF', 'MID', 'FWD')
        """
        cursor = conn.cursor()
        
        cursor.execute(
            """INSERT INTO match_lineup 
               (match_id, team_id, coach_id, player_id, is_starter, match_position) 
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (match_id, team_id, coach_id, player_id, is_starter, position)
        )
        
        cursor.close()
    
    def save_match_data(self, form_data):
        """
        Main function to save all match data from the form
        
        Args:
            form_data: Dictionary containing all form data
            
        Returns:
            Tuple: (success: bool, result: match_id or error_message)
        """
        conn = None
        try:
            # Get connection
            conn = self.get_connection()
            conn.start_transaction()
            
            # Extract match details
            match_details = form_data['match_details']
            home_team_data = form_data['home_team']
            away_team_data = form_data['away_team']
            
            # 1. Get or create teams
            home_team_id = self.get_or_create_team(conn, home_team_data['name'])
            away_team_id = self.get_or_create_team(conn, away_team_data['name'])
            
            # 2. Get or create coaches
            home_coach_id = self.get_or_create_coach(conn, home_team_id, home_team_data['coach'])
            away_coach_id = self.get_or_create_coach(conn, away_team_id, away_team_data['coach'])
            
            # 3. Create match metadata
            match_id = self.create_match_metadata(
                conn,
                home_team_id,
                away_team_id,
                match_details['venue'],
                match_details['competition'],
                match_details['date']
            )
            
            # 4. Process home team starters
            starters = home_team_data['starters']
            
            # Goalkeeper
            if starters['gk']['name']:
                player_id = self.get_or_create_player(
                    conn, home_team_id, 
                    starters['gk']['name'], 
                    starters['gk']['jersey'], 
                    'GK'
                )
                self.insert_lineup_entry(conn, match_id, home_team_id, home_coach_id, player_id, True, 'GK')
            
            # Defenders
            for defender in starters['def']:
                if defender['name']:
                    player_id = self.get_or_create_player(
                        conn, home_team_id, 
                        defender['name'], 
                        defender['jersey'], 
                        'DEF'
                    )
                    self.insert_lineup_entry(conn, match_id, home_team_id, home_coach_id, player_id, True, 'DEF')
            
            # Midfielders
            for midfielder in starters['mid']:
                if midfielder['name']:
                    player_id = self.get_or_create_player(
                        conn, home_team_id, 
                        midfielder['name'], 
                        midfielder['jersey'], 
                        'MID'
                    )
                    self.insert_lineup_entry(conn, match_id, home_team_id, home_coach_id, player_id, True, 'MID')
            
            # Forwards
            for forward in starters['fwd']:
                if forward['name']:
                    player_id = self.get_or_create_player(
                        conn, home_team_id, 
                        forward['name'], 
                        forward['jersey'], 
                        'FWD'
                    )
                    self.insert_lineup_entry(conn, match_id, home_team_id, home_coach_id, player_id, True, 'FWD')
            
            # 5. Process home team substitutes
            for sub in home_team_data['subs']:
                if sub['name']:
                    player_id = self.get_or_create_player(
                        conn, home_team_id, 
                        sub['name'], 
                        sub['jersey'], 
                        'MID'  # Default position for subs
                    )
                    self.insert_lineup_entry(conn, match_id, home_team_id, home_coach_id, player_id, False, 'MID')
            
            # 6. Process away team starters
            starters = away_team_data['starters']
            
            # Goalkeeper
            if starters['gk']['name']:
                player_id = self.get_or_create_player(
                    conn, away_team_id, 
                    starters['gk']['name'], 
                    starters['gk']['jersey'], 
                    'GK'
                )
                self.insert_lineup_entry(conn, match_id, away_team_id, away_coach_id, player_id, True, 'GK')
            
            # Defenders
            for defender in starters['def']:
                if defender['name']:
                    player_id = self.get_or_create_player(
                        conn, away_team_id, 
                        defender['name'], 
                        defender['jersey'], 
                        'DEF'
                    )
                    self.insert_lineup_entry(conn, match_id, away_team_id, away_coach_id, player_id, True, 'DEF')
            
            # Midfielders
            for midfielder in starters['mid']:
                if midfielder['name']:
                    player_id = self.get_or_create_player(
                        conn, away_team_id, 
                        midfielder['name'], 
                        midfielder['jersey'], 
                        'MID'
                    )
                    self.insert_lineup_entry(conn, match_id, away_team_id, away_coach_id, player_id, True, 'MID')
            
            # Forwards
            for forward in starters['fwd']:
                if forward['name']:
                    player_id = self.get_or_create_player(
                        conn, away_team_id, 
                        forward['name'], 
                        forward['jersey'], 
                        'FWD'
                    )
                    self.insert_lineup_entry(conn, match_id, away_team_id, away_coach_id, player_id, True, 'FWD')
            
            # 7. Process away team substitutes
            for sub in away_team_data['subs']:
                if sub['name']:
                    player_id = self.get_or_create_player(
                        conn, away_team_id, 
                        sub['name'], 
                        sub['jersey'], 
                        'MID'  # Default position for subs
                    )
                    self.insert_lineup_entry(conn, match_id, away_team_id, away_coach_id, player_id, False, 'MID')
            
            # Commit transaction
            conn.commit()
            
            return True, match_id
            
        except Exception as e:
            # Rollback on error
            if conn:
                conn.rollback()
            return False, str(e)
            
        finally:
            # Close connection
            if conn:
                conn.close()

    def load_lineup_data(self, match_id):
        """
        Load all lineup data for a match from the database
        
        Args:
            match_id: The match ID
            
        Returns:
            Dictionary with structured lineup data
        """
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        
        try:
            # Get match metadata (teams)
            cursor.execute("""
                SELECT 
                    mm.home_id,
                    mm.away_id,
                    ht.team_name as home_team_name,
                    at.team_name as away_team_name
                FROM match_metadata mm
                JOIN team ht ON mm.home_id = ht.team_id
                JOIN team at ON mm.away_id = at.team_id
                WHERE mm.match_id = %s
            """, (match_id,))
            
            match_info = cursor.fetchone()
            if not match_info:
                return None
            
            # Get all players in the lineup
            cursor.execute("""
                SELECT 
                    ml.team_id,
                    ml.player_id,
                    p.player_name,
                    p.jersey_num,
                    ml.match_position,
                    ml.is_starter
                FROM match_lineup ml
                JOIN player p ON ml.player_id = p.player_id
                WHERE ml.match_id = %s
                ORDER BY ml.team_id, ml.is_starter DESC, ml.match_position, p.jersey_num
            """, (match_id,))
            
            players = cursor.fetchall()
            
            # Organize data by team
            lineup_data = {
                'match_id': match_id,
                'home_team': {
                    'team_id': match_info['home_id'],
                    'team_name': match_info['home_team_name'],
                    'players': {
                        'gk': None,
                        'def': [],
                        'mid': [],
                        'fwd': [],
                        'sub': []
                    }
                },
                'away_team': {
                    'team_id': match_info['away_id'],
                    'team_name': match_info['away_team_name'],
                    'players': {
                        'gk': None,
                        'def': [],
                        'mid': [],
                        'fwd': [],
                        'sub': []
                    }
                }
            }
            
            # Organize players by position
            for player in players:
                player_data = {
                    'player_id': player['player_id'],
                    'name': player['player_name'],
                    'jersey': player['jersey_num']
                }
                
                # Determine which team
                if player['team_id'] == match_info['home_id']:
                    team_key = 'home_team'
                else:
                    team_key = 'away_team'
                
                # Organize by position
                if player['is_starter']:
                    position = player['match_position']
                    if position == 'GK':
                        lineup_data[team_key]['players']['gk'] = player_data
                    elif position == 'DEF':
                        lineup_data[team_key]['players']['def'].append(player_data)
                    elif position == 'MID':
                        lineup_data[team_key]['players']['mid'].append(player_data)
                    elif position == 'FWD':
                        lineup_data[team_key]['players']['fwd'].append(player_data)
                else:
                    # Substitute
                    lineup_data[team_key]['players']['sub'].append(player_data)
            
            return lineup_data
            
        finally:
            cursor.close()
            conn.close()


    def insert_event(self, conn, match_id, team_id, player_id, timestamp):
        """
        Insert a base event and return the event_id
        
        Args:
            conn: Database connection
            match_id: Match ID
            team_id: Team ID
            player_id: Player ID
            timestamp: Event timestamp (datetime)
            
        Returns:
            event_id: The ID of the created event
        """
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO event 
            (match_id, team_id, player_id, time, location_x, location_y, rating)
            VALUES (%s, %s, %s, %s, NULL, NULL, NULL)
        """, (match_id, team_id, player_id, timestamp))
        
        event_id = cursor.lastrowid
        cursor.close()
        return event_id


    def insert_ball_received(self, conn, event_id, success=True):
        """Insert ball_received event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ball_received (event_id)
            VALUES (%s)
        """, (event_id,))
        cursor.close()


    def insert_ball_played(self, conn, event_id, from_open_play=True):
        """Insert ball_played event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ball_played (event_id, from_open_play)
            VALUES (%s, %s)
        """, (event_id, from_open_play))
        cursor.close()


    def insert_pass(self, conn, event_id, pass_length, pass_height):
        """Insert pass event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO pass (event_id, pass_length, pass_height, assist, line_split)
            VALUES (%s, %s, %s, FALSE, FALSE)
        """, (event_id, pass_length, pass_height))
        cursor.close()


    def insert_shot(self, conn, event_id):
        """Insert shot event with NULL details"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO shot (event_id, execution, result)
            VALUES (%s, NULL, NULL)
        """, (event_id,))
        cursor.close()


    def insert_cross(self, conn, event_id, intention=None, technique=None):
        """Insert cross event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cross_played (event_id, intention, technique)
            VALUES (%s, %s, %s)
        """, (event_id, intention, technique))
        cursor.close()


    def insert_set_piece(self, conn, event_id, set_piece_type):
        """Insert set piece event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO set_piece (event_id, type)
            VALUES (%s, %s)
        """, (event_id, set_piece_type))
        cursor.close()


    def insert_ball_won(self, conn, event_id):
        """Insert ball_won event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ball_won (event_id)
            VALUES (%s)
        """, (event_id,))
        cursor.close()


    def insert_clearance(self, conn, event_id):
        """Insert clearance event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clearance (event_id)
            VALUES (%s)
        """, (event_id,))
        cursor.close()


    def insert_shot_block(self, conn, event_id):
        """Insert shot_block event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO shot_block (event_id, shot_event_id)
            VALUES (%s, NULL)
        """, (event_id,))
        cursor.close()


    def insert_shot_save(self, conn, event_id):
        """Insert shot_save event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO shot_save (event_id, shot_event_id)
            VALUES (%s, NULL)
        """, (event_id,))
        cursor.close()


    def insert_card(self, conn, event_id, card_color):
        """Insert card event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO card (event_id, foul_event_id, reason, color)
            VALUES (%s, NULL, NULL, %s)
        """, (event_id, card_color))
        cursor.close()

    def insert_own_goal(self, conn, event_id):
        """Insert own goal event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO own_goal (event_id)
            VALUES (%s)
        """, (event_id,))
        cursor.close()

    def insert_foul(self, conn, event_id):
        """Insert foul event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO foul (event_id, guilty_id, innocent_id, reason)
            VALUES (%s, NULL, NULL, NULL)
        """, (event_id,))
        cursor.close()
        
    def insert_offside(self, conn, event_id, offside_player_id):
        """Insert offside event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO offside (event_id, offside_player_id)
            VALUES (%s, %s)
        """, (event_id, offside_player_id))
        cursor.close()

    def insert_handball(self, conn, event_id, guilty_player_id):
        """Insert handball event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO handball (event_id, guilty_id)
            VALUES (%s, %s)
        """, (event_id, guilty_player_id))
        cursor.close()


    def insert_duel(self, conn, event_id, context):
        """Insert duel event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO duel (event_id, winner_id, loser_id, context)
            VALUES (%s, NULL, NULL, %s)
        """, (event_id, context))
        cursor.close()


    def insert_substitution(self, conn, event_id):
        """Insert substitution event"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO substitution (event_id, in_player_id, out_player_id)
            VALUES (%s, NULL, NULL)
        """, (event_id,))
        cursor.close()


    def delete_last_event(self, event_id):
        """
        Delete an event and all its related records
        
        Args:
            event_id: The event ID to delete
            
        Returns:
            bool: Success status
        """
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # Delete from event table (CASCADE will handle related tables)
            cursor.execute("DELETE FROM event WHERE event_id = %s", (event_id,))
            
            conn.commit()
            cursor.close()
            return True
            
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error deleting event: {e}")
            return False
            
        finally:
            if conn:
                conn.close()

    def get_all_events(self, conn, match_id):
        """Get all events for a match with basic info - showing full hierarchy"""
        cursor = conn.cursor(dictionary=True)
        
        # This query returns Ball Received, Ball Played, and specific subtypes as separate rows
        cursor.execute("""
            SELECT 
                all_events.event_id,
                all_events.time,
                all_events.location_x,
                all_events.location_y,
                all_events.rating,
                all_events.team_name,
                all_events.player_name,
                all_events.jersey_num,
                all_events.event_type,
                all_events.incomplete
            FROM (
                -- Ball Received entries
                SELECT 
                    e.event_id,
                    e.time,
                    e.location_x,
                    e.location_y,
                    e.rating,
                    t.team_name,
                    p.player_name,
                    p.jersey_num,
                    'Ball Received' as event_type,
                    0 as incomplete,
                    1 as display_order
                FROM event e
                JOIN team t ON e.team_id = t.team_id
                JOIN player p ON e.player_id = p.player_id
                JOIN ball_received br ON e.event_id = br.event_id
                WHERE e.match_id = %s
                
                UNION ALL
                
                -- Pass entries
                SELECT 
                    e.event_id,
                    e.time,
                    e.location_x,
                    e.location_y,
                    e.rating,
                    t.team_name,
                    p.player_name,
                    p.jersey_num,
                    CONCAT('Pass (', pa.pass_length, '/', pa.pass_height, ')') as event_type,
                    0 as incomplete,
                    2 as display_order
                FROM event e
                JOIN team t ON e.team_id = t.team_id
                JOIN player p ON e.player_id = p.player_id
                JOIN ball_played bp ON e.event_id = bp.event_id
                JOIN pass pa ON bp.event_id = pa.event_id
                WHERE e.match_id = %s
                
                UNION ALL
                
                -- Shot entries
                SELECT 
                    e.event_id,
                    e.time,
                    e.location_x,
                    e.location_y,
                    e.rating,
                    t.team_name,
                    p.player_name,
                    p.jersey_num,
                    CONCAT('Shot (', COALESCE(sh.result, 'pending'), ')') as event_type,
                    CASE WHEN e.location_x IS NULL OR sh.result IS NULL THEN 1 ELSE 0 END as incomplete,
                    2 as display_order
                FROM event e
                JOIN team t ON e.team_id = t.team_id
                JOIN player p ON e.player_id = p.player_id
                JOIN ball_played bp ON e.event_id = bp.event_id
                JOIN shot sh ON bp.event_id = sh.event_id
                WHERE e.match_id = %s
                
                UNION ALL
                
                -- Cross entries
                SELECT 
                    e.event_id,
                    e.time,
                    e.location_x,
                    e.location_y,
                    e.rating,
                    t.team_name,
                    p.player_name,
                    p.jersey_num,
                    CONCAT('Cross (', COALESCE(cr.intention, 'unknown'), ')') as event_type,
                    CASE WHEN e.location_x IS NULL OR cr.intention IS NULL OR cr.technique IS NULL THEN 1 ELSE 0 END as incomplete,
                    2 as display_order
                FROM event e
                JOIN team t ON e.team_id = t.team_id
                JOIN player p ON e.player_id = p.player_id
                JOIN ball_played bp ON e.event_id = bp.event_id
                JOIN cross_played cr ON bp.event_id = cr.event_id
                WHERE e.match_id = %s
                
                UNION ALL

                -- Duel entries
                SELECT 
                    e.event_id,
                    e.time,
                    e.location_x,
                    e.location_y,
                    e.rating,
                    t.team_name,
                    p.player_name,
                    p.jersey_num,
                    CONCAT('Duel (', du.context, ')') as event_type,
                    CASE WHEN e.location_x IS NULL OR du.context IS NULL OR du.winner_id IS NULL THEN 1 ELSE 0 END as incomplete,
                    1 as display_order
                FROM event e
                JOIN team t ON e.team_id = t.team_id
                JOIN player p ON e.player_id = p.player_id
                JOIN duel du ON e.event_id = du.event_id
                WHERE e.match_id = %s 
                       
                UNION ALL
                
                -- Other Ball Action entries
                SELECT 
                    e.event_id,
                    e.time,
                    e.location_x,
                    e.location_y,
                    e.rating,
                    t.team_name,
                    p.player_name,
                    p.jersey_num,
                    'Other Ball Action' as event_type,
                    0 as incomplete,
                    2 as display_order
                FROM event e
                JOIN team t ON e.team_id = t.team_id
                JOIN player p ON e.player_id = p.player_id
                JOIN other_ball_action oba ON e.event_id = oba.event_id
                WHERE e.match_id = %s
                
                UNION ALL
                
                -- All other event types (Goal, Foul, Card, etc.)
                SELECT 
                    e.event_id,
                    e.time,
                    e.location_x,
                    e.location_y,
                    e.rating,
                    t.team_name,
                    p.player_name,
                    p.jersey_num,
                    CASE 
                        WHEN g.event_id IS NOT NULL THEN 'Goal'
                        WHEN og.event_id IS NOT NULL THEN 'Own Goal'
                        WHEN sp.event_id IS NOT NULL THEN CONCAT('Set Piece (', sp.type, ')')
                        WHEN fo.event_id IS NOT NULL THEN 'Foul'
                        WHEN ca.event_id IS NOT NULL THEN CONCAT('Card (', ca.color, ')')
                        WHEN du.event_id IS NOT NULL THEN CONCAT('Duel (', du.context, ')')
                        WHEN os.event_id IS NOT NULL THEN 'Offside'
                        WHEN hb.event_id IS NOT NULL THEN 'Handball'
                        WHEN su.event_id IS NOT NULL THEN 'Substitution'
                        WHEN bw.event_id IS NOT NULL THEN 'Ball Won'
                        WHEN cl.event_id IS NOT NULL THEN 'Clearance'
                        WHEN sb.event_id IS NOT NULL THEN 'Shot Block'
                        WHEN ss.event_id IS NOT NULL THEN 'Shot Save'
                        ELSE 'Unknown'
                    END as event_type,
                    CASE 
                        WHEN g.event_id IS NOT NULL AND g.goal_zone IS NULL THEN 1
                        ELSE 0
                    END as incomplete,
                    2 as display_order
                FROM event e
                JOIN team t ON e.team_id = t.team_id
                JOIN player p ON e.player_id = p.player_id
                LEFT JOIN goal g ON e.event_id = g.event_id
                LEFT JOIN own_goal og ON e.event_id = og.event_id
                LEFT JOIN set_piece sp ON e.event_id = sp.event_id
                LEFT JOIN foul fo ON e.event_id = fo.event_id
                LEFT JOIN card ca ON e.event_id = ca.event_id
                LEFT JOIN duel du ON e.event_id = du.event_id
                LEFT JOIN offside os ON e.event_id = os.event_id
                LEFT JOIN handball hb ON e.event_id = hb.event_id
                LEFT JOIN substitution su ON e.event_id = su.event_id
                LEFT JOIN ball_received br ON e.event_id = br.event_id
                LEFT JOIN ball_won bw ON br.event_id = bw.event_id
                LEFT JOIN clearance cl ON br.event_id = cl.event_id
                LEFT JOIN shot_block sb ON br.event_id = sb.event_id
                LEFT JOIN shot_save ss ON br.event_id = ss.event_id
                WHERE e.match_id = %s
                AND (g.event_id IS NOT NULL 
                OR og.event_id IS NOT NULL 
                OR sp.event_id IS NOT NULL
                OR fo.event_id IS NOT NULL
                OR ca.event_id IS NOT NULL
                OR du.event_id IS NOT NULL
                OR os.event_id IS NOT NULL
                OR hb.event_id IS NOT NULL
                OR su.event_id IS NOT NULL
                OR bw.event_id IS NOT NULL
                OR cl.event_id IS NOT NULL
                OR sb.event_id IS NOT NULL
                OR ss.event_id IS NOT NULL)
            ) AS all_events
            ORDER BY all_events.event_id, all_events.display_order
        """, (match_id, match_id, match_id, match_id, match_id, match_id, match_id))
        
        result = cursor.fetchall()
        cursor.close()
        return result


    def get_event_details(self, conn, event_id):
        """Get complete details for a specific event"""
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("""
            SELECT 
                e.event_id,
                e.player_id,
                e.time,
                e.location_x,
                e.location_y,
                e.rating,
                t.team_name,
                p.player_name,
                p.jersey_num,
                sh.execution,
                sh.result,
                pa.pass_length,
                pa.pass_height,
                pa.assist,
                pa.line_split,
                cr.intention,
                cr.technique,
                g.goal_zone,
                fo.reason as foul_reason,
                ca.reason as card_reason,
                ca.color as card_color,
                fo.guilty_id as foul_guilty_id, 
                fo.innocent_id as foul_innocent_id,
                du.context as duel_context,
                du.winner_id as duel_winner_id,
                du.loser_id as duel_loser_id, 
                sp.type as set_piece_type, 
                hb.guilty_id as handball_guilty_id,  
                su.in_player_id as sub_in_player_id,  
                su.out_player_id as sub_out_player_id,      
                CASE 
                    WHEN pa.event_id IS NOT NULL THEN 'Pass'
                    WHEN sh.event_id IS NOT NULL THEN 'Shot'
                    WHEN cr.event_id IS NOT NULL THEN 'Cross'
                    WHEN bw.event_id IS NOT NULL THEN 'Ball Won'
                    WHEN cl.event_id IS NOT NULL THEN 'Clearance'
                    WHEN sb.event_id IS NOT NULL THEN 'Shot Block'
                    WHEN ss.event_id IS NOT NULL THEN 'Shot Save'
                    WHEN oba.event_id IS NOT NULL THEN 'Other Ball Action'
                    WHEN bp.event_id IS NOT NULL AND pa.event_id IS NULL AND sh.event_id IS NULL AND cr.event_id IS NULL THEN 'Ball Played'
                    WHEN br.event_id IS NOT NULL AND bw.event_id IS NULL AND cl.event_id IS NULL AND sb.event_id IS NULL AND ss.event_id IS NULL THEN 'Ball Received'
                    WHEN g.event_id IS NOT NULL THEN 'Goal'
                    WHEN og.event_id IS NOT NULL THEN 'Own Goal'
                    WHEN sp.event_id IS NOT NULL THEN 'Set Piece'
                    WHEN fo.event_id IS NOT NULL THEN 'Foul'
                    WHEN ca.event_id IS NOT NULL THEN 'Card'
                    WHEN du.event_id IS NOT NULL THEN 'Duel'
                    WHEN os.event_id IS NOT NULL THEN 'Offside'
                    WHEN hb.event_id IS NOT NULL THEN 'Handball'
                    WHEN su.event_id IS NOT NULL THEN 'Substitution'
                    ELSE 'Other'
                END as event_type
            FROM event e
            JOIN team t ON e.team_id = t.team_id
            JOIN player p ON e.player_id = p.player_id
            LEFT JOIN ball_played bp ON e.event_id = bp.event_id
            LEFT JOIN ball_received br ON e.event_id = br.event_id
            LEFT JOIN pass pa ON bp.event_id = pa.event_id
            LEFT JOIN shot sh ON bp.event_id = sh.event_id
            LEFT JOIN cross_played cr ON bp.event_id = cr.event_id
            LEFT JOIN goal g ON e.event_id = g.event_id
            LEFT JOIN own_goal og ON e.event_id = og.event_id
            LEFT JOIN set_piece sp ON e.event_id = sp.event_id
            LEFT JOIN foul fo ON e.event_id = fo.event_id
            LEFT JOIN card ca ON e.event_id = ca.event_id
            LEFT JOIN duel du ON e.event_id = du.event_id
            LEFT JOIN offside os ON e.event_id = os.event_id
            LEFT JOIN handball hb ON e.event_id = hb.event_id
            LEFT JOIN substitution su ON e.event_id = su.event_id
            LEFT JOIN other_ball_action oba ON e.event_id = oba.event_id
            LEFT JOIN ball_won bw ON br.event_id = bw.event_id
            LEFT JOIN clearance cl ON br.event_id = cl.event_id
            LEFT JOIN shot_block sb ON br.event_id = sb.event_id
            LEFT JOIN shot_save ss ON br.event_id = ss.event_id
            WHERE e.event_id = %s
        """, (event_id,))
        
        result = cursor.fetchone()
        cursor.close()
        return result


    def update_event_location(self, conn, event_id, location_x, location_y):
        """Update event location"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE event 
            SET location_x = %s, location_y = %s
            WHERE event_id = %s
        """, (location_x, location_y, event_id))
        conn.commit()


    def update_event_rating(self, conn, event_id, rating):
        """Update event rating"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE event 
            SET rating = %s
            WHERE event_id = %s
        """, (rating, event_id))
        conn.commit()


    def update_shot_execution(self, conn, event_id, execution):
        """Update shot execution"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE shot 
            SET execution = %s
            WHERE event_id = %s
        """, (execution, event_id))
        conn.commit()


    def update_pass_details(self, conn, event_id, assist, line_split):
        """Update pass assist and line_split"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE pass 
            SET assist = %s, line_split = %s
            WHERE event_id = %s
        """, (assist, line_split, event_id))
        conn.commit()


    def update_cross_details(self, conn, event_id, intention, technique):
        """Update cross intention and technique"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE cross_played 
            SET intention = %s, technique = %s
            WHERE event_id = %s
        """, (intention, technique, event_id))
        conn.commit()


    def update_goal_zone(self, conn, event_id, goal_zone):
        """Update goal zone"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE goal 
            SET goal_zone = %s
            WHERE event_id = %s
        """, (goal_zone, event_id))
        conn.commit()

    def update_pass_type(self, conn, event_id, pass_length, pass_height):
        """Update pass length and height"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE pass 
            SET pass_length = %s, pass_height = %s
            WHERE event_id = %s
        """, (pass_length, pass_height, event_id))
        conn.commit()
        cursor.close()

    def update_shot_result(self, conn, event_id, result):
        """Update shot result"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE shot 
            SET result = %s
            WHERE event_id = %s
        """, (result, event_id))
        conn.commit()
        cursor.close()

    def update_card_color(self, conn, event_id, color):
        """Update card color"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE card 
            SET color = %s
            WHERE event_id = %s
        """, (color, event_id))
        conn.commit()
        cursor.close()

    def update_card_reason(self, conn, event_id, reason):
        """Update card reason"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE card 
            SET reason = %s
            WHERE event_id = %s
        """, (reason, event_id))
        conn.commit()
        cursor.close()

    def update_duel_context(self, conn, event_id, context):
        """Update duel context"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE duel 
            SET context = %s
            WHERE event_id = %s
        """, (context, event_id))
        conn.commit()
        cursor.close()

    def update_duel_players(self, conn, event_id, winner_id, loser_id):
        """Update duel winner and loser"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE duel 
            SET winner_id = %s, loser_id = %s
            WHERE event_id = %s
        """, (winner_id, loser_id, event_id))
        conn.commit()
        cursor.close()

    def update_set_piece_type(self, conn, event_id, sp_type):
        """Update set piece type"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE set_piece 
            SET type = %s
            WHERE event_id = %s
        """, (sp_type, event_id))
        conn.commit()
        cursor.close()

    def update_foul_players(self, conn, event_id, guilty_id, innocent_id):
        """Update foul guilty and innocent players"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE foul 
            SET guilty_id = %s, innocent_id = %s
            WHERE event_id = %s
        """, (guilty_id, innocent_id, event_id))
        conn.commit()
        cursor.close()

    def update_foul_reason(self, conn, event_id, reason):
        """Update foul reason"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE foul 
            SET reason = %s
            WHERE event_id = %s
        """, (reason, event_id))
        conn.commit()
        cursor.close()

    def update_offside_player(self, conn, event_id, offside_player_id):
        """Update offside player"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE offside 
            SET offside_player_id = %s
            WHERE event_id = %s
        """, (offside_player_id, event_id))
        conn.commit()
        cursor.close()

    def update_handball_player(self, conn, event_id, guilty_id):
        """Update handball guilty player"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE handball 
            SET guilty_id = %s
            WHERE event_id = %s
        """, (guilty_id, event_id))
        conn.commit()
        cursor.close()

    def update_substitution_players(self, conn, event_id, in_player_id, out_player_id):
        """Update substitution players"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE substitution 
            SET in_player_id = %s, out_player_id = %s
            WHERE event_id = %s
        """, (in_player_id, out_player_id, event_id))
        conn.commit()
        cursor.close()

    def update_ball_played_from_open_play(self, conn, event_id, from_open_play):
        """Update ball_played from_open_play"""
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE ball_played 
            SET from_open_play = %s
            WHERE event_id = %s
        """, (from_open_play, event_id))
        conn.commit()
        cursor.close()

    def get_match_players(self, conn, match_id):
        """Get all players in a match for dropdowns"""
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT DISTINCT
                p.player_id,
                p.player_name,
                p.jersey_num,
                t.team_name,
                t.team_id
            FROM match_lineup ml
            JOIN player p ON ml.player_id = p.player_id
            JOIN team t ON ml.team_id = t.team_id
            WHERE ml.match_id = %s
            ORDER BY t.team_name, p.jersey_num
        """, (match_id,))
        result = cursor.fetchall()
        cursor.close()
        return result