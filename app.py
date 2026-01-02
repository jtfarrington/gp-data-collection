import pyvisual as pv
from ui.ui import create_ui
from database import MatchDatabase
from datetime import datetime, timedelta
from PySide6.QtGui import QTextCursor  
from PySide6.QtCore import Qt
from location_popup import LocationPopup
import os
os.environ['QT_LOGGING_RULES'] = '*.debug=false;qt.qpa.fonts=false'
from data_export import DataExporter
import os
from datetime import datetime

# ===================================================
# ================ 1. LOGIC CODE ====================
# ===================================================

# Initialize database
db = MatchDatabase()


def collect_form_data(ui):
    """
    Collect all form data from the UI
    
    Args:
        ui: Dictionary containing UI components
        
    Returns:
        Dictionary with structured form data
    """
    page = ui['page_0']
    
    # Collect match details
    match_details = {
        'competition': page['competition'].text.strip(),
        'venue': page['venue'].text.strip(),
        'date': page['date'].text.strip()
    }
    
    # Collect home team data
    home_team = {
        'name': page['home_name_input'].text.strip(),
        'coach': page['h_coach_name'].text.strip(),
        'starters': {
            'gk': {
                'name': page['h_gk_name'].text.strip(),
                'jersey': page['h_gk_j_num'].text.strip()
            },
            'def': [
                {
                    'name': page['h_def_name_1'].text.strip(),
                    'jersey': page['h_def_j_num_1'].text.strip()
                },
                {
                    'name': page['h_def_name_2'].text.strip(),
                    'jersey': page['h_def_j_num_2'].text.strip()
                },
                {
                    'name': page['h_def_name_3'].text.strip(),
                    'jersey': page['h_def_j_num_3'].text.strip()
                },
                {
                    'name': page['h_def_name_4'].text.strip(),
                    'jersey': page['h_def_j_num_4'].text.strip()
                }
            ],
            'mid': [
                {
                    'name': page['h_mid_name_1'].text.strip(),
                    'jersey': page['h_mid_j_num_1'].text.strip()
                },
                {
                    'name': page['h_mid_name_2'].text.strip(),
                    'jersey': page['h_mid_j_num_2'].text.strip()
                },
                {
                    'name': page['h_mid_name_3'].text.strip(),
                    'jersey': page['h_mid_j_num_3'].text.strip()
                },
                {
                    'name': page['h_mid_name_4'].text.strip(),
                    'jersey': page['h_mid_j_num_4'].text.strip()
                }
            ],
            'fwd': [
                {
                    'name': page['h_fwd_name_1'].text.strip(),
                    'jersey': page['h_fwd_j_num_1'].text.strip()
                },
                {
                    'name': page['h_fwd_name_2'].text.strip(),
                    'jersey': page['h_fwd_j_num_2'].text.strip()
                }
            ]
        },
        'subs': [
            {
                'name': page['h_sub_name_1'].text.strip(),
                'jersey': page['h_sub_j_num_1'].text.strip()
            },
            {
                'name': page['h_sub_name_2'].text.strip(),
                'jersey': page['h_sub_j_num_2'].text.strip()
            },
            {
                'name': page['h_sub_name_3'].text.strip(),
                'jersey': page['h_sub_j_num_3'].text.strip()
            },
            {
                'name': page['h_sub_name_4'].text.strip(),
                'jersey': page['h_sub_j_num_4'].text.strip()
            },
            {
                'name': page['h_sub_name_5'].text.strip(),
                'jersey': page['h_sub_j_num_5'].text.strip()
            },
            {
                'name': page['h_sub_name_6'].text.strip(),
                'jersey': page['h_sub_j_num_6'].text.strip()
            },
            {
                'name': page['h_sub_name_7'].text.strip(),
                'jersey': page['h_sub_j_num_7'].text.strip()
            },
            {
                'name': page['h_sub_name_8'].text.strip(),
                'jersey': page['h_sub_j_num_8'].text.strip()
            },
            {
                'name': page['h_sub_name_9'].text.strip(),
                'jersey': page['h_sub_j_num_9'].text.strip()
            },
            {
                'name': page['h_sub_name_10'].text.strip(),
                'jersey': page['h_sub_j_num_10'].text.strip()
            },
            {
                'name': page['h_sub_name_11'].text.strip(),
                'jersey': page['h_sub_j_num_11'].text.strip()
            }
        ]
    }
    
    # Collect away team data
    away_team = {
        'name': page['away_name_input'].text.strip(),
        'coach': page['a_coach_name'].text.strip(),
        'starters': {
            'gk': {
                'name': page['a_gk_name'].text.strip(),
                'jersey': page['a_gk_j_num'].text.strip()
            },
            'def': [
                {
                    'name': page['a_def_name_1'].text.strip(),
                    'jersey': page['a_def_j_num_1'].text.strip()
                },
                {
                    'name': page['a_def_name_2'].text.strip(),
                    'jersey': page['a_def_j_num_2'].text.strip()
                },
                {
                    'name': page['a_def_name_3'].text.strip(),
                    'jersey': page['a_def_j_num_3'].text.strip()
                },
                {
                    'name': page['a_def_name_4'].text.strip(),
                    'jersey': page['a_def_j_num_4'].text.strip()
                }
            ],
            'mid': [
                {
                    'name': page['a_mid_name_1'].text.strip(),
                    'jersey': page['a_mid_j_num_1'].text.strip()
                },
                {
                    'name': page['a_mid_name_2'].text.strip(),
                    'jersey': page['a_mid_j_num_2'].text.strip()
                },
                {
                    'name': page['a_mid_name_3'].text.strip(),
                    'jersey': page['a_mid_j_num_3'].text.strip()
                },
                {
                    'name': page['a_mid_name_4'].text.strip(),
                    'jersey': page['a_mid_j_num_4'].text.strip()
                }
            ],
            'fwd': [
                {
                    'name': page['a_fwd_name_1'].text.strip(),
                    'jersey': page['a_fwd_j_num_1'].text.strip()
                },
                {
                    'name': page['a_fwd_name_2'].text.strip(),
                    'jersey': page['a_fwd_j_num_2'].text.strip()
                }
            ]
        },
        'subs': [
            {
                'name': page['a_sub_name_1'].text.strip(),
                'jersey': page['a_sub_j_num_1'].text.strip()
            },
            {
                'name': page['a_sub_name_2'].text.strip(),
                'jersey': page['a_sub_j_num_2'].text.strip()
            },
            {
                'name': page['a_sub_name_3'].text.strip(),
                'jersey': page['a_sub_j_num_3'].text.strip()
            },
            {
                'name': page['a_sub_name_4'].text.strip(),
                'jersey': page['a_sub_j_num_4'].text.strip()
            },
            {
                'name': page['a_sub_name_5'].text.strip(),
                'jersey': page['a_sub_j_num_5'].text.strip()
            },
            {
                'name': page['a_sub_name_6'].text.strip(),
                'jersey': page['a_sub_j_num_6'].text.strip()
            },
            {
                'name': page['a_sub_name_7'].text.strip(),
                'jersey': page['a_sub_j_num_7'].text.strip()
            },
            {
                'name': page['a_sub_name_8'].text.strip(),
                'jersey': page['a_sub_j_num_8'].text.strip()
            },
            {
                'name': page['a_sub_name_9'].text.strip(),
                'jersey': page['a_sub_j_num_9'].text.strip()
            },
            {
                'name': page['a_sub_name_10'].text.strip(),
                'jersey': page['a_sub_j_num_10'].text.strip()
            },
            {
                'name': page['a_sub_name_11'].text.strip(),
                'jersey': page['a_sub_j_num_11'].text.strip()
            }
        ]
    }
    
    return {
        'match_details': match_details,
        'home_team': home_team,
        'away_team': away_team
    }


def handle_submit(ui):
    """
    Handle the submit button click
    
    Args:
        ui: Dictionary containing UI components
        
    Returns:
        Tuple: (success: bool, match_id or None)
    """
    # Collect form data
    form_data = collect_form_data(ui)
    
    # Save to database
    success, result = db.save_match_data(form_data)
    
    if success:
        print(f"✓ Match saved successfully! Match ID: {result}")
        return True, result
    else:
        print(f"✗ Error saving match: {result}")
        return False, None


# ===================================================
# ============ PAGE 1 INITIALIZATION ================
# ===================================================


def initialize_page_1(ui):
    """
    Initialize page 1 with lineup data when navigating from page 0
    
    Args:
        ui: Dictionary containing UI components
    """
    match_id = ui.get('current_match_id')
    if not match_id:
        print("Error: No match_id found")
        return
    
    # Load lineup data from database
    lineup_data = db.load_lineup_data(match_id)
    if not lineup_data:
        print("Error: Could not load lineup data")
        return
    
    # Store lineup data in ui
    ui['lineup_data'] = lineup_data
    
    # Initialize match state
    ui['match_clock_start'] = None
    ui['match_clock_paused'] = False
    ui['match_clock_pause_time'] = None
    ui['current_player_id'] = None
    ui['current_team_id'] = None
    ui['pending_set_piece'] = None
    ui['pending_set_piece_team_id'] = None
    ui['event_log'] = []
    ui['match_started'] = False  # Match clock started
    ui['kickoff_recorded'] = False  # Kickoff happened, events allowed
    ui['kickoff_team_id'] = None  # Which team is kicking off
    ui['match_paused'] = False
    ui['pause_time'] = None
    ui['halftime_recorded'] = False
    ui['pending_kickoff'] = False  # Waiting for a player to take kickoff
    ui['overtime_1_recorded'] = False
    ui['overtime_2_recorded'] = False
    ui['pk_shootout_recorded'] = False
    ui['match_ended'] = False
    ui['pending_foul'] = False
    ui['foul_guilty_id'] = None
    ui['foul_innocent_id'] = None
    ui['foul_event_id'] = None
    ui['pending_card'] = None  # Stores card color when waiting for reason
    ui['pending_card_player_id'] = None
    ui['pending_card_team_id'] = None
    ui['pending_card_player_name'] = None
    ui['pending_card_jersey'] = None
    ui['pending_offside'] = False
    ui['offside_pass_event_id'] = None
    ui['offside_team_id'] = None
    ui['pending_handball'] = False
    ui['last_ball_received_event_id'] = None
    ui['last_ball_received_player_name'] = None
    ui['last_ball_received_jersey'] = None
    ui['pending_shot_result'] = False
    ui['pending_shot_event_id'] = None
    ui['pending_shot_block'] = False
    ui['pending_shot_save'] = False
    ui['pending_goal_kickoff'] = False
    ui['pending_substitution'] = False
    ui['substitution_team_id'] = None
    ui['substitution_in_player_id'] = None
    ui['substitution_in_player_name'] = None
    ui['substitution_in_jersey'] = None
    
    # Populate button labels
    populate_player_buttons(ui)


def populate_player_buttons(ui):
    """
    Populate all player and team buttons with names from lineup data
    
    Args:
        ui: Dictionary containing UI components
    """
    lineup = ui['lineup_data']
    page = ui['page_1']
    
    # Set team button labels
    page['home_button'].text = lineup['home_team']['team_name']
    page['away_button'].text = lineup['away_team']['team_name']
    
    # Home team players
    home_players = lineup['home_team']['players']
    
    # Home GK
    if home_players['gk']:
        gk = home_players['gk']
        page['h_gk'].text = f"{gk['jersey']} {gk['name']}"
    
    # Home Defenders
    for i, defender in enumerate(home_players['def'][:4], 1):
        page[f'h_def_{i}'].text = f"{defender['jersey']} {defender['name']}"
    
    # Home Midfielders
    for i, midfielder in enumerate(home_players['mid'][:4], 1):
        page[f'h_mid_{i}'].text = f"{midfielder['jersey']} {midfielder['name']}"
    
    # Home Forwards
    for i, forward in enumerate(home_players['fwd'][:2], 1):
        page[f'h_fwd_{i}'].text = f"{forward['jersey']} {forward['name']}"
    
    # Home Substitutes
    for i, sub in enumerate(home_players['sub'][:11], 1):
        page[f'h_sub_{i}'].text = f"{sub['jersey']} {sub['name']}"
    
    # Away team players
    away_players = lineup['away_team']['players']
    
    # Away GK
    if away_players['gk']:
        gk = away_players['gk']
        page['a_gk'].text = f"{gk['jersey']} {gk['name']}"
    
    # Away Defenders
    for i, defender in enumerate(away_players['def'][:4], 1):
        page[f'a_def_{i}'].text = f"{defender['jersey']} {defender['name']}"
    
    # Away Midfielders
    for i, midfielder in enumerate(away_players['mid'][:4], 1):
        page[f'a_mid_{i}'].text = f"{midfielder['jersey']} {midfielder['name']}"
    
    # Away Forwards
    for i, forward in enumerate(away_players['fwd'][:2], 1):
        page[f'a_fwd_{i}'].text = f"{forward['jersey']} {forward['name']}"
    
    # Away Substitutes
    for i, sub in enumerate(away_players['sub'][:11], 1):
        page[f'a_sub_{i}'].text = f"{sub['jersey']} {sub['name']}"


# ===================================================
# ============== MATCH CLOCK FUNCTIONS ==============
# ===================================================


def get_match_time(ui):
    """
    Get current match time in MM:SS format
    
    Args:
        ui: Dictionary containing UI components
        
    Returns:
        str: Time in MM:SS format or "00:00" if not started
    """
    if not ui.get('match_clock_start'):
        return "00:00"
    
    # If paused, calculate time up to pause
    if ui.get('match_paused') and ui.get('pause_time'):
        elapsed = ui['pause_time'] - ui['match_clock_start']
    else:
        elapsed = datetime.now() - ui['match_clock_start']
    
    total_seconds = int(elapsed.total_seconds())
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    return f"{minutes:02d}:{seconds:02d}"


def get_match_timestamp(ui):
    """
    Get current match timestamp for database storage
    
    Args:
        ui: Dictionary containing UI components
        
    Returns:
        datetime: Current timestamp
    """
    return datetime.now()


# ===================================================
# ============ EVENT HANDLING FUNCTIONS =============
# ===================================================


