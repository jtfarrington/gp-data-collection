import pyvisual as pv
from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QComboBox, QScrollArea, QWidget


def create_page_2_ui(window, ui):
    """
    Create and return UI elements for Page 2 (Event Review).
    
    Args:
        window: The main window
        ui: UI state dictionary
        
    Returns:
        Dictionary of UI elements
    """
    ui_page = {}
    
    # ==========================================
    # HEADER
    # ==========================================
    ui_page["title"] = pv.PvText(
        container=window, x=20, y=10, width=400, height=40,
        text='Event Review & Enhancement',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=20,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=True
    )
    
    ui_page["match_info"] = pv.PvText(
        container=window, x=20, y=50, width=400, height=30,
        text='Match: Loading...',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=14,
        font_color=(80, 80, 80, 1),
        is_visible=True
    )
    
    # ==========================================
    # FILTERS
    # ==========================================
    ui_page["filter_label"] = pv.PvText(
        container=window, x=20, y=90, width=80, height=30,
        text='Filter:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1),
        is_visible=True
    )
    
    ui_page["filter_all_button"] = pv.PvButton(
        container=window, x=100, y=90, width=70, height=30,
        text='All Events',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1
    )
    
    ui_page["filter_shots_button"] = pv.PvButton(
        container=window, x=175, y=90, width=70, height=30,
        text='Shots',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        border_color=(220, 220, 220, 1), border_thickness=1
    )
    
    ui_page["filter_passes_button"] = pv.PvButton(
        container=window, x=250, y=90, width=70, height=30,
        text='Passes',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        border_color=(220, 220, 220, 1), border_thickness=1
    )
    
    ui_page["filter_incomplete_button"] = pv.PvButton(
        container=window, x=325, y=90, width=100, height=30,
        text='Incomplete',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        border_color=(220, 220, 220, 1), border_thickness=1
    )

    ui_page["filter_ball_flow_button"] = pv.PvButton(
    container=window, x=430, y=90, width=120, height=30,
    text='Show Ball Flow',
    font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
    font_color=(0, 0, 0, 1),
    idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
    border_color=(220, 220, 220, 1), border_thickness=1
)
    
    # ==========================================
    # LEFT PANEL - EVENT LIST
    # ==========================================
    event_list_widget = QListWidget()
    event_list_widget.setParent(window)
    event_list_widget.setGeometry(20, 130, 400, 550)
    event_list_widget.setStyleSheet("""
        QListWidget {
            background-color: #f5f5f5;
            border: 2px solid #dcdcdc;
            border-radius: 5px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
        QListWidget::item {
            padding: 8px;
            border-bottom: 1px solid #e0e0e0;
        }
        QListWidget::item:selected {
            background-color: #c8e6c9;
            color: black;
        }
        QListWidget::item:hover {
            background-color: #e8f5e9;
        }
    """)
    ui_page["event_list"] = event_list_widget
    
    # ==========================================
    # RIGHT PANEL - EVENT DETAILS (COMMON)
    # ==========================================

    # Create scroll area for detail panel
    scroll_area = QScrollArea()
    scroll_area.setParent(window)
    scroll_area.setGeometry(440, 130, 620, 550)
    scroll_area.setWidgetResizable(True)
    scroll_area.setStyleSheet("""
        QScrollArea {
            background-color: #f0f0f0;
            border: 2px solid #dcdcdc;
            border-radius: 5px;
        }
        QScrollBar:vertical {
            border: none;
            background: #f0f0f0;
            width: 10px;
            margin: 0px;
        }
        QScrollBar::handle:vertical {
            background: #c0c0c0;
            min-height: 20px;
            border-radius: 5px;
        }
        QScrollBar::handle:vertical:hover {
            background: #a0a0a0;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            border: none;
            background: none;
        }
    """)

    # Create a widget to hold all the detail fields
    scroll_content = QWidget()
    scroll_content.setMinimumSize(600, 1500)  # Set minimum height for scrolling
    scroll_area.setWidget(scroll_content)

    ui_page["detail_scroll_area"] = scroll_area
    ui_page["detail_scroll_content"] = scroll_content

    ui_page["event_header"] = pv.PvText(
        container=scroll_content, x=20, y=10, width=580, height=30,
        text='Select an event to view details',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=16,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=True
    )
    
    ui_page["event_info"] = pv.PvText(
        container=scroll_content, x=20, y=45, width=580, height=60,
        text='',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(80, 80, 80, 1),
        is_visible=True
    )
    
    # ==========================================
    # COMMON FIELDS (ALL EVENTS)
    # ==========================================
    
    # Location Section
    ui_page["location_label"] = pv.PvText(
        container=scroll_content, x=20, y=115, width=200, height=25,
        text='Location:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )
    
    ui_page["location_display"] = pv.PvText(
        container=scroll_content, x=20, y=145, width=300, height=25,
        text='Not set',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(100, 100, 100, 1),
        is_visible=False
    )
    
    ui_page["set_location_button"] = pv.PvButton(
        container=scroll_content, x=20, y=175, width=150, height=35,
        text='Set Location',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1),
        idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    # Rating Section
    ui_page["rating_label"] = pv.PvText(
        container=scroll_content, x=20, y=225, width=200, height=25,
        text='Rating:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )
    
    ui_page["rating_s_button"] = pv.PvButton(
        container=scroll_content, x=20, y=255, width=80, height=30,
        text='Success',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(165, 214, 167, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["rating_f_button"] = pv.PvButton(
        container=scroll_content, x=110, y=255, width=80, height=30,
        text='Failure',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(255, 205, 210, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["rating_none_button"] = pv.PvButton(
    container=scroll_content, x=200, y=255, width=80, height=30,
    text='No Rating',
    font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
    font_color=(0, 0, 0, 1),
    idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
    border_color=(220, 220, 220, 1), border_thickness=1,
    is_visible=False
    )

    # Event Player (for events without specific player fields)
    ui_page["event_player_label"] = pv.PvText(
        container=scroll_content, x=20, y=295, width=200, height=25,
        text='Event Player:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["event_player_dropdown"] = QComboBox()
    ui_page["event_player_dropdown"].setParent(scroll_content)
    ui_page["event_player_dropdown"].setGeometry(20, 325, 250, 30)
    ui_page["event_player_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["event_player_dropdown"].hide()
    
    # ==========================================
    # BALL PLAYED - FROM OPEN PLAY
    # ==========================================
    ui_page["from_open_play_label"] = pv.PvText(
        container=scroll_content, x=20, y=375, width=200, height=25,
        text='From Open Play:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["from_open_play_yes_button"] = pv.PvButton(
        container=scroll_content, x=20, y=405, width=80, height=30,
        text='Yes',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(165, 214, 167, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["from_open_play_no_button"] = pv.PvButton(
        container=scroll_content, x=110, y=405, width=80, height=30,
        text='No',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    # ==========================================
    # SHOT-SPECIFIC FIELDS
    # ==========================================
    ui_page["shot_execution_label"] = pv.PvText(
        container=scroll_content, x=260, y=115, width=200, height=25,
        text='Execution:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )
    
    ui_page["exec_left_button"] = pv.PvButton(
        container=scroll_content, x=260, y=145, width=80, height=30,
        text='Left',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["exec_right_button"] = pv.PvButton(
        container=scroll_content, x=350, y=145, width=80, height=30,
        text='Right',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["exec_header_button"] = pv.PvButton(
        container=scroll_content, x=440, y=145, width=80, height=30,
        text='Header',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["exec_other_button"] = pv.PvButton(
        container=scroll_content, x=530, y=145, width=80, height=30,
        text='Other',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["shot_result_label"] = pv.PvText(
    container=scroll_content, x=260, y=185, width=200, height=25,
    text='Result:',
    font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
    font_color=(0, 0, 0, 1), bold=True,
    is_visible=False
)

    ui_page["shot_result_dropdown"] = QComboBox()
    ui_page["shot_result_dropdown"].setParent(scroll_content)
    ui_page["shot_result_dropdown"].setGeometry(260, 215, 200, 30)
    ui_page["shot_result_dropdown"].addItems([
        "Not Set",
        "Over",
        "Wide Left",
        "Wide Right",
        "Post",
        "Crossbar",
        "Saved",
        "Blocked",
        "Goal"
    ])
    ui_page["shot_result_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["shot_result_dropdown"].hide()
    
    # ==========================================
    # PASS-SPECIFIC FIELDS
    # ==========================================

    ui_page["pass_type_label"] = pv.PvText(
    container=scroll_content, x=260, y=375, width=200, height=25,
    text='Pass Type:',
    font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
    font_color=(0, 0, 0, 1), bold=True,
    is_visible=False
)

    ui_page["pass_length_dropdown"] = QComboBox()
    ui_page["pass_length_dropdown"].setParent(scroll_content)
    ui_page["pass_length_dropdown"].setGeometry(260, 405, 120, 30)
    ui_page["pass_length_dropdown"].addItems(["Short", "Medium", "Long"])
    ui_page["pass_length_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["pass_length_dropdown"].hide()

    ui_page["pass_height_dropdown"] = QComboBox()
    ui_page["pass_height_dropdown"].setParent(scroll_content)
    ui_page["pass_height_dropdown"].setGeometry(390, 405, 120, 30)
    ui_page["pass_height_dropdown"].addItems(["Low", "High"])
    ui_page["pass_height_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["pass_height_dropdown"].hide()

    ui_page["pass_assist_label"] = pv.PvText(
        container=scroll_content, x=260, y=185, width=200, height=25,
        text='Assist:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )
    ui_page["pass_assist_label"] = pv.PvText(
        container=scroll_content, x=260, y=115, width=200, height=25,
        text='Assist:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )
    
    ui_page["assist_yes_button"] = pv.PvButton(
        container=scroll_content, x=260, y=145, width=80, height=30,
        text='Yes',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(165, 214, 167, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["assist_no_button"] = pv.PvButton(
        container=scroll_content, x=350, y=145, width=80, height=30,
        text='No',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["line_split_label"] = pv.PvText(
        container=scroll_content, x=260, y=185, width=200, height=25,
        text='Line Split:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )
    
    ui_page["line_split_yes_button"] = pv.PvButton(
        container=scroll_content, x=260, y=215, width=80, height=30,
        text='Yes',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(165, 214, 167, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["line_split_no_button"] = pv.PvButton(
        container=scroll_content, x=350, y=215, width=80, height=30,
        text='No',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    # Into Area buttons (similar to assist/line_split)
    ui_page["into_area_label"] = pv.PvText(
        container=scroll_content, x=20, y=450, width=200, height=25,
        text='Into Area:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["into_area_yes_button"] = pv.PvButton(
        container=scroll_content, x=20, y=480, width=80, height=30,
        text='Yes',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(165, 214, 167, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["into_area_no_button"] = pv.PvButton(
        container=scroll_content, x=110, y=480, width=80, height=30,
        text='No',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    # ==========================================
    # CROSS-SPECIFIC FIELDS
    # ==========================================
    ui_page["cross_intention_label"] = pv.PvText(
        container=scroll_content, x=260, y=115, width=200, height=25,
        text='Intention:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )
    
    ui_page["intention_near_button"] = pv.PvButton(
        container=scroll_content, x=260, y=145, width=90, height=30,
        text='Near Post',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["intention_back_button"] = pv.PvButton(
        container=scroll_content, x=360, y=145, width=90, height=30,
        text='Back Post',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["intention_central_button"] = pv.PvButton(
        container=scroll_content, x=460, y=145, width=90, height=30,
        text='Central',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["intention_other_button"] = pv.PvButton(
    container=scroll_content, x=260, y=185, width=90, height=30,  
    text='Other',
    font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
    font_color=(0, 0, 0, 1),
    idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
    border_color=(220, 220, 220, 1), border_thickness=1,
    is_visible=False
)
    
    ui_page["cross_technique_label"] = pv.PvText(
        container=scroll_content, x=290, y=225, width=200, height=25,
        text='Technique:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )
    
    ui_page["technique_inswing_button"] = pv.PvButton(
        container=scroll_content, x=290, y=255, width=90, height=30,
        text='Inswing',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["technique_outswing_button"] = pv.PvButton(
        container=scroll_content, x=390, y=255, width=90, height=30,
        text='Outswing',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    ui_page["technique_other_button"] = pv.PvButton(
        container=scroll_content, x=490, y=255, width=90, height=30,
        text='Other',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )
    
    # ==========================================
    # GOAL-SPECIFIC FIELDS
    # ==========================================

    ui_page["goal_zone_label"] = pv.PvText(
    container=scroll_content, x=260, y=115, width=200, height=25,
    text='Goal Zone:',
    font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
    font_color=(0, 0, 0, 1), bold=True,
    is_visible=False
    )

    ui_page["goal_zone_dropdown"] = QComboBox()
    ui_page["goal_zone_dropdown"].setParent(scroll_content)
    ui_page["goal_zone_dropdown"].setGeometry(260, 145, 200, 30)
    ui_page["goal_zone_dropdown"].addItems([
        "Not Set",
        "Low Right 90",
        "Upper Right 90", 
        "Lower Left 90",
        "Upper Left 90",
        "Central",
        "Left",
        "Right"
    ])
    ui_page["goal_zone_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
        QComboBox::drop-down {
            border: none;
        }
        QComboBox::down-arrow {
            image: url(down_arrow.png);
            width: 12px;
            height: 12px;
        }
    """)
    ui_page["goal_zone_dropdown"].hide()

    # ==========================================
    # FOUL-SPECIFIC FIELDS
    # ==========================================
    ui_page["foul_reason_label"] = pv.PvText(
        container=scroll_content, x=310, y=225, width=200, height=25,
        text='Foul Reason:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["foul_reason_dropdown"] = QComboBox()
    ui_page["foul_reason_dropdown"].setParent(scroll_content)
    ui_page["foul_reason_dropdown"].setGeometry(310, 255, 200, 30)
    ui_page["foul_reason_dropdown"].addItems([
        "Not Set",
        "Foul",
        "Unfairness",
        "Other"
    ])
    ui_page["foul_reason_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["foul_reason_dropdown"].hide()

    # Foul Guilty Player
    ui_page["foul_guilty_label"] = pv.PvText(
        container=scroll_content, x=20, y=315, width=200, height=25,
        text='Guilty Player:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["foul_guilty_dropdown"] = QComboBox()
    ui_page["foul_guilty_dropdown"].setParent(scroll_content)
    ui_page["foul_guilty_dropdown"].setGeometry(20, 345, 250, 30)
    ui_page["foul_guilty_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["foul_guilty_dropdown"].hide()

    # Foul Innocent Player
    ui_page["foul_innocent_label"] = pv.PvText(
        container=scroll_content, x=20, y=385, width=200, height=25,
        text='Innocent Player:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["foul_innocent_dropdown"] = QComboBox()
    ui_page["foul_innocent_dropdown"].setParent(scroll_content)
    ui_page["foul_innocent_dropdown"].setGeometry(20, 415, 250, 30)
    ui_page["foul_innocent_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["foul_innocent_dropdown"].hide()

    # ==========================================
    # CARD-SPECIFIC FIELDS
    # ==========================================
    ui_page["card_reason_label"] = pv.PvText(
        container=scroll_content, x=310, y=225, width=200, height=25,
        text='Card Reason:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    # Card Color
    ui_page["card_color_label"] = pv.PvText(
        container=scroll_content, x=260, y=400, width=200, height=25,
        text='Card Color:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["card_yellow_button"] = pv.PvButton(
        container=scroll_content, x=260, y=430, width=90, height=30,
        text='Yellow',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(255, 241, 118, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["card_second_yellow_button"] = pv.PvButton(
        container=scroll_content, x=360, y=430, width=120, height=30,
        text='2nd Yellow',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(255, 183, 77, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["card_red_button"] = pv.PvButton(
        container=scroll_content, x=490, y=430, width=90, height=30,
        text='Red',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(255, 205, 210, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["card_reason_dropdown"] = QComboBox()
    ui_page["card_reason_dropdown"].setParent(scroll_content)
    ui_page["card_reason_dropdown"].setGeometry(310, 255, 200, 30)
    ui_page["card_reason_dropdown"].addItems([
        "Not Set",
        "Foul",
        "Unfairness",
        "Other"
    ])
    ui_page["card_reason_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["card_reason_dropdown"].hide()

    # ==========================================
    # DUEL-SPECIFIC FIELDS
    # ==========================================
    ui_page["duel_winner_label"] = pv.PvText(
        container=scroll_content, x=20, y=345, width=200, height=25,
        text='Duel Winner:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    # ==========================================
    # DUEL-SPECIFIC FIELDS
    # ==========================================
    ui_page["duel_context_label"] = pv.PvText(
        container=scroll_content, x=20, y=320, width=200, height=25,
        text='Context:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["duel_ground_button"] = pv.PvButton(
        container=scroll_content, x=140, y=340, width=100, height=30,
        text='Ground',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["duel_aerial_button"] = pv.PvButton(
        container=scroll_content, x=20, y=340, width=100, height=30,
        text='Aerial',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["duel_winner_label"] = pv.PvText(
        container=scroll_content, x=250, y=115, width=200, height=25,  # Adjusted y position
        text='Duel Winner:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["duel_winner_dropdown"] = QComboBox()
    ui_page["duel_winner_dropdown"].setParent(scroll_content)
    ui_page["duel_winner_dropdown"].setGeometry(250, 145, 250, 30)
    ui_page["duel_winner_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["duel_winner_dropdown"].hide()

    ui_page["duel_loser_label"] = pv.PvText(
        container=scroll_content, x=250, y=185, width=200, height=25,
        text='Duel Loser:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["duel_loser_dropdown"] = QComboBox()
    ui_page["duel_loser_dropdown"].setParent(scroll_content)
    ui_page["duel_loser_dropdown"].setGeometry(250, 215, 250, 30)
    ui_page["duel_loser_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["duel_loser_dropdown"].hide()
        
    # ==========================================
    # ACTION BUTTONS
    # ==========================================
    ui_page["save_button"] = pv.PvButton(
        container=window, x=460, y=630, width=120, height=40,
        text='Save',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=14,
        idle_color=(165, 214, 167, 1), hover_color=(129, 199, 132, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=True
    )
    
    ui_page["save_next_button"] = pv.PvButton(
        container=window, x=590, y=630, width=180, height=40,
        text='Save & Next',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=14,
        idle_color=(165, 214, 167, 1), hover_color=(129, 199, 132, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=True
    )
    
    ui_page["prev_incomplete_button"] = pv.PvButton(
        container=window, x=780, y=630, width=130, height=40,
        text='< Prev',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=14,
        idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=True
    )
    
    ui_page["next_incomplete_button"] = pv.PvButton(
        container=window, x=920, y=630, width=130, height=40,
        text='Next >',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=14,
        idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=True
    )

    # Navigation back to Page 1
    ui_page["goto_page_1_button"] = pv.PvButton(
        container=window, x=20, y=680, width=50, height=30,
        text='←',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=18,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=True, italic=False,
        underline=False, strikethrough=False, 
        idle_color=(255, 235, 238, 1), hover_color=(255, 205, 210, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), 
        border_hover_color=None, border_thickness=1,
        corner_radius=0, border_style="solid", 
        box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', 
        box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), 
        icon_color_hover=None, icon_spacing=0, icon_scale=1, 
        paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None
    )

    # ==========================================
    # SET PIECE-SPECIFIC FIELDS
    # ==========================================
    ui_page["set_piece_type_label"] = pv.PvText(
        container=scroll_content, x=300, y=115, width=200, height=25,
        text='Set Piece Type:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    # Row 1: Corners and Throws
    ui_page["sp_corner_left_button"] = pv.PvButton(
        container=scroll_content, x=300, y=145, width=110, height=30,
        text='Corner Left',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["sp_corner_right_button"] = pv.PvButton(
        container=scroll_content, x=420, y=145, width=110, height=30,
        text='Corner Right',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    # Row 2: Throw-ins
    ui_page["sp_throw_front_button"] = pv.PvButton(
        container=scroll_content, x=300, y=180, width=110, height=30,
        text='Throw Front',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["sp_throw_rear_button"] = pv.PvButton(
        container=scroll_content, x=420, y=180, width=110, height=30,
        text='Throw Rear',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    # Row 3: Free kicks
    ui_page["sp_direct_kick_button"] = pv.PvButton(
        container=scroll_content, x=300, y=215, width=110, height=30,
        text='Direct Kick',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["sp_indirect_kick_button"] = pv.PvButton(
        container=scroll_content, x=420, y=215, width=110, height=30,
        text='Indirect Kick',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    # Row 4: Penalty and Goal kick
    ui_page["sp_penalty_kick_button"] = pv.PvButton(
        container=scroll_content, x=300, y=250, width=110, height=30,
        text='Penalty',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    ui_page["sp_goal_kick_button"] = pv.PvButton(
        container=scroll_content, x=420, y=250, width=110, height=30,
        text='Goal Kick',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=11,
        font_color=(0, 0, 0, 1),
        idle_color=(245, 245, 245, 1), hover_color=(200, 230, 201, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=False
    )

    # ==========================================
    # OFFSIDE-SPECIFIC FIELDS
    # ==========================================
    ui_page["offside_player_label"] = pv.PvText(
        container=scroll_content, x=260, y=115, width=200, height=25,
        text='Offside Player:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["offside_player_dropdown"] = QComboBox()
    ui_page["offside_player_dropdown"].setParent(scroll_content)
    ui_page["offside_player_dropdown"].setGeometry(260, 145, 250, 30)
    ui_page["offside_player_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["offside_player_dropdown"].hide()

    # ==========================================
    # HANDBALL-SPECIFIC FIELDS
    # ==========================================
    ui_page["handball_player_label"] = pv.PvText(
        container=scroll_content, x=260, y=115, width=200, height=25,
        text='Guilty Player:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["handball_player_dropdown"] = QComboBox()
    ui_page["handball_player_dropdown"].setParent(scroll_content)
    ui_page["handball_player_dropdown"].setGeometry(260, 145, 250, 30)
    ui_page["handball_player_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["handball_player_dropdown"].hide()

    # ==========================================
    # SUBSTITUTION-SPECIFIC FIELDS
    # ==========================================
    ui_page["sub_in_label"] = pv.PvText(
        container=scroll_content, x=260, y=115, width=200, height=25,
        text='Player In:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["sub_in_dropdown"] = QComboBox()
    ui_page["sub_in_dropdown"].setParent(scroll_content)
    ui_page["sub_in_dropdown"].setGeometry(260, 145, 250, 30)
    ui_page["sub_in_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["sub_in_dropdown"].hide()

    ui_page["sub_out_label"] = pv.PvText(
        container=scroll_content, x=260, y=185, width=200, height=25,
        text='Player Out:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=False
    )

    ui_page["sub_out_dropdown"] = QComboBox()
    ui_page["sub_out_dropdown"].setParent(scroll_content)
    ui_page["sub_out_dropdown"].setGeometry(260, 215, 250, 30)
    ui_page["sub_out_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #f5f5f5;
            border: 1px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }
    """)
    ui_page["sub_out_dropdown"].hide()

    ui_page["export_csv_button"] = pv.PvButton(
        container=window, x=920, y=685, width=140, height=30,
        text='Export CSV',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1),
        idle_color=(179, 229, 252, 1), hover_color=(144, 202, 249, 1),
        border_color=(220, 220, 220, 1), border_thickness=1,
        is_visible=True
    )
    
    return ui_page