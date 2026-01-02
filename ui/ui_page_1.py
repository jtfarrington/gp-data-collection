import pyvisual as pv
from PySide6.QtWidgets import QTextEdit, QComboBox


def create_page_1_ui(window,ui):
    """
    Create and return UI elements for Page 1.
    :param container: The page widget for Page 1.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["start_match_button"] = pv.PvButton(container=window, x=17, y=5, width=87,
        height=25, text='start_match', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 235, 238, 1), hover_color=(255, 205, 210, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(255, 205, 210, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["kickoff_button"] = pv.PvButton(container=window, x=104, y=5, width=87,
        height=25, text='kickoff', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 235, 238, 1), hover_color=(255, 205, 210, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(255, 205, 210, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["halftime_button"] = pv.PvButton(container=window, x=187, y=5, width=87,
        height=25, text='halftime', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 235, 238, 1), hover_color=(255, 205, 210, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(255, 205, 210, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["overtime_button"] = pv.PvButton(container=window, x=274, y=5, width=88,
        height=25, text='overtime', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 235, 238, 1), hover_color=(255, 205, 210, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(255, 205, 210, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["overtime_2_button"] = pv.PvButton(container=window, x=362, y=5, width=87,
        height=25, text='overtime_2', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 235, 238, 1), hover_color=(255, 205, 210, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(255, 205, 210, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["pk_shootout_button"] = pv.PvButton(container=window, x=449, y=5, width=87,
        height=25, text='pk_s', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 235, 238, 1), hover_color=(255, 205, 210, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(255, 205, 210, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["pause_match_button"] = pv.PvButton(container=window, x=536, y=5, width=87,
        height=25, text='pause_match', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 235, 238, 1), hover_color=(255, 205, 210, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(255, 205, 210, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["end_match_button"] = pv.PvButton(container=window, x=623, y=5, width=87,
        height=25, text='end_match', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 235, 238, 1), hover_color=(255, 205, 210, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(255, 205, 210, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_substitute_button"] = pv.PvButton(container=window, x=15, y=160, width=90,
        height=40, text='sub', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["home_button"] = pv.PvButton(container=window, x=105, y=160, width=90,
        height=40, text='home_team', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_5"] = pv.PvButton(container=window, x=14, y=360, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_fwd_2"] = pv.PvButton(container=window, x=104, y=600, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_fwd_1"] = pv.PvButton(container=window, x=104, y=560, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_4"] = pv.PvButton(container=window, x=104, y=520, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_3"] = pv.PvButton(container=window, x=104, y=480, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_2"] = pv.PvButton(container=window, x=104, y=440, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_1"] = pv.PvButton(container=window, x=104, y=400, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_4"] = pv.PvButton(container=window, x=104, y=360, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_3"] = pv.PvButton(container=window, x=104, y=320, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_2"] = pv.PvButton(container=window, x=104, y=280, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_1"] = pv.PvButton(container=window, x=104, y=240, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_gk"] = pv.PvButton(container=window, x=104, y=200, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_11"] = pv.PvButton(container=window, x=14, y=600, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_10"] = pv.PvButton(container=window, x=14, y=560, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_9"] = pv.PvButton(container=window, x=14, y=520, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_8"] = pv.PvButton(container=window, x=14, y=480, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_7"] = pv.PvButton(container=window, x=14, y=440, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_6"] = pv.PvButton(container=window, x=14, y=400, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_4"] = pv.PvButton(container=window, x=14, y=320, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_3"] = pv.PvButton(container=window, x=14, y=280, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_2"] = pv.PvButton(container=window, x=14, y=240, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_1"] = pv.PvButton(container=window, x=14, y=200, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["away_button"] = pv.PvButton(container=window, x=530, y=160, width=90,
        height=40, text='away_team', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag='away_button')

    ui_page["a_substitute_button"] = pv.PvButton(container=window, x=620, y=160, width=90,
        height=40, text='sub', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_4"] = pv.PvButton(container=window, x=530, y=360, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_11"] = pv.PvButton(container=window, x=620, y=600, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_10"] = pv.PvButton(container=window, x=620, y=560, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_9"] = pv.PvButton(container=window, x=620, y=520, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_8"] = pv.PvButton(container=window, x=620, y=480, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_7"] = pv.PvButton(container=window, x=620, y=440, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_6"] = pv.PvButton(container=window, x=620, y=400, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_5"] = pv.PvButton(container=window, x=620, y=360, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_4"] = pv.PvButton(container=window, x=620, y=320, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_3"] = pv.PvButton(container=window, x=620, y=280, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_2"] = pv.PvButton(container=window, x=620, y=240, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_1"] = pv.PvButton(container=window, x=620, y=200, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_fwd_2"] = pv.PvButton(container=window, x=530, y=600, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_fwd_1"] = pv.PvButton(container=window, x=530, y=560, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_4"] = pv.PvButton(container=window, x=530, y=520, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_3"] = pv.PvButton(container=window, x=530, y=480, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_2"] = pv.PvButton(container=window, x=530, y=440, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_1"] = pv.PvButton(container=window, x=530, y=400, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_3"] = pv.PvButton(container=window, x=530, y=320, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_2"] = pv.PvButton(container=window, x=530, y=280, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_1"] = pv.PvButton(container=window, x=530, y=240, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_gk"] = pv.PvButton(container=window, x=530, y=200, width=90,
        height=40, text='player_name', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(245, 245, 245, 1), hover_color=(224, 224, 224, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(224, 224, 224, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["short_button"] = pv.PvButton(container=window, x=226, y=665, width=90,
        height=40, text='short', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["medium_button"] = pv.PvButton(container=window, x=316, y=665, width=90,
        height=40, text='medium', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["long_button"] = pv.PvButton(container=window, x=406, y=665, width=90,
        height=40, text='long', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["short_high_button"] = pv.PvButton(container=window, x=226, y=625, width=90,
        height=40, text='short_high', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["med_high_button"] = pv.PvButton(container=window, x=316, y=625, width=90,
        height=40, text='med_high', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["long_high_button"] = pv.PvButton(container=window, x=406, y=625, width=90,
        height=40, text='long_high', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["clearance_button"] = pv.PvButton(container=window, x=226, y=600, width=90,
        height=25, text='clearance', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["shot_button"] = pv.PvButton(container=window, x=206, y=360, width=70,
        height=160, text='shot', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["over_button"] = pv.PvButton(container=window, x=351, y=360, width=90,
        height=40, text='over', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["over_left_button"] = pv.PvButton(container=window, x=276, y=360, width=75,
        height=40, text='over_left', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["post_left_button"] = pv.PvButton(container=window, x=276, y=480, width=80,
        height=40, text='post_left', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["over_right_button"] = pv.PvButton(container=window, x=441, y=360, width=75,
        height=40, text='over_right', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["failed_button"] = pv.PvButton(container=window, x=351, y=400, width=90,
        height=40, text='failed', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["wide_right_button"] = pv.PvButton(container=window, x=441, y=400, width=75,
        height=40, text='wide_right', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["wide_left_button"] = pv.PvButton(container=window, x=276, y=400, width=75,
        height=40, text='wide_left', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["blocked_button"] = pv.PvButton(container=window, x=276, y=440, width=120,
        height=40, text='blocked', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["saved_button"] = pv.PvButton(container=window, x=396, y=440, width=120,
        height=40, text='saved', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["crossbar_button"] = pv.PvButton(container=window, x=356, y=480, width=80,
        height=40, text='crossbar', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["post_right_button"] = pv.PvButton(container=window, x=436, y=480, width=80,
        height=40, text='post_right', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["delete_button"] = pv.PvButton(container=window, x=222, y=300, width=279,
        height=40, text='delete_last', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(255, 235, 238, 1), hover_color=(255, 205, 210, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(255, 205, 210, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["foul_button"] = pv.PvButton(container=window, x=234, y=160, width=85,
        height=120, text='foul', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["red_button"] = pv.PvButton(container=window, x=319, y=220, width=85,
        height=60, text='red_card', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["unfairness_button"] = pv.PvButton(container=window, x=319, y=120, width=85,
        height=40, text='unfairness', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["handball_button"] = pv.PvButton(container=window, x=404, y=120, width=85,
        height=40, text='handball', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["offside_button"] = pv.PvButton(container=window, x=234, y=120, width=85,
        height=40, text='offside', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["aerial_button"] = pv.PvButton(container=window, x=404, y=160, width=85,
        height=60, text='aerial_duel', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["corner_left_button"] = pv.PvButton(container=window, x=14, y=71, width=90,
        height=40, text='corner_left', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["corner_right_button"] = pv.PvButton(container=window, x=624, y=53, width=90,
        height=40, text='corner_right', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["throw_in_front_button"] = pv.PvButton(container=window, x=104, y=71, width=100,
        height=40, text='throw_in_front', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["throw_in_rear_button"] = pv.PvButton(container=window, x=525, y=53, width=100,
        height=40, text='throw_in_rear', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["direct_kick_button"] = pv.PvButton(container=window, x=226, y=71, width=90,
        height=40, text='direct', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["pk_button"] = pv.PvButton(container=window, x=316, y=71, width=90,
        height=40, text='penalty', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["indirect_kick_button"] = pv.PvButton(container=window, x=406, y=71, width=90,
        height=40, text='indirect', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["yellow_button"] = pv.PvButton(container=window, x=319, y=160, width=85,
        height=60, text='yellow_card', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["ground_button"] = pv.PvButton(container=window, x=404, y=220, width=85,
        height=60, text='ground_duel', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["own_goal_button"] = pv.PvButton(container=window, x=415, y=540, width=105,
        height=40, text='own_goal', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["ball_won_button"] = pv.PvButton(container=window, x=316, y=600, width=90,
        height=25, text='ball_won', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    from PySide6.QtWidgets import QTextEdit
    
    event_log_widget = QTextEdit()  # Create without parent first
    event_log_widget.setParent(window)  # Set parent after
    event_log_widget.setGeometry(720, 10, 350, 700)
    event_log_widget.setReadOnly(True)
    event_log_widget.setStyleSheet("""
        QTextEdit {
            background-color: #f5f5f5;
            border: 2px solid #c8c8c8;
            border-radius: 5px;
            padding: 10px;
            font-family: 'Courier New', monospace;
            font-size: 11px;
            color: #000000;
        }
    """)
    event_log_widget.setPlaceholderText("Event log will appear here...")
    
    ui_page["event_log_display"] = event_log_widget

    ui_page["goal_button"] = pv.PvButton(container=window, x=204, y=543, width=190,
        height=35, text='goal', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(165, 214, 167, 1), hover_color=(129, 199, 132, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(129, 199, 132, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["cross_right_button"] = pv.PvButton(container=window, x=525, y=93, width=190,
        height=37, text='cross_right', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["cross_left_button"] = pv.PvButton(container=window, x=14, y=105, width=190,
        height=37, text='cross_left', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["goal_kick_button"] = pv.PvButton(container=window, x=14, y=44, width=190,
        height=27, text='goal_kick', font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(200, 230, 201, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)
    
    # Navigation to Page 2
    ui_page["goto_page_2_button"] = pv.PvButton(
        container=window, x=640, y=680, width=50, height=30,
        text='→',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=18,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=True, italic=False,
        underline=False, strikethrough=False, 
        idle_color=(232, 245, 233, 1), hover_color=(200, 230, 201, 1),
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
    
    # Playing Direction Dropdown (add around existing match controls)
    ui_page["playing_left_label"] = pv.PvText(
        container=window, x=15, y=650, width=200, height=25,
        text='Playing Left:',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=13,
        font_color=(0, 0, 0, 1), bold=True,
        is_visible=True
    )

    ui_page["playing_left_dropdown"] = QComboBox()
    ui_page["playing_left_dropdown"].setParent(window)
    ui_page["playing_left_dropdown"].setGeometry(15, 675, 200, 30)
    ui_page["playing_left_dropdown"].addItems(["Select Team", "Home Team", "Away Team"])
    ui_page["playing_left_dropdown"].setStyleSheet("""
        QComboBox {
            background-color: #ffffff;
            border: 2px solid #dcdcdc;
            border-radius: 3px;
            padding: 5px;
            font-family: 'Courier New', monospace;
            font-size: 13px;
        }
        QComboBox:disabled {
            background-color: #f0f0f0;
            color: #888888;
        }
    """)

    return ui_page