def handle_player_click(ui, player_id, team_id, player_name, jersey_num):
    """
    Handle when a player button is clicked
    """
    # Check if kickoff has been recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    # Check if match has ended
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    # Check if goal kickoff is pending
    if ui.get('pending_goal_kickoff'):
        print("✗ Kickoff required after goal - click 'kickoff' button first")
        return
    
    # Check if this is a kickoff action
    if ui.get('pending_kickoff'):
        # This player is taking the kickoff
        ui['pending_kickoff'] = False
        ui['current_player_id'] = player_id
        ui['current_team_id'] = team_id
        
        team_name = 'Home' if team_id == ui['lineup_data']['home_team']['team_id'] else 'Away'
        
        # Determine which period is starting
        if not ui.get('halftime_recorded'):
            period_name = "1ST HALF"
        elif not ui.get('overtime_1_recorded'):
            period_name = "2ND HALF"
        elif not ui.get('overtime_2_recorded'):
            period_name = "OVERTIME 1"
        else:
            period_name = "OVERTIME 2"
        
        # Log kickoff with team info
        ui['event_log'].append({
            'event_id': None,
            'timestamp': get_match_time(ui),
            'description': f"⚽ {period_name} KICKOFF - {team_name} (#{jersey_num} {player_name})"
        })
        update_event_log_display(ui)
        
        print(f"✓ {period_name} kickoff taken by {team_name} - #{jersey_num} {player_name}")
        print(f"→ Match is live! Click action (pass/shot) for kickoff.")
        
        return
    
    # Check if this is shot block flow
    if ui.get('pending_shot_block'):
        # This player blocked the shot
        shot_event_id = ui['pending_shot_event_id']
        
        # Record shot block event
        conn = db.get_connection()
        try:
            conn.start_transaction()
            
            # Insert base event for the block
            event_id = db.insert_event(
                conn,
                ui['current_match_id'],
                team_id,
                player_id,
                get_match_timestamp(ui)
            )
            
            # Insert ball_received
            db.insert_ball_received(conn, event_id)
            
            # Insert shot_block
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO shot_block (event_id, shot_event_id)
                VALUES (%s, %s)
            """, (event_id, shot_event_id))
            cursor.close()
            
            conn.commit()
            
            # Log block event
            ui['event_log'].append({
                'event_id': event_id,
                'timestamp': get_match_time(ui),
                'description': f"#{jersey_num} {player_name} | Shot blocked"
            })
            update_event_log_display(ui)
            
            print(f"✓ Shot block recorded: #{jersey_num} {player_name}")
            
            # Clear shot block state
            ui['pending_shot_block'] = False
            ui['pending_shot_event_id'] = None
            ui['pending_shot_player_name'] = None
            ui['pending_shot_jersey'] = None
            
            # Set this player as current
            ui['current_player_id'] = player_id
            ui['current_team_id'] = team_id
            
            # Clear last ball_received
            ui['last_ball_received_event_id'] = None
            ui['last_ball_received_player_name'] = None
            ui['last_ball_received_jersey'] = None
            
        except Exception as e:
            conn.rollback()
            print(f"✗ Error recording shot block: {e}")
            ui['pending_shot_block'] = False
        finally:
            conn.close()
        
        return
    
    # Check if this is offside flow
    if ui.get('pending_offside'):
        # This player was offside
        
        # Record offside event
        conn = db.get_connection()
        try:
            conn.start_transaction()
            
            # Insert base event for offside
            # The event is attributed to the player who was offside
            event_id = db.insert_event(
                conn,
                ui['current_match_id'],
                team_id,
                player_id,
                get_match_timestamp(ui)
            )
            
            # Insert offside event using new offside table
            db.insert_offside(conn, event_id, player_id)
            
            conn.commit()
            
            # Log offside
            ui['event_log'].append({
                'event_id': event_id,
                'timestamp': get_match_time(ui),
                'description': f"⚠️ OFFSIDE: #{jersey_num} {player_name}"
            })
            update_event_log_display(ui)
            
            print(f"✓ Offside recorded: #{jersey_num} {player_name}")
            print(f"→ Now click 'indirect' for the free kick")
            
            # Clear offside flag but keep waiting for indirect kick
            ui['pending_offside'] = False
            
            # Set pending set piece to indirect automatically
            ui['pending_set_piece'] = 'indirect'
            
        except Exception as e:
            conn.rollback()
            print(f"✗ Error recording offside: {e}")
            ui['pending_offside'] = False
        finally:
            conn.close()
        
        return
    
    # Check if this is foul flow
    if ui.get('pending_foul'):
        # First click after foul = guilty player
        if ui['foul_guilty_id'] is None:
            ui['foul_guilty_id'] = player_id
            ui['foul_guilty_team_id'] = team_id
            ui['foul_guilty_name'] = player_name
            ui['foul_guilty_jersey'] = jersey_num
            print(f"→ Guilty player: #{jersey_num} {player_name}. Now click the INNOCENT player.")
            return
        
        # Second click after foul = innocent player
        if ui['foul_innocent_id'] is None:
            ui['foul_innocent_id'] = player_id
            ui['foul_innocent_team_id'] = team_id
            ui['foul_innocent_name'] = player_name
            ui['foul_innocent_jersey'] = jersey_num
            
            # Record the foul event
            conn = db.get_connection()
            try:
                conn.start_transaction()
                
                # Insert base event (attributed to guilty player)
                event_id = db.insert_event(
                    conn,
                    ui['current_match_id'],
                    ui['foul_guilty_team_id'],
                    ui['foul_guilty_id'],
                    get_match_timestamp(ui)
                )
                
                # Insert foul with both players
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO foul (event_id, guilty_id, innocent_id, reason)
                    VALUES (%s, %s, %s, 'foul')
                """, (event_id, ui['foul_guilty_id'], ui['foul_innocent_id']))
                cursor.close()
                
                conn.commit()
                
                # Store event_id for potential card linking
                ui['foul_event_id'] = event_id
                
                # Log event
                ui['event_log'].append({
                    'event_id': event_id,
                    'timestamp': get_match_time(ui),
                    'description': f"FOUL: #{ui['foul_guilty_jersey']} {ui['foul_guilty_name']} on #{ui['foul_innocent_jersey']} {ui['foul_innocent_name']}"
                })
                update_event_log_display(ui)
                
                print(f"✓ Foul recorded: {ui['foul_guilty_name']} (guilty) on {ui['foul_innocent_name']} (innocent)")
                print(f"→ Now click set piece type (direct/indirect/penalty)")
                
                # Don't clear pending_foul yet - waiting for set piece
                
            except Exception as e:
                conn.rollback()
                print(f"✗ Error recording foul: {e}")
                # Clear foul state on error
                ui['pending_foul'] = False
                ui['foul_guilty_id'] = None
                ui['foul_innocent_id'] = None
            finally:
                conn.close()
            
            return
        
    # Check if this is handball flow
    if ui.get('pending_handball'):
    # This player committed handball
    
        # Record handball event
        conn = db.get_connection()
        try:
            conn.start_transaction()
            
            # Insert base event for handball
            # The event is attributed to the guilty player
            event_id = db.insert_event(
                conn,
                ui['current_match_id'],
                team_id,
                player_id,
                get_match_timestamp(ui)
            )
            
            # Insert handball event
            db.insert_handball(conn, event_id, player_id)
            
            conn.commit()
            
            # Log handball
            ui['event_log'].append({
                'event_id': event_id,
                'timestamp': get_match_time(ui),
                'description': f"🤚 HANDBALL: #{jersey_num} {player_name}"
            })
            update_event_log_display(ui)
            
            print(f"✓ Handball recorded: #{jersey_num} {player_name}")
            print(f"→ Now click set piece type (direct/indirect/penalty)")
            
            # Clear handball flag but wait for set piece
            ui['pending_handball'] = False
        
        except Exception as e:
            conn.rollback()
            print(f"✗ Error recording handball: {e}")
            ui['pending_handball'] = False
        finally:
            conn.close()
        
        return
    
    # Check if there's a pending set piece with team selected
    if ui.get('pending_set_piece') and ui.get('pending_set_piece_team_id'):
        set_piece_type = ui['pending_set_piece']
        set_piece_team_id = ui['pending_set_piece_team_id']
        
        # Validate player is from the correct team
        if player_id != set_piece_team_id and team_id != set_piece_team_id:
            print("✗ Player must be from the team taking the set piece")
            return
        
        # Create set piece event
        conn = db.get_connection()
        try:
            conn.start_transaction()
            
            # Insert base event (attributed to the team taking set piece and player)
            event_id = db.insert_event(
                conn,
                ui['current_match_id'],
                set_piece_team_id,
                player_id,
                get_match_timestamp(ui)
            )
            
            # Insert set piece
            db.insert_set_piece(conn, event_id, set_piece_type)
            
            conn.commit()
            
            # Log event
            ui['event_log'].append({
                'event_id': event_id,
                'timestamp': get_match_time(ui),
                'description': f"#{jersey_num} {player_name} | Set piece ({set_piece_type})"
            })
            
            # Update display
            update_event_log_display(ui)
            
            print(f"✓ Set piece recorded: {player_name} - {set_piece_type}")
            
        except Exception as e:
            conn.rollback()
            print(f"✗ Error recording set piece: {e}")
        finally:
            conn.close()
        
        # Clear pending set piece COMPLETELY
        ui['pending_set_piece'] = None
        ui['pending_set_piece_team_id'] = None
        
        if ui.get('pending_foul'):
            ui['pending_foul'] = False
            ui['foul_guilty_id'] = None
            ui['foul_innocent_id'] = None
            ui['foul_event_id'] = None

        return
    
    # Check if this is substitution flow
    if ui.get('pending_substitution'):
        # Check if player is from the correct team
        if team_id != ui['substitution_team_id']:
            print("✗ Player must be from the team making the substitution")
            return
        
        # First click after substitution = player coming IN
        if ui['substitution_in_player_id'] is None:
            ui['substitution_in_player_id'] = player_id
            ui['substitution_in_player_name'] = player_name
            ui['substitution_in_jersey'] = jersey_num
            print(f"→ Player coming IN: #{jersey_num} {player_name}. Now click player going OUT.")
            return
        
        # Second click after substitution = player going OUT
        in_player_id = ui['substitution_in_player_id']
        in_player_name = ui['substitution_in_player_name']
        in_jersey = ui['substitution_in_jersey']
        
        out_player_id = player_id
        out_player_name = player_name
        out_jersey = jersey_num
        
        # Record substitution event
        conn = db.get_connection()
        try:
            conn.start_transaction()
            
            # Insert base event for substitution (attributed to the team/player coming in)
            event_id = db.insert_event(
                conn,
                ui['current_match_id'],
                team_id,
                in_player_id,  # Event attributed to player coming in
                get_match_timestamp(ui)
            )
            
            # Insert substitution with both players
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO substitution (event_id, in_player_id, out_player_id)
                VALUES (%s, %s, %s)
            """, (event_id, in_player_id, out_player_id))
            cursor.close()
            
            conn.commit()
            
            # Log substitution
            ui['event_log'].append({
                'event_id': event_id,
                'timestamp': get_match_time(ui),
                'description': f"🔄 SUB: IN #{in_jersey} {in_player_name} | OUT #{out_jersey} {out_player_name}"
            })
            update_event_log_display(ui)
            
            print(f"✓ Substitution recorded")
            print(f"   IN: #{in_jersey} {in_player_name}")
            print(f"   OUT: #{out_jersey} {out_player_name}")
            
            # Clear substitution state
            ui['pending_substitution'] = False
            ui['substitution_team_id'] = None
            ui['substitution_in_player_id'] = None
            ui['substitution_in_player_name'] = None
            ui['substitution_in_jersey'] = None
            
        except Exception as e:
            conn.rollback()
            print(f"✗ Error recording substitution: {e}")
            # Clear substitution state on error
            ui['pending_substitution'] = False
            ui['substitution_team_id'] = None
            ui['substitution_in_player_id'] = None
        finally:
            conn.close()
        
        return
    
    # Normal player click - create ball_received event
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # If there's a previous ball_received event, mark it as other_ball_action
        if ui.get('last_ball_received_event_id') is not None:
            # Insert other_ball_action for the previous ball_received
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO other_ball_action (event_id)
                VALUES (%s)
            """, (ui['last_ball_received_event_id'],))
            cursor.close()
            
            # Add to event log
            ui['event_log'].append({
                'event_id': ui['last_ball_received_event_id'],
                'timestamp': get_match_time(ui),
                'description': f"#{ui['last_ball_received_jersey']} {ui['last_ball_received_player_name']} | Other ball action"
            })
        
        # Insert base event for current player
        event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            team_id,
            player_id,
            get_match_timestamp(ui)
        )
        
        # Insert ball_received
        db.insert_ball_received(conn, event_id)
        
        conn.commit()

        # Update display if we added other_ball_action
        if ui.get('last_ball_received_event_id') is not None:
            update_event_log_display(ui)
        
        # Store this as the last ball_received event
        ui['last_ball_received_event_id'] = event_id
        ui['last_ball_received_player_name'] = player_name
        ui['last_ball_received_jersey'] = jersey_num
        
        # Don't log ball_received to event log (it will show when action happens or becomes other_ball_action)
        # Just print to console for debugging
        print(f"✓ Ball received: {player_name} (waiting for action)")
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording ball received: {e}")
    finally:
        conn.close()

    # Set current player
    ui['current_player_id'] = player_id
    ui['current_team_id'] = team_id


def handle_pass_click(ui, pass_length, pass_height):
    """
    Handle pass button click
    
    Args:
        ui: Dictionary containing UI components
        pass_length: 'short', 'medium', or 'long'
        pass_height: 'high' or 'low'
    """

    # Check if match has ended
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    if ui.get('pending_kickoff'):
        print("✗ Click a player to take the kickoff first")
        return
    
    if not ui.get('current_player_id'):
        print("✗ No player selected")
        return
    
    # Get current player info
    player_name, jersey_num = get_player_name_and_jersey(ui, ui['current_player_id'])
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Insert base event
        event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            ui['current_team_id'],
            ui['current_player_id'],
            get_match_timestamp(ui)
        )
        
        # Determine if from open play
        from_open_play = ui.get('pending_set_piece') is None
        
        # Insert ball_played
        db.insert_ball_played(conn, event_id, from_open_play=from_open_play)
        
        # Insert pass
        db.insert_pass(conn, event_id, pass_length, pass_height)
        
        conn.commit()
        
        # Log event
        ui['event_log'].append({
            'event_id': event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{jersey_num} {player_name} | Pass ({pass_length}/{pass_height})"
        })
        
        # Update display
        update_event_log_display(ui)
        
        print(f"✓ Pass recorded: {pass_length} {pass_height}")

        # Clear last ball_received since this was followed by an action
        ui['last_ball_received_event_id'] = None
        ui['last_ball_received_player_name'] = None
        ui['last_ball_received_jersey'] = None
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording pass: {e}")
    finally:
        conn.close()

    # Check if kickoff has been recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return


def handle_shot_click(ui):
    """Handle shot button click"""
    
    # Validation
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    if ui.get('pending_kickoff'):
        print("✗ Click a player to take the kickoff first")
        return
    
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    if not ui.get('current_player_id'):
        print("✗ No player selected")
        return
    
    # Get current player info
    player_name, jersey_num = get_player_name_and_jersey(ui, ui['current_player_id'])
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Insert base event
        event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            ui['current_team_id'],
            ui['current_player_id'],
            get_match_timestamp(ui)
        )
        
        # Determine if from open play
        from_open_play = ui.get('pending_set_piece') is None
        
        # Insert ball_played
        db.insert_ball_played(conn, event_id, from_open_play=from_open_play)
        
        # Insert shot with NULL result for now
        db.insert_shot(conn, event_id)
        
        conn.commit()
        
        # Store shot event_id and wait for result
        ui['pending_shot_result'] = True
        ui['pending_shot_event_id'] = event_id
        ui['pending_shot_player_name'] = player_name
        ui['pending_shot_jersey'] = jersey_num
        
        print(f"✓ Shot recorded by #{jersey_num} {player_name}")
        print(f"→ Click shot result (over/wide/post/crossbar)")
        
        # Clear last ball_received since this was followed by an action
        ui['last_ball_received_event_id'] = None
        ui['last_ball_received_player_name'] = None
        ui['last_ball_received_jersey'] = None
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording shot: {e}")
    finally:
        conn.close()

    # Check if kickoff has been recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return

def handle_shot_result_click(ui, result):
    """
    Handle shot result button click
    
    Args:
        ui: Dictionary containing UI components
        result: Shot result ('over', 'over_left', 'over_right', 'wide_left', 
                'wide_right', 'post_left', 'post_right', 'crossbar')
    """
    # Check if we're waiting for a shot result
    if not ui.get('pending_shot_result'):
        print("✗ No shot waiting for result - click shot button first")
        return
    
    event_id = ui['pending_shot_event_id']
    player_name = ui['pending_shot_player_name']
    jersey_num = ui['pending_shot_jersey']
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Update the shot result
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE shot 
            SET result = %s
            WHERE event_id = %s
        """, (result, event_id))
        cursor.close()
        
        conn.commit()
        
        # Log event with result
        ui['event_log'].append({
            'event_id': event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{jersey_num} {player_name} | Shot ({result.replace('_', ' ')})"
        })
        
        # Update display
        update_event_log_display(ui)
        
        print(f"✓ Shot result recorded: {result}")
        
        # Clear pending shot result
        ui['pending_shot_result'] = False
        ui['pending_shot_event_id'] = None
        ui['pending_shot_player_name'] = None
        ui['pending_shot_jersey'] = None
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording shot result: {e}")
    finally:
        conn.close()

def handle_cross_click(ui, direction):
    """
    Handle cross button click
    
    Args:
        ui: Dictionary containing UI components
        direction: 'left' or 'right'
    """
    # Validation
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    if ui.get('pending_kickoff'):
        print("✗ Click a player to take the kickoff first")
        return
    
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    if not ui.get('current_player_id'):
        print("✗ No player selected")
        return
    
    # Get current player info
    player_name, jersey_num = get_player_name_and_jersey(ui, ui['current_player_id'])
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Insert base event
        event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            ui['current_team_id'],
            ui['current_player_id'],
            get_match_timestamp(ui)
        )
        
        # Determine if from open play
        from_open_play = ui.get('pending_set_piece') is None
        
        # Insert ball_played
        db.insert_ball_played(conn, event_id, from_open_play=from_open_play)
        
        db.insert_cross(conn, event_id, intention='other', technique='other')
        
        conn.commit()
        
        # Log event
        ui['event_log'].append({
            'event_id': event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{jersey_num} {player_name} | Cross ({direction})"
        })
        
        # Update display
        update_event_log_display(ui)
        
        print(f"✓ Cross recorded: {direction}")

        # Clear last ball_received since this was followed by an action
        ui['last_ball_received_event_id'] = None
        ui['last_ball_received_player_name'] = None
        ui['last_ball_received_jersey'] = None
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording cross: {e}")
    finally:
        conn.close()
    
def handle_set_piece_click(ui, set_piece_type):
    """
    Handle set piece button click - sets pending state
    
    Args:
        ui: Dictionary containing UI components
        set_piece_type: Type of set piece
    """
    # Check if match has started and kickoff recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    # Check if match has ended
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    # Check if this is completing a foul sequence
    if ui.get('pending_foul') and ui.get('foul_innocent_id') is not None:
        # Only allow direct, indirect, or penalty after a foul
        if set_piece_type not in ['direct', 'indirect', 'penalty']:
            print(f"✗ After a foul, only direct/indirect/penalty kicks are allowed")
            return
        
        print(f"✓ Set piece type selected: {set_piece_type}")

    # Check if this is after offside
    if ui.get('offside_pass_event_id') is not None:
        # Only allow indirect after offside
        if set_piece_type != 'indirect':
            print(f"✗ After offside, only indirect kick is allowed")
            return
        
        # Clear offside state when indirect is confirmed
        ui['offside_pass_event_id'] = None
    
    # Set pending set piece (no team selection needed)
    ui['pending_set_piece'] = set_piece_type
    ui['pending_set_piece_team_id'] = None  
    print(f"→ Set piece pending: {set_piece_type}. Click team taking it.")

def handle_handball_click(ui):
    """Handle handball button click - starts handball flow"""
    
    # Validation
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    # Start handball flow
    ui['pending_handball'] = True
    
    print("→ Handball called. Click the GUILTY player.")

def handle_ball_won_click(ui):
    """Handle ball_won button click"""

    # Check if match has ended
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    if not ui.get('current_player_id'):
        print("✗ No player selected")
        return
    
    # Get current player info
    player_name, jersey_num = get_player_name_and_jersey(ui, ui['current_player_id'])
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Insert base event
        event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            ui['current_team_id'],
            ui['current_player_id'],
            get_match_timestamp(ui)
        )
        
        # Insert ball_received
        db.insert_ball_received(conn, event_id)
        
        # Insert ball_won
        db.insert_ball_won(conn, event_id)
        
        conn.commit()
        
        # Log event
        ui['event_log'].append({
            'event_id': event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{jersey_num} {player_name} | Ball won"
        })
        
        # Update display
        update_event_log_display(ui)
        
        print(f"✓ Ball won recorded")

        # Clear last ball_received since this was followed by an action
        ui['last_ball_received_event_id'] = None
        ui['last_ball_received_player_name'] = None
        ui['last_ball_received_jersey'] = None
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording ball won: {e}")
    finally:
        conn.close()

    # Check if kickoff has been recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return    


def handle_clearance_click(ui):
    """Handle clearance button click"""

    # Check if match has ended
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    if not ui.get('current_player_id'):
        print("✗ No player selected")
        return
    
    # Get current player info
    player_name, jersey_num = get_player_name_and_jersey(ui, ui['current_player_id'])
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Insert base event
        event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            ui['current_team_id'],
            ui['current_player_id'],
            get_match_timestamp(ui)
        )
        
        # Insert ball_received
        db.insert_ball_received(conn, event_id)
        
        # Insert clearance
        db.insert_clearance(conn, event_id)
        
        conn.commit()
        
        # Log event
        ui['event_log'].append({
            'event_id': event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{jersey_num} {player_name} | Clearance"
        })
        
        # Update display
        update_event_log_display(ui)
        
        print(f"✓ Clearance recorded")

        # Clear last ball_received since this was followed by an action
        ui['last_ball_received_event_id'] = None
        ui['last_ball_received_player_name'] = None
        ui['last_ball_received_jersey'] = None
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording clearance: {e}")
    finally:
        conn.close()

    # Check if kickoff has been recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return

def handle_shot_blocked_click(ui):
    """Handle shot blocked button click - waits for player who blocked it"""
    
    # Check if we're waiting for a shot result
    if not ui.get('pending_shot_result'):
        print("✗ No shot waiting for result - click shot button first")
        return
    
    event_id = ui['pending_shot_event_id']
    player_name = ui['pending_shot_player_name']
    jersey_num = ui['pending_shot_jersey']
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Update the shot result to 'blocked'
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE shot 
            SET result = 'blocked'
            WHERE event_id = %s
        """, (event_id,))
        cursor.close()
        
        conn.commit()
        
        # Log shot event
        ui['event_log'].append({
            'event_id': event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{jersey_num} {player_name} | Shot (blocked)"
        })
        update_event_log_display(ui)
        
        print(f"✓ Shot blocked recorded")
        print(f"→ Click player who BLOCKED the shot")
        
        # Clear shot result flag but set block flag
        ui['pending_shot_result'] = False
        ui['pending_shot_block'] = True
        # Keep shot_event_id for linking
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording shot blocked: {e}")
    finally:
        conn.close()

