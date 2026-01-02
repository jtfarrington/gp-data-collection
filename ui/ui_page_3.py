"""
Page 3 - Analytics & Export
UI for match analytics, statistics, and data export functionality
"""

import pyvisual as pv
from PySide6.QtWidgets import QComboBox


def create_page_3_ui(window, ui):
    """Create Page 3 UI elements"""
    
    ui_page = {}
    
    # ==========================================
    # PAGE HEADER
    # ==========================================
    ui_page["title"] = pv.PvText(
        container=window, x=20, y=20, width=400, height=40,
        text='Analytics & Export',
        font_size=24,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=True
    )
    
    ui_page["match_info"] = pv.PvText(
        container=window, x=20, y=65, width=600, height=25,
        text='Select a match to view analytics',
        font_size=14,
        font_color=(100, 100, 100, 1),
        is_visible=True
    )
    
    # ==========================================
    # EXPORT SECTION
    # ==========================================
    ui_page["export_section_title"] = pv.PvText(
        container=window, x=20, y=120, width=300, height=30,
        text='Data Export',
        font_size=18,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=True
    )
    
    # Export Events CSV
    ui_page["export_events_button"] = pv.PvButton(
        container=window, x=20, y=160, width=200, height=40,
        text='Export Events CSV',
        font_size=13,
        font_color=(0, 0, 0, 1),
        idle_color=(165, 214, 167, 1), hover_color=(129, 199, 132, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=True
    )
    
    ui_page["export_events_description"] = pv.PvText(
        container=window, x=230, y=165, width=400, height=30,
        text='All events with complete details',
        font_size=12,
        font_color=(100, 100, 100, 1),
        is_visible=True
    )
    
    # Export Match Summary CSV
    ui_page["export_summary_button"] = pv.PvButton(
        container=window, x=20, y=210, width=200, height=40,
        text='Export Summary CSV',
        font_size=13,
        font_color=(0, 0, 0, 1),
        idle_color=(165, 214, 167, 1), hover_color=(129, 199, 132, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=True
    )
    
    ui_page["export_summary_description"] = pv.PvText(
        container=window, x=230, y=215, width=400, height=30,
        text='Match statistics by team',
        font_size=12,
        font_color=(100, 100, 100, 1),
        is_visible=True
    )
    
    # Export Player Stats CSV
    ui_page["export_players_button"] = pv.PvButton(
        container=window, x=20, y=260, width=200, height=40,
        text='Export Player Stats CSV',
        font_size=13,
        font_color=(0, 0, 0, 1),
        idle_color=(165, 214, 167, 1), hover_color=(129, 199, 132, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=True
    )
    
    ui_page["export_players_description"] = pv.PvText(
        container=window, x=230, y=265, width=400, height=30,
        text='Individual player performance metrics',
        font_size=12,
        font_color=(100, 100, 100, 1),
        is_visible=True
    )
    
    # Export status message
    ui_page["export_status"] = pv.PvText(
        container=window, x=20, y=315, width=600, height=25,
        text='',
        font_size=13,
        font_color=(0, 150, 0, 1), bold=True,
        is_visible=True
    )
    
    # ==========================================
    # STATISTICS SECTION (PLACEHOLDER)
    # ==========================================
    ui_page["stats_section_title"] = pv.PvText(
        container=window, x=20, y=370, width=300, height=30,
        text='Match Statistics',
        font_size=18,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=True
    )
    
    ui_page["stats_placeholder"] = pv.PvText(
        container=window, x=20, y=410, width=600, height=100,
        text='Statistics visualization coming soon...\n\n'
             'Export data to CSV to view in Excel or other tools.',
        font_size=14,
        font_color=(100, 100, 100, 1),
        is_visible=True
    )
    
    # ==========================================
    # NAVIGATION
    # ==========================================
    ui_page["goto_page_1_button"] = pv.PvButton(
        container=window, x=10, y=680, width=50, height=30,
        text='←',
        font_size=18,
        font_color=(0, 0, 0, 1), bold=True,
        idle_color=(255, 235, 238, 1), hover_color=(255, 205, 210, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=True
    )
    
    ui_page["goto_page_2_button"] = pv.PvButton(
        container=window, x=70, y=680, width=100, height=30,
        text='Review Events',
        font_size=13,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=True
    )
    
    return ui_page