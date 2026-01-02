"""
Data Export Module
Handles exporting match data to CSV, Excel, JSON, and PDF formats
"""

import csv
import os
from datetime import datetime


class DataExporter:
    """Handle all data export operations"""
    
    def __init__(self, database):
        """
        Initialize exporter with database connection
        
        Args:
            database: MatchDatabase instance
        """
        self.db = database
    
    def export_events_csv(self, match_id, output_path):
        """
        Export all events from a match to CSV
        
        Args:
            match_id: Match ID to export
            output_path: Path to save CSV file
            
        Returns:
            True if successful, False otherwise
        """
        conn = self.db.get_connection()
        try:
            # Get all events with full details
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT 
                    e.event_id,
                    e.time,
                    e.location_x,
                    e.location_y,
                    e.rating,
                    t.team_name,
                    p.player_name,
                    p.jersey_num,
                    
                    -- Event Type Classification
                    CASE 
                        WHEN pa.event_id IS NOT NULL THEN 'Pass'
                        WHEN sh.event_id IS NOT NULL THEN 'Shot'
                        WHEN cr.event_id IS NOT NULL THEN 'Cross'
                        WHEN g.event_id IS NOT NULL THEN 'Goal'
                        WHEN og.event_id IS NOT NULL THEN 'Own Goal'
                        WHEN fo.event_id IS NOT NULL THEN 'Foul'
                        WHEN ca.event_id IS NOT NULL THEN 'Card'
                        WHEN du.event_id IS NOT NULL THEN 'Duel'
                        WHEN os.event_id IS NOT NULL THEN 'Offside'
                        WHEN hb.event_id IS NOT NULL THEN 'Handball'
                        WHEN su.event_id IS NOT NULL THEN 'Substitution'
                        WHEN sp.event_id IS NOT NULL THEN 'Set Piece'
                        WHEN br.event_id IS NOT NULL THEN 'Ball Received'
                        WHEN bw.event_id IS NOT NULL THEN 'Ball Won'
                        WHEN cl.event_id IS NOT NULL THEN 'Clearance'
                        WHEN sb.event_id IS NOT NULL THEN 'Shot Block'
                        WHEN ss.event_id IS NOT NULL THEN 'Shot Save'
                        ELSE 'Other'
                    END as event_type,
                    
                    -- Pass Details
                    pa.pass_length,
                    pa.pass_height,
                    pa.assist,
                    pa.line_split,
                    
                    -- Shot Details
                    sh.execution as shot_execution,
                    sh.result as shot_result,
                    
                    -- Cross Details
                    cr.intention as cross_intention,
                    cr.technique as cross_technique,
                    
                    -- Goal Details
                    g.goal_zone,
                    
                    -- Ball Played
                    bp.from_open_play,
                    
                    -- Foul Details
                    fo.reason as foul_reason,
                    
                    -- Card Details
                    ca.color as card_color,
                    ca.reason as card_reason,
                    
                    -- Duel Details
                    du.context as duel_context,
                    
                    -- Set Piece
                    sp.type as set_piece_type
                    
                FROM event e
                JOIN team t ON e.team_id = t.team_id
                JOIN player p ON e.player_id = p.player_id
                
                -- Join all event type tables
                LEFT JOIN ball_played bp ON e.event_id = bp.event_id
                LEFT JOIN ball_received br ON e.event_id = br.event_id
                
                -- Ball Played subtypes
                LEFT JOIN pass pa ON bp.event_id = pa.event_id
                LEFT JOIN shot sh ON bp.event_id = sh.event_id
                LEFT JOIN cross_played cr ON bp.event_id = cr.event_id
                
                -- Ball Received subtypes
                LEFT JOIN ball_won bw ON br.event_id = bw.event_id
                LEFT JOIN clearance cl ON br.event_id = cl.event_id
                LEFT JOIN shot_block sb ON br.event_id = sb.event_id
                LEFT JOIN shot_save ss ON br.event_id = ss.event_id
                
                -- Direct event types
                LEFT JOIN goal g ON e.event_id = g.event_id
                LEFT JOIN own_goal og ON e.event_id = og.event_id
                LEFT JOIN foul fo ON e.event_id = fo.event_id
                LEFT JOIN card ca ON e.event_id = ca.event_id
                LEFT JOIN duel du ON e.event_id = du.event_id
                LEFT JOIN offside os ON e.event_id = os.event_id
                LEFT JOIN handball hb ON e.event_id = hb.event_id
                LEFT JOIN substitution su ON e.event_id = su.event_id
                LEFT JOIN set_piece sp ON e.event_id = sp.event_id
                
                WHERE e.match_id = %s
                ORDER BY e.event_id
            """, (match_id,))
            
            events = cursor.fetchall()
            cursor.close()
            
            if not events:
                print(f"✗ No events found for match {match_id}")
                return False
            
            # Write to CSV
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                # Get column names from first row
                fieldnames = events[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(events)
            
            print(f"✓ Exported {len(events)} events to {output_path}")
            return True
            
        except Exception as e:
            print(f"✗ Error exporting events: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            conn.close()
    
    def export_match_summary_csv(self, match_id, output_path):
        """
        Export match summary statistics to CSV
        
        Args:
            match_id: Match ID to export
            output_path: Path to save CSV file
            
        Returns:
            True if successful, False otherwise
        """
        conn = self.db.get_connection()
        try:
            # Get match info
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT 
                    m.match_id,
                    m.venue,
                    m.competition,
                    m.match_start,
                    m.match_end,
                    home.team_name as home_team,
                    away.team_name as away_team
                FROM match_metadata m
                JOIN team home ON m.home_id = home.team_id
                JOIN team away ON m.away_id = away.team_id
                WHERE m.match_id = %s
            """, (match_id,))
            match_info = cursor.fetchone()
            cursor.close()
            
            if not match_info:
                print(f"✗ Match {match_id} not found")
                return False
            
            # Get statistics by team
            stats = []
            
            for team_name in [match_info['home_team'], match_info['away_team']]:
                cursor = conn.cursor(dictionary=True)
                cursor.execute("""
                    SELECT 
                        t.team_name,
                        
                        -- Total events
                        COUNT(e.event_id) as total_events,
                        
                        -- Passes
                        SUM(CASE WHEN pa.event_id IS NOT NULL THEN 1 ELSE 0 END) as passes,
                        
                        -- Shots
                        SUM(CASE WHEN sh.event_id IS NOT NULL THEN 1 ELSE 0 END) as shots,
                        SUM(CASE WHEN sh.result IN ('goal', 'saved') THEN 1 ELSE 0 END) as shots_on_target,
                        
                        -- Goals
                        SUM(CASE WHEN g.event_id IS NOT NULL THEN 1 ELSE 0 END) as goals,
                        
                        -- Fouls & Cards
                        SUM(CASE WHEN fo.event_id IS NOT NULL THEN 1 ELSE 0 END) as fouls,
                        SUM(CASE WHEN ca.event_id IS NOT NULL AND ca.color = 'yellow' THEN 1 ELSE 0 END) as yellow_cards,
                        SUM(CASE WHEN ca.event_id IS NOT NULL AND ca.color = 'red' THEN 1 ELSE 0 END) as red_cards,
                        
                        -- Duels
                        SUM(CASE WHEN du.event_id IS NOT NULL THEN 1 ELSE 0 END) as duels
                        
                    FROM event e
                    JOIN team t ON e.team_id = t.team_id
                    LEFT JOIN ball_played bp ON e.event_id = bp.event_id
                    LEFT JOIN pass pa ON bp.event_id = pa.event_id
                    LEFT JOIN shot sh ON bp.event_id = sh.event_id
                    LEFT JOIN goal g ON e.event_id = g.event_id
                    LEFT JOIN foul fo ON e.event_id = fo.event_id
                    LEFT JOIN card ca ON e.event_id = ca.event_id
                    LEFT JOIN duel du ON e.event_id = du.event_id
                    
                    WHERE e.match_id = %s AND t.team_name = %s
                    GROUP BY t.team_name
                """, (match_id, team_name))
                
                team_stats = cursor.fetchone()
                cursor.close()
                
                if team_stats:
                    stats.append(team_stats)
            
            # Write to CSV
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                # Header rows
                csvfile.write(f"Match Summary\n")
                csvfile.write(f"Match ID:,{match_info['match_id']}\n")
                csvfile.write(f"Venue:,{match_info['venue']}\n")
                csvfile.write(f"Competition:,{match_info['competition']}\n")
                csvfile.write(f"Home Team:,{match_info['home_team']}\n")
                csvfile.write(f"Away Team:,{match_info['away_team']}\n")
                csvfile.write(f"\n")
                
                # Stats table
                if stats:
                    fieldnames = stats[0].keys()
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(stats)
            
            print(f"✓ Exported match summary to {output_path}")
            return True
            
        except Exception as e:
            print(f"✗ Error exporting match summary: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            conn.close()
    
    def export_player_stats_csv(self, match_id, output_path):
        """
        Export player statistics to CSV
        
        Args:
            match_id: Match ID to export
            output_path: Path to save CSV file
            
        Returns:
            True if successful, False otherwise
        """
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT 
                    t.team_name,
                    p.player_name,
                    p.jersey_num,
                    
                    -- Event counts
                    COUNT(e.event_id) as total_events,
                    SUM(CASE WHEN pa.event_id IS NOT NULL THEN 1 ELSE 0 END) as passes,
                    SUM(CASE WHEN sh.event_id IS NOT NULL THEN 1 ELSE 0 END) as shots,
                    SUM(CASE WHEN g.event_id IS NOT NULL THEN 1 ELSE 0 END) as goals,
                    SUM(CASE WHEN pa.assist = 1 THEN 1 ELSE 0 END) as assists,
                    SUM(CASE WHEN fo.event_id IS NOT NULL THEN 1 ELSE 0 END) as fouls_committed,
                    SUM(CASE WHEN ca.event_id IS NOT NULL THEN 1 ELSE 0 END) as cards_received,
                    SUM(CASE WHEN du.winner_id = p.player_id THEN 1 ELSE 0 END) as duels_won,
                    SUM(CASE WHEN du.loser_id = p.player_id THEN 1 ELSE 0 END) as duels_lost
                    
                FROM event e
                JOIN team t ON e.team_id = t.team_id
                JOIN player p ON e.player_id = p.player_id
                LEFT JOIN ball_played bp ON e.event_id = bp.event_id
                LEFT JOIN pass pa ON bp.event_id = pa.event_id
                LEFT JOIN shot sh ON bp.event_id = sh.event_id
                LEFT JOIN goal g ON e.event_id = g.event_id
                LEFT JOIN foul fo ON e.event_id = fo.event_id
                LEFT JOIN card ca ON e.event_id = ca.event_id
                LEFT JOIN duel du ON e.event_id = du.event_id
                
                WHERE e.match_id = %s
                GROUP BY t.team_name, p.player_name, p.jersey_num
                ORDER BY t.team_name, total_events DESC
            """, (match_id,))
            
            player_stats = cursor.fetchall()
            cursor.close()
            
            if not player_stats:
                print(f"✗ No player stats found for match {match_id}")
                return False
            
            # Write to CSV
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = player_stats[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(player_stats)
            
            print(f"✓ Exported stats for {len(player_stats)} players to {output_path}")
            return True
            
        except Exception as e:
            print(f"✗ Error exporting player stats: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            conn.close()