def handle_shot_saved_click(ui):
    """Handle shot saved button click - auto-assigns to opposing GK"""
    
    # Check if we're waiting for a shot result
    if not ui.get('pending_shot_result'):
        print("✗ No shot waiting for result - click shot button first")
        return
    
    event_id = ui['pending_shot_event_id']
    player_name = ui['pending_shot_player_name']
    jersey_num = ui['pending_shot_jersey']
    shot_team_id = ui['current_team_id']
    
    # Determine which GK saved it (opposing team's GK)
    lineup = ui['lineup_data']
    if shot_team_id == lineup['home_team']['team_id']:
        # Home team shot, away GK saved
        gk = lineup['away_team']['players']['gk']
        gk_team_id = lineup['away_team']['team_id']
    else:
        # Away team shot, home GK saved
        gk = lineup['home_team']['players']['gk']
        gk_team_id = lineup['home_team']['team_id']
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Update the shot result to 'saved'
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE shot 
            SET result = 'saved'
            WHERE event_id = %s
        """, (event_id,))
        
        # Create event for GK saving the shot
        save_event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            gk_team_id,
            gk['player_id'],
            get_match_timestamp(ui)
        )
        
        # Insert ball_received for GK
        db.insert_ball_received(conn, save_event_id)
        
        # Insert shot_save
        cursor.execute("""
            INSERT INTO shot_save (event_id, shot_event_id)
            VALUES (%s, %s)
        """, (save_event_id, event_id))
        
        cursor.close()
        conn.commit()
        
        # Log shot event
        ui['event_log'].append({
            'event_id': event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{jersey_num} {player_name} | Shot (saved)"
        })
        
        # Log save event
        ui['event_log'].append({
            'event_id': save_event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{gk['jersey']} {gk['name']} | Shot saved"
        })
        
        update_event_log_display(ui)
        
        print(f"✓ Shot saved by #{gk['jersey']} {gk['name']}")
        
        # Set GK as current player
        ui['current_player_id'] = gk['player_id']
        ui['current_team_id'] = gk_team_id
        
        # Clear shot state
        ui['pending_shot_result'] = False
        ui['pending_shot_event_id'] = None
        ui['pending_shot_player_name'] = None
        ui['pending_shot_jersey'] = None
        
        # Clear last ball_received (GK now has the ball)
        ui['last_ball_received_event_id'] = None
        ui['last_ball_received_player_name'] = None
        ui['last_ball_received_jersey'] = None
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording shot saved: {e}")
    finally:
        conn.close()
    
def handle_goal_click(ui):
    """Handle goal button click - creates goal event and requires kickoff"""
    
    # Check if we're waiting for a shot result
    if not ui.get('pending_shot_result'):
        print("✗ No shot waiting for result - click shot button first")
        return
    
    event_id = ui['pending_shot_event_id']
    player_name = ui['pending_shot_player_name']
    jersey_num = ui['pending_shot_jersey']
    scoring_team_id = ui['current_team_id']
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Update the shot result to 'goal'
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE shot 
            SET result = 'goal'
            WHERE event_id = %s
        """, (event_id,))
        
        # Create goal event (same event_id as the shot, references the shot)
        # Note: goal has its own event_id, but references the shot_event_id
        goal_event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            scoring_team_id,
            ui['current_player_id'],
            get_match_timestamp(ui)
        )
        
        # Insert goal with NULL goal_zone for now (can be filled later)
        cursor.execute("""
            INSERT INTO goal (event_id, shot_event_id, goal_zone)
            VALUES (%s, %s, NULL)
        """, (goal_event_id, event_id))
        
        cursor.close()
        conn.commit()
        
        # Determine which team scored
        lineup = ui['lineup_data']
        if scoring_team_id == lineup['home_team']['team_id']:
            scoring_team_name = lineup['home_team']['team_name']
        else:
            scoring_team_name = lineup['away_team']['team_name']
        
        # Log shot event
        ui['event_log'].append({
            'event_id': event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{jersey_num} {player_name} | Shot (goal)"
        })
        
        # Log goal event
        ui['event_log'].append({
            'event_id': goal_event_id,
            'timestamp': get_match_time(ui),
            'description': f"⚽ GOAL! {scoring_team_name} - #{jersey_num} {player_name}"
        })
        
        update_event_log_display(ui)
        
        print(f"✓ ⚽ GOAL scored by #{jersey_num} {player_name}!")
        print(f"→ Kickoff required - click 'kickoff' button")
        
        # Set flag for required kickoff
        ui['pending_goal_kickoff'] = True
        
        # Clear shot state
        ui['pending_shot_result'] = False
        ui['pending_shot_event_id'] = None
        ui['pending_shot_player_name'] = None
        ui['pending_shot_jersey'] = None
        
        # Clear last ball_received
        ui['last_ball_received_event_id'] = None
        ui['last_ball_received_player_name'] = None
        ui['last_ball_received_jersey'] = None
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording goal: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()

def handle_own_goal_click(ui):
    """Handle own goal button click - can occur after any event or directly"""
    
    # Validation
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    if not ui.get('current_player_id'):
        print("✗ No player selected")
        return
    
    # Get current player info (the player who scored the own goal)
    player_name, jersey_num = get_player_name_and_jersey(ui, ui['current_player_id'])
    own_goal_team_id = ui['current_team_id']
    
    # Determine which team benefits (opposing team)
    lineup = ui['lineup_data']
    if own_goal_team_id == lineup['home_team']['team_id']:
        # Home player scored own goal, away team benefits
        benefiting_team_name = lineup['away_team']['team_name']
        own_goal_team_name = lineup['home_team']['team_name']
    else:
        # Away player scored own goal, home team benefits
        benefiting_team_name = lineup['home_team']['team_name']
        own_goal_team_name = lineup['away_team']['team_name']
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Create own goal event attributed to the player who scored it
        own_goal_event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            own_goal_team_id,
            ui['current_player_id'],
            get_match_timestamp(ui)
        )
        
        # Insert own goal using new own_goal table
        db.insert_own_goal(conn, own_goal_event_id)
        
        conn.commit()
        
        # Log own goal event
        ui['event_log'].append({
            'event_id': own_goal_event_id,
            'timestamp': get_match_time(ui),
            'description': f"⚽ OWN GOAL! {benefiting_team_name} benefits - #{jersey_num} {player_name} ({own_goal_team_name})"
        })
        
        update_event_log_display(ui)
        
        print(f"✓ Own goal by #{jersey_num} {player_name} ({own_goal_team_name})")
        print(f"✓ {benefiting_team_name} benefits from own goal")
        print(f"→ Kickoff required - {own_goal_team_name} will restart - click 'kickoff' button")
        
        # Set flag for required kickoff (same team that conceded restarts)
        ui['pending_goal_kickoff'] = True
        
        # Clear last ball_received
        ui['last_ball_received_event_id'] = None
        ui['last_ball_received_player_name'] = None
        ui['last_ball_received_jersey'] = None
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording own goal: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()

def handle_card_click(ui, card_color):
    """Handle card button click - starts card flow"""
    
    # Validation
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    if not ui.get('current_player_id'):
        print("✗ No player selected - click player first, then card")
        return
    
    # Store card info and wait for reason
    ui['pending_card'] = card_color
    ui['pending_card_player_id'] = ui['current_player_id']
    ui['pending_card_team_id'] = ui['current_team_id']
    
    player_name, jersey_num = get_player_name_and_jersey(ui, ui['current_player_id'])
    ui['pending_card_player_name'] = player_name
    ui['pending_card_jersey'] = jersey_num
    
    print(f"→ {card_color} card for #{jersey_num} {player_name}. Click reason: 'foul' or 'unfairness'")

def handle_foul_click(ui):
    """Handle foul button click - starts foul recording flow"""
    
    # Validation
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    # Start foul flow
    ui['pending_foul'] = True
    ui['foul_guilty_id'] = None
    ui['foul_innocent_id'] = None
    ui['foul_event_id'] = None
    
    print("→ Foul called. Click the GUILTY player.")

def handle_card_reason_foul(ui):
    """Handle when foul button is clicked as card reason"""
    
    if not ui.get('pending_card'):
        # Normal foul button behavior
        handle_foul_click(ui)
        return
    
    # This is a card reason
    card_color = ui['pending_card']
    player_id = ui['pending_card_player_id']
    team_id = ui['pending_card_team_id']
    player_name = ui['pending_card_player_name']
    jersey_num = ui['pending_card_jersey']
    
    # Get the foul_event_id if this card is related to the recent foul
    foul_event_id = ui.get('foul_event_id')
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Insert base event
        event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            team_id,
            player_id,
            get_match_timestamp(ui)
        )
        
        # Insert card with foul reason
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO card (event_id, foul_event_id, reason, color)
            VALUES (%s, %s, 'foul', %s)
        """, (event_id, foul_event_id, card_color))
        cursor.close()
        
        conn.commit()
        
        # Log event
        ui['event_log'].append({
            'event_id': event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{jersey_num} {player_name} | {card_color.replace('_', ' ').title()} card (foul)"
        })
        update_event_log_display(ui)
        
        print(f"✓ {card_color} card recorded for {player_name} (reason: foul)")
        
        # Clear card state
        ui['pending_card'] = None
        ui['pending_card_player_id'] = None
        ui['pending_card_team_id'] = None
        ui['pending_card_player_name'] = None
        ui['pending_card_jersey'] = None
        
        # Clear foul_event_id since card was issued
        ui['foul_event_id'] = None
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording card: {e}")
    finally:
        conn.close()


def handle_card_reason_unfairness(ui):
    """Handle when unfairness button is clicked as card reason"""
    
    if not ui.get('pending_card'):
        print("✗ Click player → card first before selecting reason")
        return
    
    # This is a card reason
    card_color = ui['pending_card']
    player_id = ui['pending_card_player_id']
    team_id = ui['pending_card_team_id']
    player_name = ui['pending_card_player_name']
    jersey_num = ui['pending_card_jersey']
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Insert base event
        event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            team_id,
            player_id,
            get_match_timestamp(ui)
        )
        
        # Insert card with unfairness reason
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO card (event_id, foul_event_id, reason, color)
            VALUES (%s, NULL, 'unfairness', %s)
        """, (event_id, card_color))
        cursor.close()
        
        conn.commit()
        
        # Log event
        ui['event_log'].append({
            'event_id': event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{jersey_num} {player_name} | {card_color.replace('_', ' ').title()} card (unfairness)"
        })
        update_event_log_display(ui)
        
        print(f"✓ {card_color} card recorded for {player_name} (reason: unfairness)")
        
        # Clear card state
        ui['pending_card'] = None
        ui['pending_card_player_id'] = None
        ui['pending_card_team_id'] = None
        ui['pending_card_player_name'] = None
        ui['pending_card_jersey'] = None
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording card: {e}")
    finally:
        conn.close()

def handle_offside_click(ui):
    """Handle offside button click - marks last pass as offside"""
    
    # Validation
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    # Check if there's a recent pass event
    if not ui.get('event_log') or len(ui['event_log']) == 0:
        print("✗ No pass to mark as offside")
        return
    
    # Get the last event
    last_event = ui['event_log'][-1]
    
    # Check if it was a pass
    if 'Pass' not in last_event['description']:
        print("✗ Last event was not a pass - offside can only follow a pass")
        return
    
    # Start offside flow
    ui['pending_offside'] = True
    ui['offside_pass_event_id'] = last_event['event_id']
    
    # Get the team that will receive the indirect kick (defending team)
    # This is the opposite team from the player who made the pass
    ui['offside_team_id'] = ui['current_team_id']  # Team that made the offside pass
    
    print(f"→ Offside called on the pass. Click the player who was OFFSIDE.")

def handle_duel_click(ui, context):
    """
    Handle duel button click
    
    Args:
        ui: Dictionary containing UI components
        context: 'ground' or 'aerial'
    """
    # Validation
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    if ui.get('pending_kickoff'):
        print("✗ Click a player to take the kickoff first")
        return
    
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    if not ui.get('current_player_id'):
        print("✗ No player selected")
        return
    
    # Get current player info
    player_name, jersey_num = get_player_name_and_jersey(ui, ui['current_player_id'])
    
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        # Insert base event
        event_id = db.insert_event(
            conn,
            ui['current_match_id'],
            ui['current_team_id'],
            ui['current_player_id'],
            get_match_timestamp(ui)
        )
        
        # Insert duel with NULL winner/loser for now
        db.insert_duel(conn, event_id, context)
        
        conn.commit()
        
        # Log event
        ui['event_log'].append({
            'event_id': event_id,
            'timestamp': get_match_time(ui),
            'description': f"#{jersey_num} {player_name} | {context.title()} duel"
        })
        
        # Update display
        update_event_log_display(ui)
        
        print(f"✓ {context.title()} duel recorded")
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording duel: {e}")
    finally:
        conn.close()

    # Check if kickoff has been recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return

def handle_substitution_click(ui, team_id):
    """
    Handle substitution button click - starts substitution flow
    
    Args:
        ui: Dictionary containing UI components
        team_id: The team making the substitution (home or away)
    """
    # Validation
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    # Start substitution flow
    ui['pending_substitution'] = True
    ui['substitution_team_id'] = team_id
    ui['substitution_in_player_id'] = None
    ui['substitution_in_player_name'] = None
    ui['substitution_in_jersey'] = None
    
    # Determine team name
    lineup = ui['lineup_data']
    if team_id == lineup['home_team']['team_id']:
        team_name = lineup['home_team']['team_name']
    else:
        team_name = lineup['away_team']['team_name']
    
    print(f"→ Substitution for {team_name}. Click player coming IN (substitute).")


def handle_team_click(ui, team_id):
    """
    Handle team button click (only for kickoff team selection)
    
    Args:
        ui: Dictionary containing UI components
        team_id: The team's database ID
    """
    
    # Scenario 1: Set piece team selection
    if ui.get('pending_set_piece'):
        ui['pending_set_piece_team_id'] = team_id
        team_name = 'Home' if team_id == ui['lineup_data']['home_team']['team_id'] else 'Away'
        print(f"→ Set piece for {team_name} team. Click player taking {ui['pending_set_piece']}.")
        return


def handle_start_match_click(ui):
    """Handle start match button click"""

    # Validate playing direction is selected
    playing_left = ui['page_1']['playing_left_dropdown'].currentText()
    if playing_left == "Select Team":
        print("✗ Please select which team is playing left")
        return

    # Check if match has ended
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    if ui.get('match_started'):
        print("Match already started")
        return
    
    # Validate that match has been created
    if not ui.get('current_match_id'):
        print("✗ Please create a match first (set teams and lineups)")
        return
    
    # Get team IDs from database
    conn = db.get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT home_id, away_id
            FROM match_metadata
            WHERE match_id = %s
        """, (ui['current_match_id'],))
        match_data = cursor.fetchone()
        cursor.close()
        
        if not match_data:
            print("✗ Match not found")
            return
        
        home_team_id = match_data['home_id']
        away_team_id = match_data['away_id']
        
        # Determine which team is on left
        if playing_left == "Home Team":
            left_team_id = home_team_id
        else:  # Away Team
            left_team_id = away_team_id
        
        # Save playing direction to database
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO match_sides (match_id, left_team_first_half)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE left_team_first_half = %s
        """, (ui['current_match_id'], left_team_id, left_team_id))
        conn.commit()
        cursor.close()
        
        print(f"✓ {playing_left} will start on the left side")
        
    except Exception as e:
        print(f"✗ Error saving playing direction: {e}")
        return
    finally:
        conn.close()
    
    # Lock the dropdown (disable it)
    ui['page_1']['playing_left_dropdown'].setEnabled(False)
    
    # Start match clock
    ui['match_clock_start'] = datetime.now()
    ui['match_started'] = True
    print(f"✓ Match started at {get_match_time(ui)}")
    print(f"Click Kickoff -> Player Name -> Action")
    
def handle_kickoff_click(ui):
    """Handle kickoff button click"""

    # Check if match has ended
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    # Scenario 1: First kickoff (start of match)
    if not ui.get('kickoff_recorded'):
        # Check if match started
        if not ui.get('match_started'):
            print("✗ Start the match first")
            return
        
        # Record kickoff timestamp in match_flow table (team will be determined by first action)
        conn = db.get_connection()
        try:
            conn.start_transaction()
            
            cursor = conn.cursor()
            
            # Insert into match_flow table
            kickoff_time = get_match_timestamp(ui)
            cursor.execute("""
                INSERT INTO match_flow (match_id, kickoff, halftime)
                VALUES (%s, %s, %s)
            """, (ui['current_match_id'], kickoff_time, kickoff_time))  # Placeholder for halftime
            
            conn.commit()
            cursor.close()
            
            ui['kickoff_recorded'] = True
            ui['pending_kickoff'] = True
            
            print(f"✓ Kickoff ready - click player to take kickoff")
            
        except Exception as e:
            conn.rollback()
            print(f"✗ Error recording kickoff: {e}")
        finally:
            conn.close()
        
        return
    
    # Scenario 2: Kickoff after pause (halftime, overtime 1, or overtime 2)
    if ui.get('match_paused'):
        # Calculate how long the match was paused
        pause_duration = datetime.now() - ui['pause_time']
        
        # Adjust the match start time to account for pause
        ui['match_clock_start'] = ui['match_clock_start'] + pause_duration
        
        # Unpause
        ui['match_paused'] = False
        ui['pause_time'] = None
        ui['pending_kickoff'] = True
        
        # Determine which period is starting
        if not ui.get('halftime_recorded'):
            period_name = "1st Half"  # Should not happen, but just in case
        elif not ui.get('overtime_1_recorded'):
            period_name = "2nd Half"
        elif not ui.get('overtime_2_recorded'):
            period_name = "Overtime 1"
        else:
            period_name = "Overtime 2"
        
        print(f"✓ {period_name} kickoff ready - click player to take kickoff")
        
        return
    
    # Scenario 3: Kickoff during play (after goal)
    if ui.get('pending_goal_kickoff'):
        # Clear the goal kickoff flag
        ui['pending_goal_kickoff'] = False

    # Set pending kickoff (player will take it)    
    ui['pending_kickoff'] = True
    print(f"✓ Kickoff ready - click player to take kickoff")

def handle_halftime_click(ui):
    """Handle halftime button click"""
    
    # Check if match started
    if not ui.get('match_started'):
        print("✗ Match hasn't started")
        return
    
    # Check if kickoff recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Match hasn't kicked off yet")
        return
    
    # Check if already at halftime
    if ui.get('halftime_recorded'):
        print("✗ Halftime already recorded")
        return
    
    # Check if match paused
    if ui.get('match_paused'):
        print("✗ Match is already paused")
        return
    
    # Check if match has ended
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    # Pause the clock
    ui['match_paused'] = True
    ui['pause_time'] = datetime.now()
    ui['halftime_recorded'] = True
    
    current_time = get_match_time(ui)
    
    # Update match_flow table with halftime timestamp
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        cursor = conn.cursor()
        
        halftime_timestamp = get_match_timestamp(ui)
        cursor.execute("""
            UPDATE match_flow 
            SET halftime = %s
            WHERE match_id = %s
        """, (halftime_timestamp, ui['current_match_id']))
        
        conn.commit()
        cursor.close()
        
        # Log to event log
        ui['event_log'].append({
            'event_id': None,
            'timestamp': current_time,
            'description': f"⏸️ HALFTIME"
        })
        update_event_log_display(ui)
        
        print(f"✓ Halftime recorded at {current_time}")
        print(f"→ Clock paused. Click 'kickoff' to start second half.")
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording halftime: {e}")
    finally:
        conn.close()

def handle_overtime_click(ui, overtime_period):
    """
    Handle overtime button click
    
    Args:
        ui: Dictionary containing UI components
        overtime_period: 1 or 2 for first or second overtime
    """
    period_name = f"overtime_{overtime_period}"
    recorded_key = f'overtime_{overtime_period}_recorded'
    
    # Check if match started
    if not ui.get('match_started'):
        print("✗ Match hasn't started")
        return
    
    # Check if kickoff recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Match hasn't kicked off yet")
        return
    
    # Check if already recorded
    if ui.get(recorded_key):
        print(f"✗ Overtime {overtime_period} already recorded")
        return
    
    # For overtime 2, check if overtime 1 was recorded
    if overtime_period == 2 and not ui.get('overtime_1_recorded'):
        print("✗ Must record overtime 1 before overtime 2")
        return
    
    # Check if match paused
    if ui.get('match_paused'):
        print("✗ Match is already paused")
        return
    
    # Check if match has ended
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    # Pause the clock
    ui['match_paused'] = True
    ui['pause_time'] = datetime.now()
    ui[recorded_key] = True
    
    current_time = get_match_time(ui)
    
    # Update match_flow table with overtime timestamp
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        cursor = conn.cursor()
        
        overtime_timestamp = get_match_timestamp(ui)
        cursor.execute(f"""
            UPDATE match_flow 
            SET {period_name} = %s
            WHERE match_id = %s
        """, (overtime_timestamp, ui['current_match_id']))
        
        conn.commit()
        cursor.close()
        
        # Determine what period just ended
        if overtime_period == 1:
            period_ended = "REGULATION"
        else:  # overtime_period == 2
            period_ended = "OVERTIME 1"
        
        # Log to event log
        ui['event_log'].append({
            'event_id': None,
            'timestamp': current_time,
            'description': f"⏸️ END OF {period_ended}"
        })
        update_event_log_display(ui)
        
        print(f"✓ End of {period_ended} at {current_time}")
        print(f"→ Clock paused. Click 'kickoff' to start Overtime {overtime_period}.")
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording overtime {overtime_period}: {e}")
    finally:
        conn.close()

def handle_pk_shootout_click(ui):
    """Handle pk shootout button click"""
    
    # Check if match started
    if not ui.get('match_started'):
        print("✗ Match hasn't started")
        return
    
    # Check if kickoff recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Match hasn't kicked off yet")
        return
    
    # Check if already recorded
    if ui.get('pk_shootout_recorded'):
        print("✗ PK shootout already recorded")
        return
    
    # Check if match paused
    if ui.get('match_paused'):
        print("✗ Match is already paused")
        return
    
    # Check if match has ended
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    # Pause the clock (shootout doesn't use match clock)
    ui['match_paused'] = True
    ui['pause_time'] = datetime.now()
    ui['pk_shootout_recorded'] = True
    
    current_time = get_match_time(ui)
    
    # Update match_flow table with pk_shootout timestamp
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        cursor = conn.cursor()
        
        pk_timestamp = get_match_timestamp(ui)
        cursor.execute("""
            UPDATE match_flow 
            SET pk_shootout = %s
            WHERE match_id = %s
        """, (pk_timestamp, ui['current_match_id']))
        
        conn.commit()
        cursor.close()
        
        # Determine what period just ended
        if ui.get('overtime_2_recorded'):
            period_ended = "OVERTIME 2"
        elif ui.get('overtime_1_recorded'):
            period_ended = "OVERTIME 1"
        elif ui.get('halftime_recorded'):
            period_ended = "2ND HALF"
        else:
            period_ended = "1ST HALF"
        
        # Log to event log
        ui['event_log'].append({
            'event_id': None,
            'timestamp': current_time,
            'description': f"⏸️ END OF {period_ended}"
        })
        ui['event_log'].append({
            'event_id': None,
            'timestamp': current_time,
            'description': f"🎯 PENALTY SHOOTOUT BEGINS"
        })
        update_event_log_display(ui)
        
        print(f"✓ End of {period_ended} at {current_time}")
        print(f"✓ Penalty shootout begins")
        print(f"→ Record penalty shots. Clock is paused.")
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error recording pk shootout: {e}")
    finally:
        conn.close()

def handle_pause_match_click(ui):
    """Handle pause/unpause match button click"""
    
    # Check if match started
    if not ui.get('match_started'):
        print("✗ Match hasn't started")
        return
    
    # Check if kickoff recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Match hasn't kicked off yet")
        return
    
    # Check if match ended
    if ui.get('match_ended'):
        print("✗ Match has already ended")
        return
    
    current_time = get_match_time(ui)
    
    # Toggle pause state
    if ui.get('match_paused'):
        # UNPAUSE
        # Calculate how long the match was paused
        pause_duration = datetime.now() - ui['pause_time']
        
        # Adjust the match start time to account for pause
        ui['match_clock_start'] = ui['match_clock_start'] + pause_duration
        
        # Unpause
        ui['match_paused'] = False
        ui['pause_time'] = None
        
        # Update button text
        ui['page_1']['pause_match_button'].text = 'pause_match'
        
        # Log to event log
        ui['event_log'].append({
            'event_id': None,
            'timestamp': get_match_time(ui),
            'description': f"▶️ MATCH RESUMED"
        })
        update_event_log_display(ui)
        
        print(f"✓ Match resumed")
        
    else:
        # PAUSE
        ui['match_paused'] = True
        ui['pause_time'] = datetime.now()
        
        # Update button text
        ui['page_1']['pause_match_button'].text = 'unpause_match'
        
        # Log to event log
        ui['event_log'].append({
            'event_id': None,
            'timestamp': current_time,
            'description': f"⏸️ MATCH PAUSED"
        })
        update_event_log_display(ui)
        
        print(f"✓ Match paused at {current_time}")

def handle_end_match_click(ui):
    """Handle end match button click"""
    
    # Check if match started
    if not ui.get('match_started'):
        print("✗ Match hasn't started")
        return
    
    # Check if kickoff recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Match hasn't kicked off yet")
        return
    
    # Check if already ended
    if ui.get('match_ended'):
        print("✗ Match has already ended")
        return
    
    # Check if match has ended
    if ui.get('match_ended'):
        print("✗ Cannot record events - match has ended")
        return
    
    # Get current time before stopping clock
    current_time = get_match_time(ui)
    end_timestamp = get_match_timestamp(ui)
    
    # Stop the clock
    ui['match_ended'] = True
    ui['match_paused'] = True
    ui['pause_time'] = datetime.now()
    
    # Update match_metadata table with match_end timestamp
    conn = db.get_connection()
    try:
        conn.start_transaction()
        
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE match_metadata 
            SET match_end = %s
            WHERE match_id = %s
        """, (end_timestamp, ui['current_match_id']))
        
        conn.commit()
        cursor.close()
        
        # Log to event log
        ui['event_log'].append({
            'event_id': None,
            'timestamp': current_time,
            'description': f"🏁 MATCH ENDED"
        })
        update_event_log_display(ui)
        
        print(f"✓ Match ended at {current_time}")
        print(f"→ Match clock stopped. No more events can be recorded.")
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error ending match: {e}")
    finally:
        conn.close()
    
def handle_delete_last_click(ui):
    """Handle delete last event button click"""
    if not ui.get('event_log') or len(ui['event_log']) == 0:
        print("No events to delete")
        return
    
    # Get last event
    last_event = ui['event_log'].pop()
    
    # Delete from database
    success = db.delete_last_event(last_event['event_id'])
    
    if success:
        print(f"✓ Deleted: {last_event['description']}")
        # Update display
        update_event_log_display(ui)
    else:
        print(f"✗ Failed to delete event")
        # Re-add if deletion failed
        ui['event_log'].append(last_event)

    # Check if kickoff has been recorded
    if not ui.get('kickoff_recorded'):
        print("✗ Cannot record events - kickoff has not been recorded yet")
        return
    
# ===================================================
# ============== Page 2 =============================
# ===================================================

def handle_player_change(ui):
    """Handle main player dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    player_id = ui['page_2']['player_dropdown'].currentData()
    
    if player_id is None:
        return
    
    conn = db.get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE event 
            SET player_id = %s
            WHERE event_id = %s
        """, (player_id, event_id))
        conn.commit()
        cursor.close()
        
        print(f"✓ Event player updated: {player_id}")
    except Exception as e:
        print(f"✗ Error updating player: {e}")
    finally:
        conn.close()


def handle_foul_guilty_change(ui):
    """Handle foul guilty player dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    guilty_id = ui['page_2']['foul_guilty_dropdown'].currentData()
    
    conn = db.get_connection()
    try:
        event = db.get_event_details(conn, event_id)
        innocent_id = event.get('foul_innocent_id')
        
        db.update_foul_players(conn, event_id, guilty_id, innocent_id)
        print(f"✓ Foul guilty player updated")
    except Exception as e:
        print(f"✗ Error updating foul guilty player: {e}")
    finally:
        conn.close()


def handle_foul_innocent_change(ui):
    """Handle foul innocent player dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    innocent_id = ui['page_2']['foul_innocent_dropdown'].currentData()
    
    conn = db.get_connection()
    try:
        event = db.get_event_details(conn, event_id)
        guilty_id = event.get('foul_guilty_id')
        
        db.update_foul_players(conn, event_id, guilty_id, innocent_id)
        print(f"✓ Foul innocent player updated")
    except Exception as e:
        print(f"✗ Error updating foul innocent player: {e}")
    finally:
        conn.close()

def handle_from_open_play_click(ui, value):
    """Handle from_open_play button clicks"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        db.update_ball_played_from_open_play(conn, event_id, value)
        
        # Update button colors
        if value:
            ui['page_2']['from_open_play_yes_button'].idle_color = (165, 214, 167, 1)
            ui['page_2']['from_open_play_no_button'].idle_color = (245, 245, 245, 1)
        else:
            ui['page_2']['from_open_play_yes_button'].idle_color = (245, 245, 245, 1)
            ui['page_2']['from_open_play_no_button'].idle_color = (224, 224, 224, 1)
        
        print(f"✓ From open play updated: {value}")
        
    except Exception as e:
        print(f"✗ Error updating from_open_play: {e}")
    finally:
        conn.close()

def handle_cross_technique_click(ui, technique):
    """Handle cross technique button clicks"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        # Get current cross details
        event = db.get_event_details(conn, event_id)
        intention = event.get('intention')
        
        # Update technique
        db.update_cross_details(conn, event_id, intention, technique)
        
        # Update button colors
        ui['page_2']['technique_inswing_button'].idle_color = (165, 214, 167, 1) if technique == 'inswing' else (245, 245, 245, 1)
        ui['page_2']['technique_outswing_button'].idle_color = (165, 214, 167, 1) if technique == 'outswing' else (245, 245, 245, 1)
        ui['page_2']['technique_other_button'].idle_color = (165, 214, 167, 1) if technique == 'other' else (245, 245, 245, 1)
        
        print(f"✓ Cross technique updated: {technique}")
        
    except Exception as e:
        print(f"✗ Error updating cross technique: {e}")
    finally:
        conn.close()

def show_ball_played_fields(ui, event):
    """Show ball_played specific fields and populate with data"""
    ui['page_2']['from_open_play_label'].is_visible = True
    ui['page_2']['from_open_play_yes_button'].is_visible = True
    ui['page_2']['from_open_play_no_button'].is_visible = True
    
    # Highlight based on current value
    from_open_play = event.get('from_open_play')

    # Default to True if NULL (backward compatibility)
    if from_open_play is None:
        from_open_play = True

    if from_open_play == 1 or from_open_play is True:
        ui['page_2']['from_open_play_yes_button'].idle_color = (165, 214, 167, 1)
        ui['page_2']['from_open_play_no_button'].idle_color = (245, 245, 245, 1)
    elif from_open_play == 0 or from_open_play is False:
        ui['page_2']['from_open_play_yes_button'].idle_color = (245, 245, 245, 1)
        ui['page_2']['from_open_play_no_button'].idle_color = (224, 224, 224, 1)
    else:  # NULL or unknown
        ui['page_2']['from_open_play_yes_button'].idle_color = (245, 245, 245, 1)
        ui['page_2']['from_open_play_no_button'].idle_color = (245, 245, 245, 1)


def hide_all_detail_fields(ui):
    """Hide all event-type-specific detail fields"""
    
    # Shot fields
    ui['page_2']['shot_execution_label'].is_visible = False
    ui['page_2']['exec_left_button'].is_visible = False
    ui['page_2']['exec_right_button'].is_visible = False
    ui['page_2']['exec_header_button'].is_visible = False
    ui['page_2']['exec_other_button'].is_visible = False
    ui['page_2']['shot_result_label'].is_visible = False 
    ui['page_2']['shot_result_dropdown'].hide()  
    
    # Pass fields
    ui['page_2']['pass_assist_label'].is_visible = False
    ui['page_2']['assist_yes_button'].is_visible = False
    ui['page_2']['assist_no_button'].is_visible = False
    ui['page_2']['line_split_label'].is_visible = False
    ui['page_2']['line_split_yes_button'].is_visible = False
    ui['page_2']['line_split_no_button'].is_visible = False
    ui['page_2']['pass_type_label'].is_visible = False  
    ui['page_2']['pass_length_dropdown'].hide()  
    ui['page_2']['pass_height_dropdown'].hide()  
    
    # Cross fields
    ui['page_2']['cross_intention_label'].is_visible = False
    ui['page_2']['intention_near_button'].is_visible = False
    ui['page_2']['intention_back_button'].is_visible = False
    ui['page_2']['intention_central_button'].is_visible = False
    ui['page_2']['intention_other_button'].is_visible = False
    ui['page_2']['cross_technique_label'].is_visible = False
    ui['page_2']['technique_inswing_button'].is_visible = False
    ui['page_2']['technique_outswing_button'].is_visible = False
    ui['page_2']['technique_other_button'].is_visible = False
    
    # Goal fields
    ui['page_2']['goal_zone_label'].is_visible = False
    ui['page_2']['goal_zone_dropdown'].hide()
    
    # Ball Played fields
    ui['page_2']['from_open_play_label'].is_visible = False
    ui['page_2']['from_open_play_yes_button'].is_visible = False
    ui['page_2']['from_open_play_no_button'].is_visible = False

    # Foul fields
    ui['page_2']['foul_reason_label'].is_visible = False
    ui['page_2']['foul_reason_dropdown'].hide()
    ui['page_2']['foul_guilty_label'].is_visible = False  
    ui['page_2']['foul_guilty_dropdown'].hide()  
    ui['page_2']['foul_innocent_label'].is_visible = False  
    ui['page_2']['foul_innocent_dropdown'].hide()  

    # Card fields
    ui['page_2']['card_reason_label'].is_visible = False
    ui['page_2']['card_reason_dropdown'].hide()
    ui['page_2']['card_color_label'].is_visible = False  
    ui['page_2']['card_yellow_button'].is_visible = False  
    ui['page_2']['card_second_yellow_button'].is_visible = False  
    ui['page_2']['card_red_button'].is_visible = False  

    # Offside fields - NEW
    ui['page_2']['offside_player_label'].is_visible = False
    ui['page_2']['offside_player_dropdown'].hide()

    # Handball fields - NEW
    ui['page_2']['handball_player_label'].is_visible = False
    ui['page_2']['handball_player_dropdown'].hide()

    # Substitution fields - NEW
    ui['page_2']['sub_in_label'].is_visible = False
    ui['page_2']['sub_in_dropdown'].hide()
    ui['page_2']['sub_out_label'].is_visible = False
    ui['page_2']['sub_out_dropdown'].hide()

    # Set Piece fields 
    ui['page_2']['set_piece_type_label'].is_visible = False
    ui['page_2']['sp_corner_left_button'].is_visible = False
    ui['page_2']['sp_corner_right_button'].is_visible = False
    ui['page_2']['sp_throw_front_button'].is_visible = False
    ui['page_2']['sp_throw_rear_button'].is_visible = False
    ui['page_2']['sp_direct_kick_button'].is_visible = False
    ui['page_2']['sp_indirect_kick_button'].is_visible = False
    ui['page_2']['sp_penalty_kick_button'].is_visible = False
    ui['page_2']['sp_goal_kick_button'].is_visible = False

    # Common fields
    ui['page_2']['rating_none_button'].is_visible = False

    # Duel fields
    ui['page_2']['duel_context_label'].is_visible = False  
    ui['page_2']['duel_ground_button'].is_visible = False  
    ui['page_2']['duel_aerial_button'].is_visible = False  
    ui['page_2']['duel_winner_label'].is_visible = False
    ui['page_2']['duel_winner_dropdown'].hide()
    ui['page_2']['duel_loser_label'].is_visible = False
    ui['page_2']['duel_loser_dropdown'].hide()


def show_common_fields(ui):
    """Show fields common to all events"""
    ui['page_2']['location_label'].is_visible = True
    ui['page_2']['location_display'].is_visible = True
    ui['page_2']['set_location_button'].is_visible = True
    ui['page_2']['rating_label'].is_visible = True
    ui['page_2']['rating_s_button'].is_visible = True
    ui['page_2']['rating_f_button'].is_visible = True
    ui['page_2']['rating_none_button'].is_visible = True

def show_foul_fields(ui, event):
    """Show foul-specific fields and populate with data"""
    ui['page_2']['foul_reason_label'].is_visible = True
    ui['page_2']['foul_reason_dropdown'].show()
    ui['page_2']['foul_guilty_label'].is_visible = True
    ui['page_2']['foul_guilty_dropdown'].show()
    ui['page_2']['foul_innocent_label'].is_visible = True
    ui['page_2']['foul_innocent_dropdown'].show()
    
    # Set reason
    reason_mapping = {
        'foul': 'Foul',
        'unfairness': 'Unfairness',
        'other': 'Other'
    }
    
    foul_reason = event.get('foul_reason')
    if foul_reason and foul_reason in reason_mapping:
        display_text = reason_mapping[foul_reason]
        index = ui['page_2']['foul_reason_dropdown'].findText(display_text)
        if index >= 0:
            ui['page_2']['foul_reason_dropdown'].setCurrentIndex(index)
    else:
        ui['page_2']['foul_reason_dropdown'].setCurrentIndex(0)
    
    # Populate guilty/innocent dropdowns
    guilty_id = event.get('foul_guilty_id')
    innocent_id = event.get('foul_innocent_id')
    
    populate_player_dropdown(ui, ui['page_2']['foul_guilty_dropdown'], guilty_id)
    populate_player_dropdown(ui, ui['page_2']['foul_innocent_dropdown'], innocent_id)

def show_offside_fields(ui, event):
    """Show offside-specific fields and populate with data"""
    ui['page_2']['offside_player_label'].is_visible = True
    ui['page_2']['offside_player_dropdown'].show()
    
    # Get offside_player_id, but default to event player if not set
    offside_player_id = event.get('offside_player_id')
    
    # If offside_player_id is NULL, default to the event's player_id
    if not offside_player_id:
        offside_player_id = event.get('player_id')
    
    # Populate dropdown
    populate_player_dropdown(ui, ui['page_2']['offside_player_dropdown'], offside_player_id) 
    
    # Populate dropdown
    offside_player_id = event.get('offside_player_id')
    populate_player_dropdown(ui, ui['page_2']['offside_player_dropdown'], offside_player_id)


def show_handball_fields(ui, event):
    """Show handball-specific fields and populate with data"""
    ui['page_2']['handball_player_label'].is_visible = True
    ui['page_2']['handball_player_dropdown'].show()
    
    # Populate dropdown
    guilty_id = event.get('handball_guilty_id')
    populate_player_dropdown(ui, ui['page_2']['handball_player_dropdown'], guilty_id)


def show_substitution_fields(ui, event):
    """Show substitution-specific fields and populate with data"""
    ui['page_2']['sub_in_label'].is_visible = True
    ui['page_2']['sub_in_dropdown'].show()
    ui['page_2']['sub_out_label'].is_visible = True
    ui['page_2']['sub_out_dropdown'].show()
    
    # Populate dropdowns
    in_player_id = event.get('sub_in_player_id')
    out_player_id = event.get('sub_out_player_id')
    
    populate_player_dropdown(ui, ui['page_2']['sub_in_dropdown'], in_player_id)
    populate_player_dropdown(ui, ui['page_2']['sub_out_dropdown'], out_player_id)

def show_set_piece_fields(ui, event):
    """Show set piece-specific fields and populate with data"""
    ui['page_2']['set_piece_type_label'].is_visible = True
    ui['page_2']['sp_corner_left_button'].is_visible = True
    ui['page_2']['sp_corner_right_button'].is_visible = True
    ui['page_2']['sp_throw_front_button'].is_visible = True
    ui['page_2']['sp_throw_rear_button'].is_visible = True
    ui['page_2']['sp_direct_kick_button'].is_visible = True
    ui['page_2']['sp_indirect_kick_button'].is_visible = True
    ui['page_2']['sp_penalty_kick_button'].is_visible = True
    ui['page_2']['sp_goal_kick_button'].is_visible = True
    
    # Highlight current type
    sp_type = event.get('set_piece_type')
    ui['page_2']['sp_corner_left_button'].idle_color = (165, 214, 167, 1) if sp_type == 'corner_left' else (245, 245, 245, 1)
    ui['page_2']['sp_corner_right_button'].idle_color = (165, 214, 167, 1) if sp_type == 'corner_right' else (245, 245, 245, 1)
    ui['page_2']['sp_throw_front_button'].idle_color = (165, 214, 167, 1) if sp_type == 'throw_in_front' else (245, 245, 245, 1)
    ui['page_2']['sp_throw_rear_button'].idle_color = (165, 214, 167, 1) if sp_type == 'throw_in_rear' else (245, 245, 245, 1)
    ui['page_2']['sp_direct_kick_button'].idle_color = (165, 214, 167, 1) if sp_type == 'direct_kick' else (245, 245, 245, 1)
    ui['page_2']['sp_indirect_kick_button'].idle_color = (165, 214, 167, 1) if sp_type == 'indirect_kick' else (245, 245, 245, 1)
    ui['page_2']['sp_penalty_kick_button'].idle_color = (165, 214, 167, 1) if sp_type == 'penalty_kick' else (245, 245, 245, 1)
    ui['page_2']['sp_goal_kick_button'].idle_color = (165, 214, 167, 1) if sp_type == 'goal_kick' else (245, 245, 245, 1)

def show_card_fields(ui, event):
    """Show card-specific fields and populate with data"""
    ui['page_2']['card_reason_label'].is_visible = True
    ui['page_2']['card_reason_dropdown'].show()
    ui['page_2']['card_color_label'].is_visible = True
    ui['page_2']['card_yellow_button'].is_visible = True
    ui['page_2']['card_second_yellow_button'].is_visible = True
    ui['page_2']['card_red_button'].is_visible = True
    
    # Map database values to dropdown display text
    reason_mapping = {
        'foul': 'Foul',
        'unfairness': 'Unfairness',
        'other': 'Other'
    }
    
    # Set dropdown to current value
    card_reason = event.get('card_reason')
    if card_reason and card_reason in reason_mapping:
        display_text = reason_mapping[card_reason]
        index = ui['page_2']['card_reason_dropdown'].findText(display_text)
        if index >= 0:
            ui['page_2']['card_reason_dropdown'].setCurrentIndex(index)
    else:
        ui['page_2']['card_reason_dropdown'].setCurrentIndex(0)  # "Not Set"

    # Highlight card color - NEW
    card_color = event.get('card_color')
    ui['page_2']['card_yellow_button'].idle_color = (255, 241, 118, 1) if card_color == 'yellow' else (245, 245, 245, 1)
    ui['page_2']['card_second_yellow_button'].idle_color = (255, 183, 77, 1) if card_color == 'second_yellow' else (245, 245, 245, 1)
    ui['page_2']['card_red_button'].idle_color = (255, 205, 210, 1) if card_color == 'red' else (245, 245, 245, 1)

def show_duel_fields(ui, event):
    """Show duel-specific fields and populate with data"""
    ui['page_2']['duel_context_label'].is_visible = True
    ui['page_2']['duel_ground_button'].is_visible = True
    ui['page_2']['duel_aerial_button'].is_visible = True
    ui['page_2']['duel_winner_label'].is_visible = True
    ui['page_2']['duel_winner_dropdown'].show()
    ui['page_2']['duel_loser_label'].is_visible = True
    ui['page_2']['duel_loser_dropdown'].show()
    
    # Highlight context - NEW
    context = event.get('duel_context')
    ui['page_2']['duel_ground_button'].idle_color = (165, 214, 167, 1) if context == 'ground' else (245, 245, 245, 1)
    ui['page_2']['duel_aerial_button'].idle_color = (165, 214, 167, 1) if context == 'aerial' else (245, 245, 245, 1)
    
    # Clear and populate dropdowns with match players
    ui['page_2']['duel_winner_dropdown'].clear()
    ui['page_2']['duel_loser_dropdown'].clear()
    
    ui['page_2']['duel_winner_dropdown'].addItem("Not Set", None)
    ui['page_2']['duel_loser_dropdown'].addItem("Not Set", None)
    
    # Get all players in the match
    conn = db.get_connection()
    try:
        players = db.get_match_players(conn, ui['current_match_id'])
        
        for player in players:
            display_text = f"[{player['team_name']}] #{player['jersey_num']} {player['player_name']}"
            
            # Add to both dropdowns with player_id as data
            ui['page_2']['duel_winner_dropdown'].addItem(display_text, player['player_id'])
            ui['page_2']['duel_loser_dropdown'].addItem(display_text, player['player_id'])
        
        # Set current values if they exist
        winner_id = event.get('duel_winner_id')
        loser_id = event.get('duel_loser_id')
        
        if winner_id:
            for i in range(ui['page_2']['duel_winner_dropdown'].count()):
                if ui['page_2']['duel_winner_dropdown'].itemData(i) == winner_id:
                    ui['page_2']['duel_winner_dropdown'].setCurrentIndex(i)
                    break
        
        if loser_id:
            for i in range(ui['page_2']['duel_loser_dropdown'].count()):
                if ui['page_2']['duel_loser_dropdown'].itemData(i) == loser_id:
                    ui['page_2']['duel_loser_dropdown'].setCurrentIndex(i)
                    break
                    
    finally:
        conn.close()

def handle_duel_context_click(ui, context):
    """Handle duel context button clicks"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        db.update_duel_context(conn, event_id, context)
        
        # Update button colors
        ui['page_2']['duel_ground_button'].idle_color = (165, 214, 167, 1) if context == 'ground' else (245, 245, 245, 1)
        ui['page_2']['duel_aerial_button'].idle_color = (165, 214, 167, 1) if context == 'aerial' else (245, 245, 245, 1)
        
        print(f"✓ Duel context updated: {context}")
        
    except Exception as e:
        print(f"✗ Error updating duel context: {e}")
    finally:
        conn.close()

def handle_card_color_click(ui, color):
    """Handle card color button clicks"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        db.update_card_color(conn, event_id, color)
        
        # Update button colors
        ui['page_2']['card_yellow_button'].idle_color = (255, 241, 118, 1) if color == 'yellow' else (245, 245, 245, 1)
        ui['page_2']['card_second_yellow_button'].idle_color = (255, 183, 77, 1) if color == 'second_yellow' else (245, 245, 245, 1)
        ui['page_2']['card_red_button'].idle_color = (255, 205, 210, 1) if color == 'red' else (245, 245, 245, 1)
        
        print(f"✓ Card color updated: {color}")
        
    except Exception as e:
        print(f"✗ Error updating card color: {e}")
    finally:
        conn.close()

def handle_card_reason_change(ui):
    """Handle card reason dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    selected_text = ui['page_2']['card_reason_dropdown'].currentText()
    
    # Map display text back to database values
    reason_reverse_mapping = {
        'Foul': 'foul',
        'Unfairness': 'unfairness',
        'Other': 'other',
        'Not Set': None
    }
    
    card_reason = reason_reverse_mapping.get(selected_text)
    
    conn = db.get_connection()
    try:
        db.update_card_reason(conn, event_id, card_reason)
        print(f"✓ Card reason updated: {card_reason if card_reason else 'Not Set'}")
    except Exception as e:
        print(f"✗ Error updating card reason: {e}")
    finally:
        conn.close()

def handle_event_selected(ui, event_id):
    """Handle when an event is selected from the list"""
    
    # Get event details from database
    conn = db.get_connection()
    try:
        event = db.get_event_details(conn, event_id)
        
        if not event:
            print(f"✗ Event {event_id} not found")
            return
        
        # Store current event
        ui['current_review_event_id'] = event_id
        ui['current_review_event'] = event
        
        # Update header
        ui['page_2']['event_header'].text = f"Event #{event_id}: {event['event_type']}"
        
        # Update info
        info_text = f"Player: #{event['jersey_num']} {event['player_name']} ({event['team_name']})\n"
        info_text += f"Time: {event['time']}"
        ui['page_2']['event_info'].text = info_text
        
        # Hide all type-specific fields first
        hide_all_detail_fields(ui)
        
        # Show common fields
        show_common_fields(ui)

        # Determine if event needs player dropdown
        event_type = event['event_type']

        # Events that have their own player dropdowns (don't need event player)
        events_with_own_players = ['Foul', 'Duel', 'Offside', 'Handball', 'Substitution']

        needs_event_player = True
        for evt in events_with_own_players:
            if event_type.startswith(evt):
                needs_event_player = False
                break
        
        # Show event player dropdown if needed
        if needs_event_player:
            show_event_player_dropdown(ui, event)
        else:
            hide_event_player_dropdown(ui)
        
        # Update location display
        if event['location_x'] is not None:
            ui['page_2']['location_display'].text = f"x={event['location_x']}, y={event['location_y']}"
        else:
            ui['page_2']['location_display'].text = "Not set"
        
        # Update rating buttons
        if event['rating'] == 'S':
            ui['page_2']['rating_s_button'].idle_color = (165, 214, 167, 1)
            ui['page_2']['rating_f_button'].idle_color = (245, 245, 245, 1)
            ui['page_2']['rating_none_button'].idle_color = (245, 245, 245, 1)
        elif event['rating'] == 'F':
            ui['page_2']['rating_s_button'].idle_color = (245, 245, 245, 1)
            ui['page_2']['rating_f_button'].idle_color = (255, 205, 210, 1)
            ui['page_2']['rating_none_button'].idle_color = (245, 245, 245, 1)
        else:  # NULL rating
            ui['page_2']['rating_s_button'].idle_color = (245, 245, 245, 1)
            ui['page_2']['rating_f_button'].idle_color = (245, 245, 245, 1)
            ui['page_2']['rating_none_button'].idle_color = (224, 224, 224, 1)  # Highlight No Rating
        
        # Show type-specific fields based on event type
        if event['event_type'] == 'Shot':
            show_shot_fields(ui, event)
            show_ball_played_fields(ui, event)
        elif event['event_type'] == 'Pass':
            show_pass_fields(ui, event)
            show_ball_played_fields(ui, event)
        elif event['event_type'] == 'Cross':
            show_cross_fields(ui, event)
            show_ball_played_fields(ui, event)
        elif event['event_type'] == 'Goal':
            show_goal_fields(ui, event)
        elif event['event_type'] == 'Ball Received':
            # Only show common fields (location, rating)
            # No type-specific fields needed
            pass
        elif event['event_type'] == 'Ball Played':
            show_ball_played_fields(ui, event)
            pass
        elif event['event_type'] == 'Foul':  
            show_foul_fields(ui, event)
        elif event['event_type'].startswith('Card'): 
            show_card_fields(ui, event)
        elif event['event_type'].startswith('Duel'):  
            show_duel_fields(ui, event)
        elif event['event_type'].startswith('Set Piece'):  
            show_set_piece_fields(ui, event)
        elif event['event_type'] == 'Offside': 
            show_offside_fields(ui, event)
        elif event['event_type'] == 'Handball': 
            show_handball_fields(ui, event)
        elif event['event_type'] == 'Substitution':  
            show_substitution_fields(ui, event)
            
        
    finally:
        conn.close()

def handle_event_player_change(ui):
    """Handle event player dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    player_id = ui['page_2']['event_player_dropdown'].currentData()
    
    if player_id is None:
        return
    
    conn = db.get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE event 
            SET player_id = %s
            WHERE event_id = %s
        """, (player_id, event_id))
        conn.commit()
        cursor.close()
        
        print(f"✓ Event player updated: {player_id}")
    except Exception as e:
        print(f"✗ Error updating event player: {e}")
    finally:
        conn.close()

def handle_set_piece_type_click(ui, sp_type):
    """Handle set piece type button clicks"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        db.update_set_piece_type(conn, event_id, sp_type)
        
        # Update button colors
        ui['page_2']['sp_corner_left_button'].idle_color = (165, 214, 167, 1) if sp_type == 'corner_left' else (245, 245, 245, 1)
        ui['page_2']['sp_corner_right_button'].idle_color = (165, 214, 167, 1) if sp_type == 'corner_right' else (245, 245, 245, 1)
        ui['page_2']['sp_throw_front_button'].idle_color = (165, 214, 167, 1) if sp_type == 'throw_in_front' else (245, 245, 245, 1)
        ui['page_2']['sp_throw_rear_button'].idle_color = (165, 214, 167, 1) if sp_type == 'throw_in_rear' else (245, 245, 245, 1)
        ui['page_2']['sp_direct_kick_button'].idle_color = (165, 214, 167, 1) if sp_type == 'direct_kick' else (245, 245, 245, 1)
        ui['page_2']['sp_indirect_kick_button'].idle_color = (165, 214, 167, 1) if sp_type == 'indirect_kick' else (245, 245, 245, 1)
        ui['page_2']['sp_penalty_kick_button'].idle_color = (165, 214, 167, 1) if sp_type == 'penalty_kick' else (245, 245, 245, 1)
        ui['page_2']['sp_goal_kick_button'].idle_color = (165, 214, 167, 1) if sp_type == 'goal_kick' else (245, 245, 245, 1)
        
        print(f"✓ Set piece type updated: {sp_type}")
        
    except Exception as e:
        print(f"✗ Error updating set piece type: {e}")
    finally:
        conn.close()

def handle_offside_player_change(ui):
    """Handle offside player dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    offside_player_id = ui['page_2']['offside_player_dropdown'].currentData()
    
    conn = db.get_connection()
    try:
        db.update_offside_player(conn, event_id, offside_player_id)
        print(f"✓ Offside player updated")
    except Exception as e:
        print(f"✗ Error updating offside player: {e}")
    finally:
        conn.close()


def handle_handball_player_change(ui):
    """Handle handball guilty player dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    guilty_id = ui['page_2']['handball_player_dropdown'].currentData()
    
    conn = db.get_connection()
    try:
        db.update_handball_player(conn, event_id, guilty_id)
        print(f"✓ Handball guilty player updated")
    except Exception as e:
        print(f"✗ Error updating handball player: {e}")
    finally:
        conn.close()


def handle_sub_in_change(ui):
    """Handle substitution in player dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    in_player_id = ui['page_2']['sub_in_dropdown'].currentData()
    
    conn = db.get_connection()
    try:
        event = db.get_event_details(conn, event_id)
        out_player_id = event.get('sub_out_player_id')
        
        db.update_substitution_players(conn, event_id, in_player_id, out_player_id)
        print(f"✓ Substitution in player updated")
    except Exception as e:
        print(f"✗ Error updating sub in player: {e}")
    finally:
        conn.close()


def handle_sub_out_change(ui):
    """Handle substitution out player dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    out_player_id = ui['page_2']['sub_out_dropdown'].currentData()
    
    conn = db.get_connection()
    try:
        event = db.get_event_details(conn, event_id)
        in_player_id = event.get('sub_in_player_id')
        
        db.update_substitution_players(conn, event_id, in_player_id, out_player_id)
        print(f"✓ Substitution out player updated")
    except Exception as e:
        print(f"✗ Error updating sub out player: {e}")
    finally:
        conn.close()

def handle_pass_assist_click(ui, is_assist):
    """Handle pass assist button clicks"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        # Get current pass details
        event = db.get_event_details(conn, event_id)
        line_split = event.get('line_split', False)
        
        # Update assist
        db.update_pass_details(conn, event_id, is_assist, line_split)
        
        # Update button colors
        if is_assist:
            ui['page_2']['assist_yes_button'].idle_color = (165, 214, 167, 1)
            ui['page_2']['assist_no_button'].idle_color = (245, 245, 245, 1)
        else:
            ui['page_2']['assist_yes_button'].idle_color = (245, 245, 245, 1)
            ui['page_2']['assist_no_button'].idle_color = (224, 224, 224, 1)
        
        print(f"✓ Pass assist updated: {is_assist}")
        
    except Exception as e:
        print(f"✗ Error updating assist: {e}")
    finally:
        conn.close()


def handle_pass_line_split_click(ui, is_line_split):
    """Handle pass line split button clicks"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        # Get current pass details
        event = db.get_event_details(conn, event_id)
        assist = event.get('assist', False)
        
        # Update line_split
        db.update_pass_details(conn, event_id, assist, is_line_split)
        
        # Update button colors
        if is_line_split:
            ui['page_2']['line_split_yes_button'].idle_color = (165, 214, 167, 1)
            ui['page_2']['line_split_no_button'].idle_color = (245, 245, 245, 1)
        else:
            ui['page_2']['line_split_yes_button'].idle_color = (245, 245, 245, 1)
            ui['page_2']['line_split_no_button'].idle_color = (224, 224, 224, 1)
        
        print(f"✓ Pass line split updated: {is_line_split}")
        
    except Exception as e:
        print(f"✗ Error updating line split: {e}")
    finally:
        conn.close()

def handle_save_event(ui):
    """Save current event details"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    # For now, just confirmation
    # Individual fields (rating, location, etc.) are saved immediately when clicked
    print(f"✓ Event {ui['current_review_event_id']} details saved")


def handle_save_and_next(ui):
    """Save current event and move to next incomplete event"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    # Save current (already saved via individual field updates)
    handle_save_event(ui)
    
    # Find next incomplete event
    current_event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        # Get all incomplete events
        events = db.get_all_events(conn, ui['current_match_id'])
        incomplete_events = [e for e in events if e['incomplete'] == 1]
        
        # Find next incomplete after current
        next_event = None
        found_current = False
        
        for event in incomplete_events:
            if found_current:
                next_event = event
                break
            if event['event_id'] == current_event_id:
                found_current = True
        
        if next_event:
            # Select next event
            handle_event_selected(ui, next_event['event_id'])
            
            # Highlight in list
            for i in range(ui['page_2']['event_list'].count()):
                item = ui['page_2']['event_list'].item(i)
                if item.data(Qt.UserRole) == next_event['event_id']:
                    ui['page_2']['event_list'].setCurrentItem(item)
                    break
            
            print(f"→ Moved to next incomplete event: {next_event['event_id']}")
        else:
            print("✓ No more incomplete events!")
            
    except Exception as e:
        print(f"✗ Error finding next event: {e}")
    finally:
        conn.close()

def show_shot_fields(ui, event):
    """Show shot-specific fields and populate with data"""
    ui['page_2']['shot_execution_label'].is_visible = True
    ui['page_2']['exec_left_button'].is_visible = True
    ui['page_2']['exec_right_button'].is_visible = True
    ui['page_2']['exec_header_button'].is_visible = True
    ui['page_2']['exec_other_button'].is_visible = True
    ui['page_2']['shot_result_label'].is_visible = True  
    ui['page_2']['shot_result_dropdown'].show()  
    
    # Highlight selected execution
    exec_val = event.get('execution')
    ui['page_2']['exec_left_button'].idle_color = (165, 214, 167, 1) if exec_val == 'left' else (245, 245, 245, 1)
    ui['page_2']['exec_right_button'].idle_color = (165, 214, 167, 1) if exec_val == 'right' else (245, 245, 245, 1)
    ui['page_2']['exec_header_button'].idle_color = (165, 214, 167, 1) if exec_val == 'header' else (245, 245, 245, 1)
    ui['page_2']['exec_other_button'].idle_color = (165, 214, 167, 1) if exec_val == 'other' else (245, 245, 245, 1)

        # Set result dropdown - NEW
    result_mapping = {
        'over': 'Over',
        'wide_left': 'Wide Left',
        'wide_right': 'Wide Right',
        'post': 'Post',
        'crossbar': 'Crossbar',
        'saved': 'Saved',
        'blocked': 'Blocked',
        'goal': 'Goal'
    }
    
    result = event.get('result')
    if result and result in result_mapping:
        display_text = result_mapping[result]
        index = ui['page_2']['shot_result_dropdown'].findText(display_text)
        if index >= 0:
            ui['page_2']['shot_result_dropdown'].setCurrentIndex(index)
    else:
        ui['page_2']['shot_result_dropdown'].setCurrentIndex(0)  # "Not Set"


def show_pass_fields(ui, event):
    """Show pass-specific fields and populate with data"""
    ui['page_2']['pass_type_label'].is_visible = True
    ui['page_2']['pass_length_dropdown'].show()
    ui['page_2']['pass_height_dropdown'].show()
    ui['page_2']['pass_assist_label'].is_visible = True
    ui['page_2']['assist_yes_button'].is_visible = True
    ui['page_2']['assist_no_button'].is_visible = True
    ui['page_2']['line_split_label'].is_visible = True
    ui['page_2']['line_split_yes_button'].is_visible = True
    ui['page_2']['line_split_no_button'].is_visible = True
    
    # Set pass length dropdown
    pass_length = event.get('pass_length')
    if pass_length == 'short':
        ui['page_2']['pass_length_dropdown'].setCurrentIndex(0)
    elif pass_length == 'medium':
        ui['page_2']['pass_length_dropdown'].setCurrentIndex(1)
    elif pass_length == 'long':
        ui['page_2']['pass_length_dropdown'].setCurrentIndex(2)
    
    # Set pass height dropdown
    pass_height = event.get('pass_height')
    if pass_height == 'low':
        ui['page_2']['pass_height_dropdown'].setCurrentIndex(0)
    elif pass_height == 'high':
        ui['page_2']['pass_height_dropdown'].setCurrentIndex(1)
    
    # Highlight assist
    if event.get('assist'):
        ui['page_2']['assist_yes_button'].idle_color = (165, 214, 167, 1)
        ui['page_2']['assist_no_button'].idle_color = (245, 245, 245, 1)
    else:
        ui['page_2']['assist_yes_button'].idle_color = (245, 245, 245, 1)
        ui['page_2']['assist_no_button'].idle_color = (224, 224, 224, 1)
    
    # Highlight line split
    if event.get('line_split'):
        ui['page_2']['line_split_yes_button'].idle_color = (165, 214, 167, 1)
        ui['page_2']['line_split_no_button'].idle_color = (245, 245, 245, 1)
    else:
        ui['page_2']['line_split_yes_button'].idle_color = (245, 245, 245, 1)
        ui['page_2']['line_split_no_button'].idle_color = (224, 224, 224, 1)


def show_cross_fields(ui, event):
    """Show cross-specific fields and populate with data"""
    ui['page_2']['cross_intention_label'].is_visible = True
    ui['page_2']['intention_near_button'].is_visible = True
    ui['page_2']['intention_back_button'].is_visible = True
    ui['page_2']['intention_central_button'].is_visible = True
    ui['page_2']['cross_technique_label'].is_visible = True
    ui['page_2']['technique_inswing_button'].is_visible = True
    ui['page_2']['technique_outswing_button'].is_visible = True
    ui['page_2']['technique_other_button'].is_visible = True
    ui['page_2']['intention_other_button'].is_visible = True
    
    # Highlight intention
    intent = event.get('intention')
    ui['page_2']['intention_near_button'].idle_color = (165, 214, 167, 1) if intent == 'near_post' else (245, 245, 245, 1)
    ui['page_2']['intention_back_button'].idle_color = (165, 214, 167, 1) if intent == 'back_post' else (245, 245, 245, 1)
    ui['page_2']['intention_central_button'].idle_color = (165, 214, 167, 1) if intent == 'central' else (245, 245, 245, 1)
    ui['page_2']['intention_other_button'].idle_color = (165, 214, 167, 1) if intent == 'other' else (245, 245, 245, 1)
    
    # Highlight technique
    tech = event.get('technique')
    ui['page_2']['technique_inswing_button'].idle_color = (165, 214, 167, 1) if tech == 'inswing' else (245, 245, 245, 1)
    ui['page_2']['technique_outswing_button'].idle_color = (165, 214, 167, 1) if tech == 'outswing' else (245, 245, 245, 1)
    ui['page_2']['technique_other_button'].idle_color = (165, 214, 167, 1) if tech == 'other' else (245, 245, 245, 1)


def show_goal_fields(ui, event):
    """Show goal-specific fields and populate with data"""
    ui['page_2']['goal_zone_label'].is_visible = True
    ui['page_2']['goal_zone_dropdown'].show()
    
    # Map database values to dropdown display text
    zone_mapping = {
        'low_right_90': 'Low Right 90',
        'upper_right_90': 'Upper Right 90',
        'lower_left_90': 'Lower Left 90',
        'upper_left_90': 'Upper Left 90',
        'central': 'Central',
        'left': 'Left',
        'right': 'Right'
    }
    
    # Set dropdown to current value
    goal_zone = event.get('goal_zone')
    if goal_zone and goal_zone in zone_mapping:
        display_text = zone_mapping[goal_zone]
        index = ui['page_2']['goal_zone_dropdown'].findText(display_text)
        if index >= 0:
            ui['page_2']['goal_zone_dropdown'].setCurrentIndex(index)
    else:
        ui['page_2']['goal_zone_dropdown'].setCurrentIndex(0)  # "Not Set"

def handle_shot_result_change(ui):
    """Handle shot result dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    selected_text = ui['page_2']['shot_result_dropdown'].currentText()
    
    # Map display text back to database values
    result_reverse_mapping = {
        'Over': 'over',
        'Wide Left': 'wide_left',
        'Wide Right': 'wide_right',
        'Post': 'post',
        'Crossbar': 'crossbar',
        'Saved': 'saved',
        'Blocked': 'blocked',
        'Goal': 'goal',
        'Not Set': None
    }
    
    shot_result = result_reverse_mapping.get(selected_text)
    
    conn = db.get_connection()
    try:
        db.update_shot_result(conn, event_id, shot_result)
        print(f"✓ Shot result updated: {shot_result if shot_result else 'Not Set'}")
    except Exception as e:
        print(f"✗ Error updating shot result: {e}")
    finally:
        conn.close()

def handle_goal_zone_change(ui):
    """Handle goal zone dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    selected_text = ui['page_2']['goal_zone_dropdown'].currentText()
    
    # Map display text back to database values
    zone_reverse_mapping = {
        'Low Right 90': 'low_right_90',
        'Upper Right 90': 'upper_right_90',
        'Lower Left 90': 'lower_left_90',
        'Upper Left 90': 'upper_left_90',
        'Central': 'central',
        'Left': 'left',
        'Right': 'right',
        'Not Set': None
    }
    
    goal_zone = zone_reverse_mapping.get(selected_text)
    
    conn = db.get_connection()
    try:
        db.update_goal_zone(conn, event_id, goal_zone)
        print(f"✓ Goal zone updated: {goal_zone if goal_zone else 'Not Set'}")
    except Exception as e:
        print(f"✗ Error updating goal zone: {e}")
    finally:
        conn.close()



def load_event_list(ui, match_id, filter_type='actions_only'):
    """Load events into the list widget"""
    
    conn = db.get_connection()
    try:
        events = db.get_all_events(conn, match_id)
        
        # Clear existing items
        ui['page_2']['event_list'].clear()
        
        # Filter events
        if filter_type == 'shots':
            events = [e for e in events if e['event_type'] == 'Shot']
        elif filter_type == 'passes':
            events = [e for e in events if e['event_type'].startswith('Pass')]
        elif filter_type == 'incomplete':
            events = [e for e in events if e['incomplete'] == 1]
        elif filter_type == 'actions_only':  
            events = [e for e in events if e['event_type'] not in ['Ball Received', 'Ball Played']]
        # 'all' shows everything including Ball Received/Played
        
        # Add items to list
        from PySide6.QtWidgets import QListWidgetItem
        for event in events:
            time_str = event['time'].strftime('%M:%S') if event['time'] else '00:00'
            incomplete_marker = ' ⚠' if event['incomplete'] else ''
            
            item_text = f"{time_str} #{event['jersey_num']} {event['player_name']} - {event['event_type']}{incomplete_marker}"
            
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, event['event_id'])  # Store event_id in item
            ui['page_2']['event_list'].addItem(item)
        
        # Update match info
        ui['page_2']['match_info'].text = f"Match {match_id}: {len(events)} events"
        
    finally:
        conn.close()

def handle_shot_execution_click(ui, execution):
    """Handle shot execution button clicks"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        db.update_shot_execution(conn, event_id, execution)
        
        # Update button colors
        ui['page_2']['exec_left_button'].idle_color = (165, 214, 167, 1) if execution == 'left' else (245, 245, 245, 1)
        ui['page_2']['exec_right_button'].idle_color = (165, 214, 167, 1) if execution == 'right' else (245, 245, 245, 1)
        ui['page_2']['exec_header_button'].idle_color = (165, 214, 167, 1) if execution == 'header' else (245, 245, 245, 1)
        ui['page_2']['exec_other_button'].idle_color = (165, 214, 167, 1) if execution == 'other' else (245, 245, 245, 1)
        
        print(f"✓ Shot execution updated: {execution}")
        
    except Exception as e:
        print(f"✗ Error updating execution: {e}")
    finally:
        conn.close()

def initialize_page_2(ui):
    """Initialize page 2 when switching to it"""
    # Load events for current match
    if ui.get('current_match_id'):
        load_event_list(ui, ui['current_match_id'], 'actions_only')
        
        # Only bind event list selection once
        if not ui.get('page_2_initialized'):
            # Bind event list selection
            def on_event_list_click(item):
                event_id = item.data(Qt.UserRole)
                handle_event_selected(ui, event_id)
            
            ui['page_2']['event_list'].itemClicked.connect(on_event_list_click)
            
            # Bind rating buttons
            ui['page_2']['rating_s_button'].on_click = lambda _: handle_rating_click(ui, 'S')
            ui['page_2']['rating_f_button'].on_click = lambda _: handle_rating_click(ui, 'F')
            ui['page_2']['rating_none_button'].on_click = lambda _: handle_rating_click(ui, None)
            
            # Bind filter buttons
            ui['page_2']['filter_all_button'].on_click = lambda _: load_event_list(ui, ui['current_match_id'], 'actions_only')  # Changed from 'all'
            ui['page_2']['filter_shots_button'].on_click = lambda _: load_event_list(ui, ui['current_match_id'], 'shots')
            ui['page_2']['filter_passes_button'].on_click = lambda _: load_event_list(ui, ui['current_match_id'], 'passes')
            ui['page_2']['filter_incomplete_button'].on_click = lambda _: load_event_list(ui, ui['current_match_id'], 'incomplete')
            ui['page_2']['filter_ball_flow_button'].on_click = lambda _: load_event_list(ui, ui['current_match_id'], 'all')  # NEW - shows everything
            
            # Bind navigation buttons
            ui['page_2']['save_button'].on_click = lambda _: handle_save_event(ui)
            ui['page_2']['save_next_button'].on_click = lambda _: handle_save_and_next(ui)

            # From open play buttons
            ui['page_2']['from_open_play_yes_button'].on_click = lambda _: handle_from_open_play_click(ui, True)
            ui['page_2']['from_open_play_no_button'].on_click = lambda _: handle_from_open_play_click(ui, False)
            
            # Mark as initialized
            ui['page_2_initialized'] = True

            # Bind goal zone dropdown
            ui['page_2']['goal_zone_dropdown'].currentTextChanged.connect(lambda: handle_goal_zone_change(ui))

            # Bind cross technique buttons
            ui['page_2']['technique_inswing_button'].on_click = lambda _: handle_cross_technique_click(ui, 'inswing')
            ui['page_2']['technique_outswing_button'].on_click = lambda _: handle_cross_technique_click(ui, 'outswing')
            ui['page_2']['technique_other_button'].on_click = lambda _: handle_cross_technique_click(ui, 'other')

            # Bind cross intention buttons
            ui['page_2']['intention_near_button'].on_click = lambda _: handle_cross_intention_click(ui, 'near_post')
            ui['page_2']['intention_back_button'].on_click = lambda _: handle_cross_intention_click(ui, 'back_post')
            ui['page_2']['intention_central_button'].on_click = lambda _: handle_cross_intention_click(ui, 'central')
            ui['page_2']['intention_other_button'].on_click = lambda _: handle_cross_intention_click(ui, 'other')  

            # Bind foul player dropdowns
            ui['page_2']['foul_guilty_dropdown'].currentIndexChanged.connect(lambda: handle_foul_guilty_change(ui))
            ui['page_2']['foul_innocent_dropdown'].currentIndexChanged.connect(lambda: handle_foul_innocent_change(ui))

            # Bind foul reason
            ui['page_2']['foul_reason_dropdown'].currentTextChanged.connect(lambda: handle_foul_reason_change(ui))

            # Bind card reason
            ui['page_2']['card_reason_dropdown'].currentTextChanged.connect(lambda: handle_card_reason_change(ui))

            # Bind pass type dropdowns
            ui['page_2']['pass_length_dropdown'].currentIndexChanged.connect(lambda: handle_pass_type_change(ui))
            ui['page_2']['pass_height_dropdown'].currentIndexChanged.connect(lambda: handle_pass_type_change(ui))
            
            # Bind pass assist/line split buttons
            ui['page_2']['assist_yes_button'].on_click = lambda _: handle_pass_assist_click(ui, True)
            ui['page_2']['assist_no_button'].on_click = lambda _: handle_pass_assist_click(ui, False)
            ui['page_2']['line_split_yes_button'].on_click = lambda _: handle_pass_line_split_click(ui, True)
            ui['page_2']['line_split_no_button'].on_click = lambda _: handle_pass_line_split_click(ui, False)

            # Bind shot result dropdown
            ui['page_2']['shot_result_dropdown'].currentTextChanged.connect(lambda: handle_shot_result_change(ui))

            # Bind shot execution buttons
            ui['page_2']['exec_left_button'].on_click = lambda _: handle_shot_execution_click(ui, 'left')
            ui['page_2']['exec_right_button'].on_click = lambda _: handle_shot_execution_click(ui, 'right')
            ui['page_2']['exec_header_button'].on_click = lambda _: handle_shot_execution_click(ui, 'header')
            ui['page_2']['exec_other_button'].on_click = lambda _: handle_shot_execution_click(ui, 'other')

            # Bind card color buttons
            ui['page_2']['card_yellow_button'].on_click = lambda _: handle_card_color_click(ui, 'yellow')
            ui['page_2']['card_second_yellow_button'].on_click = lambda _: handle_card_color_click(ui, 'second_yellow')
            ui['page_2']['card_red_button'].on_click = lambda _: handle_card_color_click(ui, 'red')

            # Bind duel context buttons
            ui['page_2']['duel_ground_button'].on_click = lambda _: handle_duel_context_click(ui, 'ground')
            ui['page_2']['duel_aerial_button'].on_click = lambda _: handle_duel_context_click(ui, 'aerial')

            # Bind duel dropdowns
            ui['page_2']['duel_winner_dropdown'].currentIndexChanged.connect(lambda: handle_duel_winner_change(ui))
            ui['page_2']['duel_loser_dropdown'].currentIndexChanged.connect(lambda: handle_duel_loser_change(ui))

            # Bind set piece type buttons
            ui['page_2']['sp_corner_left_button'].on_click = lambda _: handle_set_piece_type_click(ui, 'corner_left')
            ui['page_2']['sp_corner_right_button'].on_click = lambda _: handle_set_piece_type_click(ui, 'corner_right')
            ui['page_2']['sp_throw_front_button'].on_click = lambda _: handle_set_piece_type_click(ui, 'throw_in_front')
            ui['page_2']['sp_throw_rear_button'].on_click = lambda _: handle_set_piece_type_click(ui, 'throw_in_rear')
            ui['page_2']['sp_direct_kick_button'].on_click = lambda _: handle_set_piece_type_click(ui, 'direct_kick')
            ui['page_2']['sp_indirect_kick_button'].on_click = lambda _: handle_set_piece_type_click(ui, 'indirect_kick')
            ui['page_2']['sp_penalty_kick_button'].on_click = lambda _: handle_set_piece_type_click(ui, 'penalty_kick')
            ui['page_2']['sp_goal_kick_button'].on_click = lambda _: handle_set_piece_type_click(ui, 'goal_kick')

            # Bind offside dropdown
            ui['page_2']['offside_player_dropdown'].currentIndexChanged.connect(lambda: handle_offside_player_change(ui))

            # Bind handball dropdown
            ui['page_2']['handball_player_dropdown'].currentIndexChanged.connect(lambda: handle_handball_player_change(ui))

            # Bind substitution dropdowns
            ui['page_2']['sub_in_dropdown'].currentIndexChanged.connect(lambda: handle_sub_in_change(ui))
            ui['page_2']['sub_out_dropdown'].currentIndexChanged.connect(lambda: handle_sub_out_change(ui))

            # Bind event player dropdown
            ui['page_2']['event_player_dropdown'].currentIndexChanged.connect(lambda: handle_event_player_change(ui))

            # Bind set location button
            ui['page_2']['set_location_button'].on_click = lambda _: handle_set_location_click(ui)

             # Bind nav buttons
            ui['page_2']['prev_incomplete_button'].on_click = lambda _: handle_prev_incomplete_click(ui)
            ui['page_2']['next_incomplete_button'].on_click = lambda _: handle_next_incomplete_click(ui)
            
            # Bind save and next button
            ui['page_2']['save_next_button'].on_click = lambda _: handle_save_and_next_click(ui)

            # Bind export button
            ui['page_2']['export_csv_button'].on_click = lambda _: handle_export_csv_click(ui)

    else:
        ui['page_2']['match_info'].text = "No match loaded"

def handle_set_location_click(ui):
    """Handle Set Location button click - opens field popup"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    event_id = ui['current_review_event_id']
    
    # Get event details
    conn = db.get_connection()
    try:
        # Get event info including team
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT e.event_id, e.time, e.location_x, e.location_y, e.team_id
            FROM event e
            WHERE e.event_id = %s
        """, (event_id,))
        event = cursor.fetchone()
        cursor.close()
        
        if not event:
            print("✗ Event not found")
            return
        
        # Get current location if set
        current_x = event.get('location_x')
        current_y = event.get('location_y')
        event_team_id = event.get('team_id')
        
        # Determine which team is on which side
        # Convert event time to seconds
        if event['time']:
            time_obj = event['time']
            if hasattr(time_obj, 'hour'):
                # It's a datetime/time object
                time_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
            else:
                # It's already seconds or unknown format
                time_seconds = 0
        else:
            time_seconds = 0
        
        # Get team on left at this timestamp
        left_team_id = db.get_team_on_left(conn, ui['current_match_id'], time_seconds)
        
        # Get match teams
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT home_id, away_id 
            FROM match_metadata 
            WHERE match_id = %s
        """, (ui['current_match_id'],))
        match_info = cursor.fetchone()
        cursor.close()
        
        if not match_info:
            print("✗ Match not found")
            return
        
        home_team_id = match_info['home_id']
        away_team_id = match_info['away_id']
        
        # Get team names
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT team_id, team_name 
            FROM team 
            WHERE team_id IN (%s, %s)
        """, (home_team_id, away_team_id))
        teams = cursor.fetchall()
        cursor.close()
        
        # Create team name lookup
        team_names = {t['team_id']: t['team_name'] for t in teams}
        
        # Determine left and right team names based on left_team_id
        if left_team_id:
            left_team_name = team_names.get(left_team_id, "Left Team")
            right_team_id = away_team_id if left_team_id == home_team_id else home_team_id
            right_team_name = team_names.get(right_team_id, "Right Team")
        else:
            left_team_name = team_names.get(home_team_id, "Left Team")
            right_team_name = team_names.get(away_team_id, "Right Team")
        
        # Get path to field image
        field_image_path = os.path.join(os.path.dirname(__file__), 'assets', 'football-soccer-field-illustration.jpg')
        
        if not os.path.exists(field_image_path):
            print(f"✗ Field image not found at: {field_image_path}")
            return
        
        # Open popup
        popup = LocationPopup(
            field_image_path=field_image_path,
            current_x=current_x,
            current_y=current_y,
            left_team_name=left_team_name,
            right_team_name=right_team_name,
            parent=ui['window']
        )
        
        if popup.exec():  # User clicked Confirm
            x, y = popup.get_coordinates()
            
            if x is not None and y is not None:
                # Update database
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE event
                    SET location_x = %s, location_y = %s
                    WHERE event_id = %s
                """, (x, y, event_id))
                conn.commit()
                cursor.close()
                
                # Update display
                ui['page_2']['location_display'].text = f"X: {x:.1f}, Y: {y:.1f}"
                
                print(f"✓ Location updated: ({x:.1f}, {y:.1f})")
            else:
                print("✗ No location selected")
        else:
            print("Location selection cancelled")
            
    except Exception as e:
        print(f"✗ Error opening location popup: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()

def handle_prev_incomplete_click(ui):
    """Navigate to previous incomplete event"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    current_event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        # Get all incomplete events
        events = db.get_all_events(conn, ui['current_match_id'])
        incomplete_events = [e for e in events if e['incomplete'] == 1]
        
        if not incomplete_events:
            print("✗ No incomplete events")
            return
        
        # Find previous incomplete before current
        prev_event = None
        
        for event in reversed(incomplete_events):
            if event['event_id'] < current_event_id:
                prev_event = event
                break
        
        if prev_event:
            # Select previous event
            handle_event_selected(ui, prev_event['event_id'])
            
            # Highlight in list
            for i in range(ui['page_2']['event_list'].count()):
                item = ui['page_2']['event_list'].item(i)
                if item.data(Qt.UserRole) == prev_event['event_id']:
                    ui['page_2']['event_list'].setCurrentItem(item)
                    ui['page_2']['event_list'].scrollToItem(item)
                    break
            
            print(f"← Previous incomplete event: {prev_event['event_id']}")
        else:
            print("✗ No previous incomplete events")
            
    except Exception as e:
        print(f"✗ Error finding previous event: {e}")
    finally:
        conn.close()


def handle_next_incomplete_click(ui):
    """Navigate to next incomplete event"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    current_event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        # Get all incomplete events
        events = db.get_all_events(conn, ui['current_match_id'])
        incomplete_events = [e for e in events if e['incomplete'] == 1]
        
        if not incomplete_events:
            print("✗ No incomplete events")
            return
        
        # Find next incomplete after current
        next_event = None
        
        for event in incomplete_events:
            if event['event_id'] > current_event_id:
                next_event = event
                break
        
        if next_event:
            # Select next event
            handle_event_selected(ui, next_event['event_id'])
            
            # Highlight in list
            for i in range(ui['page_2']['event_list'].count()):
                item = ui['page_2']['event_list'].item(i)
                if item.data(Qt.UserRole) == next_event['event_id']:
                    ui['page_2']['event_list'].setCurrentItem(item)
                    ui['page_2']['event_list'].scrollToItem(item)
                    break
            
            print(f"→ Next incomplete event: {next_event['event_id']}")
        else:
            print("✓ No more incomplete events!")
            
    except Exception as e:
        print(f"✗ Error finding next event: {e}")
    finally:
        conn.close()

def handle_save_and_next_click(ui):
    """Save current event and navigate to next incomplete event"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    current_event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        # Note: Individual fields are already saved via their handlers (dropdowns, buttons)
        # This function just navigates to the next incomplete event
        
        # Get all incomplete events
        events = db.get_all_events(conn, ui['current_match_id'])
        incomplete_events = [e for e in events if e['incomplete'] == 1]
        
        if not incomplete_events:
            print("✓ No incomplete events - all done!")
            return
        
        # Find next incomplete after current
        next_event = None
        
        for event in incomplete_events:
            if event['event_id'] > current_event_id:
                next_event = event
                break
        
        if next_event:
            # Select next event
            handle_event_selected(ui, next_event['event_id'])
            
            # Highlight in list
            for i in range(ui['page_2']['event_list'].count()):
                item = ui['page_2']['event_list'].item(i)
                if item.data(Qt.UserRole) == next_event['event_id']:
                    ui['page_2']['event_list'].setCurrentItem(item)
                    ui['page_2']['event_list'].scrollToItem(item)
                    break
            
            print(f"✓ Saved. → Next incomplete event: {next_event['event_id']}")
        else:
            print("✓ Saved. No more incomplete events - all done!")
            
    except Exception as e:
        print(f"✗ Error in save & next: {e}")
    finally:
        conn.close()

def handle_cross_intention_click(ui, intention):
    """Handle cross intention button clicks"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        # Get current cross details
        event = db.get_event_details(conn, event_id)
        technique = event.get('technique')
        
        # Update intention
        db.update_cross_details(conn, event_id, intention, technique)
        
        # Update button colors
        ui['page_2']['intention_near_button'].idle_color = (165, 214, 167, 1) if intention == 'near_post' else (245, 245, 245, 1)
        ui['page_2']['intention_back_button'].idle_color = (165, 214, 167, 1) if intention == 'back_post' else (245, 245, 245, 1)
        ui['page_2']['intention_central_button'].idle_color = (165, 214, 167, 1) if intention == 'central' else (245, 245, 245, 1)
        ui['page_2']['intention_other_button'].idle_color = (165, 214, 167, 1) if intention == 'other' else (245, 245, 245, 1)  # ADD THIS
        
        print(f"✓ Cross intention updated: {intention}")
        
    except Exception as e:
        print(f"✗ Error updating cross intention: {e}")
    finally:
        conn.close()

def handle_pass_type_change(ui):
    """Handle pass length/height dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    
    # Get selected values
    length_text = ui['page_2']['pass_length_dropdown'].currentText()
    height_text = ui['page_2']['pass_height_dropdown'].currentText()
    
    pass_length = length_text.lower()
    pass_height = height_text.lower()
    
    conn = db.get_connection()
    try:
        db.update_pass_type(conn, event_id, pass_length, pass_height)
        print(f"✓ Pass type updated: {pass_length}/{pass_height}")
    except Exception as e:
        print(f"✗ Error updating pass type: {e}")
    finally:
        conn.close()

def handle_foul_reason_change(ui):
    """Handle foul reason dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    selected_text = ui['page_2']['foul_reason_dropdown'].currentText()
    
    # Map display text back to database values
    reason_reverse_mapping = {
        'Foul': 'foul',
        'Unfairness': 'unfairness',
        'Other': 'other',
        'Not Set': None
    }
    
    foul_reason = reason_reverse_mapping.get(selected_text)
    
    conn = db.get_connection()
    try:
        db.update_foul_reason(conn, event_id, foul_reason)
        print(f"✓ Foul reason updated: {foul_reason if foul_reason else 'Not Set'}")
    except Exception as e:
        print(f"✗ Error updating foul reason: {e}")
    finally:
        conn.close()

def handle_goto_page_2_click(ui):
    """Navigate to page 2 (Event Review)"""
    
    # Check if match has been started
    if not ui.get('current_match_id'):
        print("✗ No match loaded - start a match first")
        return
    
    # Switch to page 2 (index 2)
    ui['pages'].set_current_page(2)
    
    # Initialize page 2 with current match data
    initialize_page_2(ui)
    
    print(f"→ Switched to Event Review (Page 2)")


def handle_goto_page_1_click(ui):
    """Navigate back to page 1 (Live Recording)"""
    ui['pages'].set_current_page(1)
    print(f"→ Switched back to Live Recording (Page 1)")

def handle_rating_click(ui, rating_value):
    """Handle rating button clicks (S, F, or None)"""
    
    if not ui.get('current_review_event_id'):
        print("✗ No event selected")
        return
    
    event_id = ui['current_review_event_id']
    
    conn = db.get_connection()
    try:
        db.update_event_rating(conn, event_id, rating_value)
        
        # Update button colors
        if rating_value == 'S':
            ui['page_2']['rating_s_button'].idle_color = (165, 214, 167, 1)
            ui['page_2']['rating_f_button'].idle_color = (245, 245, 245, 1)
            ui['page_2']['rating_none_button'].idle_color = (245, 245, 245, 1)
        elif rating_value == 'F':
            ui['page_2']['rating_s_button'].idle_color = (245, 245, 245, 1)
            ui['page_2']['rating_f_button'].idle_color = (255, 205, 210, 1)
            ui['page_2']['rating_none_button'].idle_color = (245, 245, 245, 1)
        else:  # None
            ui['page_2']['rating_s_button'].idle_color = (245, 245, 245, 1)
            ui['page_2']['rating_f_button'].idle_color = (245, 245, 245, 1)
            ui['page_2']['rating_none_button'].idle_color = (224, 224, 224, 1)
        
        print(f"✓ Rating updated: {rating_value if rating_value else 'None'}")
        
    except Exception as e:
        print(f"✗ Error updating rating: {e}")
    finally:
        conn.close()

def handle_duel_winner_change(ui):
    """Handle duel winner dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    winner_id = ui['page_2']['duel_winner_dropdown'].currentData()
    
    # Get current loser_id
    conn = db.get_connection()
    try:
        event = db.get_event_details(conn, event_id)
        loser_id = event.get('duel_loser_id')
        
        db.update_duel_players(conn, event_id, winner_id, loser_id)
        print(f"✓ Duel winner updated: {winner_id if winner_id else 'Not Set'}")
    except Exception as e:
        print(f"✗ Error updating duel winner: {e}")
    finally:
        conn.close()


def handle_duel_loser_change(ui):
    """Handle duel loser dropdown change"""
    
    if not ui.get('current_review_event_id'):
        return
    
    event_id = ui['current_review_event_id']
    loser_id = ui['page_2']['duel_loser_dropdown'].currentData()
    
    # Get current winner_id
    conn = db.get_connection()
    try:
        event = db.get_event_details(conn, event_id)
        winner_id = event.get('duel_winner_id')
        
        db.update_duel_players(conn, event_id, winner_id, loser_id)
        print(f"✓ Duel loser updated: {loser_id if loser_id else 'Not Set'}")
    except Exception as e:
        print(f"✗ Error updating duel loser: {e}")
    finally:
        conn.close()

def handle_export_csv_click(ui):
    """Export all events to CSV"""
    
    if not ui.get('current_match_id'):
        print("✗ No match selected")
        return
    
    match_id = ui['current_match_id']
    
    # Create exports directory
    exports_dir = os.path.join(os.path.dirname(__file__), 'exports')
    os.makedirs(exports_dir, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"match_{match_id}_events_{timestamp}.csv"
    filepath = os.path.join(exports_dir, filename)
    
    # Export
    exporter = DataExporter(db)
    success = exporter.export_events_csv(match_id, filepath)
    
    if success:
        print(f"✓ Exported to: exports/{filename}")
    else:
        print("✗ Export failed")

# ===================================================
# =============== HELPER FUNCTIONS ==================
# ===================================================


def get_player_info(ui, button_name):
    """
    Get player info from button name
    
    Args:
        ui: Dictionary containing UI components
        button_name: Name of the button (e.g., 'h_gk', 'a_def_1')
        
    Returns:
        tuple: (player_id, team_id, player_name, jersey_num) or (None, None, None, None)
    """
    lineup = ui.get('lineup_data')
    if not lineup:
        return None, None, None, None
    
    # Parse button name
    parts = button_name.split('_')
    team_prefix = parts[0]  # 'h' or 'a'
    position = parts[1] if len(parts) > 1 else None
    index = int(parts[2]) - 1 if len(parts) > 2 else 0
    
    # Get team
    if team_prefix == 'h':
        team = lineup['home_team']
    elif team_prefix == 'a':
        team = lineup['away_team']
    else:
        return None, None, None, None
    
    # Get player
    try:
        if position == 'gk':
            player = team['players']['gk']
        elif position == 'def':
            player = team['players']['def'][index]
        elif position == 'mid':
            player = team['players']['mid'][index]
        elif position == 'fwd':
            player = team['players']['fwd'][index]
        elif position == 'sub':
            player = team['players']['sub'][index]
        else:
            return None, None, None, None
        
        return player['player_id'], team['team_id'], player['name'], player['jersey']
    
    except (IndexError, KeyError):
        return None, None, None, None


def get_player_name_and_jersey(ui, player_id):
    """
    Get player name and jersey from player_id
    
    Args:
        ui: Dictionary containing UI components
        player_id: The player's ID
        
    Returns:
        tuple: (name, jersey) or (None, None)
    """
    lineup = ui.get('lineup_data')
    if not lineup:
        return None, None
    
    for team_key in ['home_team', 'away_team']:
        team_players = lineup[team_key]['players']
        
        # Check goalkeeper
        if team_players.get('gk') and team_players['gk'].get('player_id') == player_id:
            return team_players['gk']['name'], team_players['gk']['jersey']
        
        # Check other positions
        for pos in ['def', 'mid', 'fwd', 'sub']:
            for player in team_players.get(pos, []):
                if player.get('player_id') == player_id:
                    return player['name'], player['jersey']
    
    return None, None


def update_event_log_display(ui):
    """
    Update the event log widget to show all events
    
    Args:
        ui: Dictionary containing UI components
    """
    if 'event_log_display' not in ui.get('page_1', {}):
        return
    
    event_log = ui.get('event_log', [])
    
    if not event_log:
        ui['page_1']['event_log_display'].setPlainText("--- Event Log ---\n\nNo events recorded yet.")
        return
    
    # Build log text
    log_lines = ["--- Event Log ---\n"]
    
    for event in event_log:
        log_lines.append(f"{event['timestamp']} | {event['description']}")
    
    log_text = "\n".join(log_lines)
    
    # Update display
    ui['page_1']['event_log_display'].setPlainText(log_text)
    
    # Auto-scroll to bottom (show most recent)
    cursor = ui['page_1']['event_log_display'].textCursor()
    cursor.movePosition(QTextCursor.End)
    ui['page_1']['event_log_display'].setTextCursor(cursor)
    

def populate_player_dropdown(ui, dropdown, selected_player_id=None):
    """Populate a player dropdown with all match players"""
    dropdown.clear()
    dropdown.addItem("Not Set", None)
    
    conn = db.get_connection()
    try:
        players = db.get_match_players(conn, ui['current_match_id'])
        
        for player in players:
            display_text = f"[{player['team_name']}] #{player['jersey_num']} {player['player_name']}"
            dropdown.addItem(display_text, player['player_id'])
        
        # Set selected player if provided
        if selected_player_id:
            for i in range(dropdown.count()):
                if dropdown.itemData(i) == selected_player_id:
                    dropdown.setCurrentIndex(i)
                    break
    finally:
        conn.close()

def show_event_player_dropdown(ui, event):
    """Show event player dropdown for events without specific player fields"""
    ui['page_2']['event_player_label'].is_visible = True
    ui['page_2']['event_player_dropdown'].show()
    
    # Populate with current event player
    player_id = event.get('player_id')
    populate_player_dropdown(ui, ui['page_2']['event_player_dropdown'], player_id)


def hide_event_player_dropdown(ui):
    """Hide event player dropdown"""
    ui['page_2']['event_player_label'].is_visible = False
    ui['page_2']['event_player_dropdown'].hide()


# ===================================================
# ============== 2. EVENT BINDINGS ==================
# ===================================================


def attach_events(ui):
    """
    Bind events to UI components.
    :param ui: Dictionary containing UI components.
    """
    
    # ============ PAGE 0 EVENTS ============
    
    def on_submit_click(button):
        success, match_id = handle_submit(ui)
        if success:
            ui["current_match_id"] = match_id
            print(f"→ Navigating to event collection page...")
            
            # Initialize page 1
            initialize_page_1(ui)
            
            # Navigate to page 1
            ui["pages"].set_current_page(1)
        else:
            print(f"✗ Cannot proceed to event collection - please fix errors")
    
    ui['page_0']['submit_lineups_button'].on_click = on_submit_click
    
    # ============ PAGE 1 EVENTS ============
    
    # Match flow buttons
    ui['page_1']['start_match_button'].on_click = lambda btn: handle_start_match_click(ui)

    # Delete last event button
    ui['page_1']['delete_button'].on_click = lambda _: handle_delete_last_click(ui)
    
    # Team buttons
    def bind_team_button(button_name, team_key):
        def handler(_):
            team_id = ui['lineup_data'][team_key]['team_id']
            handle_team_click(ui, team_id)
        ui['page_1'][button_name].on_click = handler
    
    bind_team_button('home_button', 'home_team')
    bind_team_button('away_button', 'away_team')
    
        # Player buttons - Home team
    for pos in ['gk']:
        button_name = f'h_{pos}'
        def make_handler(btn_name):
            def handler(_):
                player_id, team_id, player_name, jersey_num = get_player_info(ui, btn_name)
                if player_id:
                    handle_player_click(ui, player_id, team_id, player_name, jersey_num)
            return handler
        ui['page_1'][button_name].on_click = make_handler(button_name)

    for pos in ['def', 'mid']:
        for i in range(1, 5):
            button_name = f'h_{pos}_{i}'
            def make_handler(btn_name):
                def handler(_):
                    player_id, team_id, player_name, jersey_num = get_player_info(ui, btn_name)
                    if player_id:
                        handle_player_click(ui, player_id, team_id, player_name, jersey_num)
                return handler
            ui['page_1'][button_name].on_click = make_handler(button_name)

    for i in range(1, 3):
        button_name = f'h_fwd_{i}'
        def make_handler(btn_name):
            def handler(_):
                player_id, team_id, player_name, jersey_num = get_player_info(ui, btn_name)
                if player_id:
                    handle_player_click(ui, player_id, team_id, player_name, jersey_num)
            return handler
        ui['page_1'][button_name].on_click = make_handler(button_name)

    for i in range(1, 12):
        button_name = f'h_sub_{i}'
        def make_handler(btn_name):
            def handler(_):
                player_id, team_id, player_name, jersey_num = get_player_info(ui, btn_name)
                if player_id:
                    handle_player_click(ui, player_id, team_id, player_name, jersey_num)
            return handler
        ui['page_1'][button_name].on_click = make_handler(button_name)

    # Player buttons - Away team
    for pos in ['gk']:
        button_name = f'a_{pos}'
        def make_handler(btn_name):
            def handler(_):
                player_id, team_id, player_name, jersey_num = get_player_info(ui, btn_name)
                if player_id:
                    handle_player_click(ui, player_id, team_id, player_name, jersey_num)
            return handler
        ui['page_1'][button_name].on_click = make_handler(button_name)

    for pos in ['def', 'mid']:
        for i in range(1, 5):
            button_name = f'a_{pos}_{i}'
            def make_handler(btn_name):
                def handler(_):
                    player_id, team_id, player_name, jersey_num = get_player_info(ui, btn_name)
                    if player_id:
                        handle_player_click(ui, player_id, team_id, player_name, jersey_num)
                return handler
            ui['page_1'][button_name].on_click = make_handler(button_name)

    for i in range(1, 3):
        button_name = f'a_fwd_{i}'
        def make_handler(btn_name):
            def handler(_):
                player_id, team_id, player_name, jersey_num = get_player_info(ui, btn_name)
                if player_id:
                    handle_player_click(ui, player_id, team_id, player_name, jersey_num)
            return handler
        ui['page_1'][button_name].on_click = make_handler(button_name)

    for i in range(1, 12):
        button_name = f'a_sub_{i}'
        def make_handler(btn_name):
            def handler(_):
                player_id, team_id, player_name, jersey_num = get_player_info(ui, btn_name)
                if player_id:
                    handle_player_click(ui, player_id, team_id, player_name, jersey_num)
            return handler
        ui['page_1'][button_name].on_click = make_handler(button_name)
    
    # Pass buttons
    ui['page_1']['short_button'].on_click = lambda _: handle_pass_click(ui, 'short', 'low')
    ui['page_1']['short_high_button'].on_click = lambda _: handle_pass_click(ui, 'short', 'high')
    ui['page_1']['medium_button'].on_click = lambda _: handle_pass_click(ui, 'medium', 'low')
    ui['page_1']['med_high_button'].on_click = lambda _: handle_pass_click(ui, 'medium', 'high')
    ui['page_1']['long_button'].on_click = lambda _: handle_pass_click(ui, 'long', 'low')
    ui['page_1']['long_high_button'].on_click = lambda _: handle_pass_click(ui, 'long', 'high')
    
    # Shot button
    ui['page_1']['shot_button'].on_click = lambda _: handle_shot_click(ui)
    
    # Cross buttons
    ui['page_1']['cross_left_button'].on_click = lambda _: handle_cross_click(ui, 'left')
    ui['page_1']['cross_right_button'].on_click = lambda _: handle_cross_click(ui, 'right')
    
    # Set piece buttons
    ui['page_1']['throw_in_front_button'].on_click = lambda _: handle_set_piece_click(ui, 'throw_in_front')
    ui['page_1']['throw_in_rear_button'].on_click = lambda _: handle_set_piece_click(ui, 'throw_in_rear')
    ui['page_1']['direct_kick_button'].on_click = lambda _: handle_set_piece_click(ui, 'direct')
    ui['page_1']['indirect_kick_button'].on_click = lambda _: handle_set_piece_click(ui, 'indirect')
    ui['page_1']['pk_button'].on_click = lambda _: handle_set_piece_click(ui, 'penalty')
    ui['page_1']['corner_left_button'].on_click = lambda _: handle_set_piece_click(ui, 'corner_left')
    ui['page_1']['corner_right_button'].on_click = lambda _: handle_set_piece_click(ui, 'corner_right')
    ui['page_1']['goal_kick_button'].on_click = lambda _: handle_set_piece_click(ui, 'goal_kick')
    
    # Other action buttons
    ui['page_1']['ball_won_button'].on_click = lambda _: handle_ball_won_click(ui)
    ui['page_1']['clearance_button'].on_click = lambda _: handle_clearance_click(ui)
    ui['page_1']['blocked_button'].on_click = lambda _: handle_shot_blocked_click(ui)
    ui['page_1']['saved_button'].on_click = lambda _: handle_shot_saved_click(ui)
    
    # Card buttons
    ui['page_1']['yellow_button'].on_click = lambda _: handle_card_click(ui, 'yellow')
    ui['page_1']['red_button'].on_click = lambda _: handle_card_click(ui, 'red')
    
    # Foul button - dual functionality
    ui['page_1']['foul_button'].on_click = lambda _: handle_card_reason_foul(ui)

    # Offside button
    ui['page_1']['offside_button'].on_click = lambda _: handle_offside_click(ui)

    # Unfairness button (need to find this in your UI)
    ui['page_1']['unfairness_button'].on_click = lambda _: handle_card_reason_unfairness(ui)
    
    # Duel buttons
    ui['page_1']['ground_button'].on_click = lambda _: handle_duel_click(ui, 'ground')
    ui['page_1']['aerial_button'].on_click = lambda _: handle_duel_click(ui, 'aerial')
    
    # Substitution buttons
    def bind_substitution_button(button_name, team_key):
        def handler(_):
            team_id = ui['lineup_data'][team_key]['team_id']
            handle_substitution_click(ui, team_id)
        ui['page_1'][button_name].on_click = handler

    bind_substitution_button('h_substitute_button', 'home_team')
    bind_substitution_button('a_substitute_button', 'away_team')
    
    # Kickoff button
    ui['page_1']['kickoff_button'].on_click = lambda _: handle_kickoff_click(ui)

    #Halftime button
    ui['page_1']['halftime_button'].on_click = lambda _: handle_halftime_click(ui)

    # Overtime buttons
    ui['page_1']['overtime_button'].on_click = lambda _: handle_overtime_click(ui, 1)
    ui['page_1']['overtime_2_button'].on_click = lambda _: handle_overtime_click(ui, 2)

    # Pk Shootout button
    ui['page_1']['pk_shootout_button'].on_click = lambda _: handle_pk_shootout_click(ui)

    # Pause match button
    ui['page_1']['pause_match_button'].on_click = lambda _: handle_pause_match_click(ui)

    # End match button
    ui['page_1']['end_match_button'].on_click = lambda _: handle_end_match_click(ui)

    # Handball button
    ui['page_1']['handball_button'].on_click = lambda _: handle_handball_click(ui)

    # Shot button
    ui['page_1']['shot_button'].on_click = lambda _: handle_shot_click(ui)

    # Shot result buttons (update the existing bindings)
    ui['page_1']['over_left_button'].on_click = lambda _: handle_shot_result_click(ui, 'over_left')
    ui['page_1']['over_button'].on_click = lambda _: handle_shot_result_click(ui, 'over')
    ui['page_1']['over_right_button'].on_click = lambda _: handle_shot_result_click(ui, 'over_right')
    ui['page_1']['wide_left_button'].on_click = lambda _: handle_shot_result_click(ui, 'wide_left')
    ui['page_1']['wide_right_button'].on_click = lambda _: handle_shot_result_click(ui, 'wide_right')
    ui['page_1']['post_left_button'].on_click = lambda _: handle_shot_result_click(ui, 'post_left')
    ui['page_1']['post_right_button'].on_click = lambda _: handle_shot_result_click(ui, 'post_right')
    ui['page_1']['crossbar_button'].on_click = lambda _: handle_shot_result_click(ui, 'crossbar')
    ui['page_1']['failed_button'].on_click = lambda _: handle_shot_result_click(ui, 'failed')

    # Special shot results
    ui['page_1']['blocked_button'].on_click = lambda _: handle_shot_blocked_click(ui)
    ui['page_1']['saved_button'].on_click = lambda _: handle_shot_saved_click(ui)
    ui['page_1']['goal_button'].on_click = lambda _: handle_goal_click(ui)  

    # Own goal button
    ui['page_1']['own_goal_button'].on_click = lambda _: handle_own_goal_click(ui)

    # Got to page_2 button
    ui['page_1']['goto_page_2_button'].on_click = lambda _: handle_goto_page_2_click(ui)

    # page_2 -> page_1 button
    ui['page_2']['goto_page_1_button'].on_click = lambda _: handle_goto_page_1_click(ui)





# ===================================================
# ============== 3. MAIN FUNCTION ==================
# ===================================================


def main():
    app = pv.PvApp()
    ui = create_ui()
    attach_events(ui)
    ui["window"].show()
    app.run()


if __name__ == '__main__':
    main()