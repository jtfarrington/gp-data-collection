import pyvisual as pv


def create_page_0_ui(window,ui):
    """
    Create and return UI elements for Page 0.
    :param container: The page widget for Page 0.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["home_name_input"] = pv.PvTextInput(container=window, x=220, y=63, width=350,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_team__name....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=16, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["Text_1"] = pv.PvText(container=window, x=527, y=21, width=125,
        height=50, idle_color=(171, 84, 220, 0), text='Enter Lineups', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Montserrat/Montserrat.ttf', font_size=16,
        font_color=(0, 0, 0, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_2"] = pv.PvText(container=window, x=18, y=21, width=180,
        height=50, idle_color=(171, 84, 220, 0), text='Enter Match Details', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Montserrat/Montserrat.ttf', font_size=16,
        font_color=(0, 0, 0, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["submit_lineups_button"] = pv.PvButton(container=window, x=833, y=641, width=200,
        height=50, text='Submit', font='assets/fonts/Lexend/Lexend.ttf', font_size=16,
        font_color=(0, 0, 0, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(165, 214, 167, 1), hover_color=(129, 199, 132, 1),
        clicked_color=None, border_color=(220, 220, 220, 1), border_hover_color=(129, 199, 132, 1), border_thickness=1,
        corner_radius=0, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["competition"] = pv.PvTextInput(container=window, x=8, y=81, width=200,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='competition....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=14, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["venue"] = pv.PvTextInput(container=window, x=8, y=138, width=200,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='venue....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=14, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["date"] = pv.PvTextInput(container=window, x=8, y=200, width=200,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='date(dd/mm/yy)....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=14, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_name_1"] = pv.PvTextInput(container=window, x=295, y=103, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_coach_name"] = pv.PvTextInput(container=window, x=220, y=560, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='h_coach....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_name_2"] = pv.PvTextInput(container=window, x=295, y=143, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_name_11"] = pv.PvTextInput(container=window, x=295, y=503, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_name_10"] = pv.PvTextInput(container=window, x=295, y=463, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_name_9"] = pv.PvTextInput(container=window, x=295, y=423, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_name_8"] = pv.PvTextInput(container=window, x=295, y=383, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_name_7"] = pv.PvTextInput(container=window, x=295, y=343, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_name_6"] = pv.PvTextInput(container=window, x=295, y=303, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_name_5"] = pv.PvTextInput(container=window, x=295, y=263, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_name_4"] = pv.PvTextInput(container=window, x=295, y=223, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_name_3"] = pv.PvTextInput(container=window, x=295, y=183, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_gk_name"] = pv.PvTextInput(container=window, x=395, y=103, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_gk....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_name_1"] = pv.PvTextInput(container=window, x=395, y=143, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_def....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_name_2"] = pv.PvTextInput(container=window, x=395, y=183, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_def....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_name_3"] = pv.PvTextInput(container=window, x=395, y=223, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_def....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_name_4"] = pv.PvTextInput(container=window, x=395, y=263, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_def....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_name_1"] = pv.PvTextInput(container=window, x=395, y=303, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_mid....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_name_2"] = pv.PvTextInput(container=window, x=395, y=343, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_mid....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_name_3"] = pv.PvTextInput(container=window, x=395, y=383, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_mid....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_name_4"] = pv.PvTextInput(container=window, x=395, y=423, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_mid....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_fwd_name_1"] = pv.PvTextInput(container=window, x=395, y=463, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_fwd....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_fwd_name_2"] = pv.PvTextInput(container=window, x=395, y=503, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='home_fwd....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["away_name_input"] = pv.PvTextInput(container=window, x=583, y=63, width=350,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_team__name....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=16, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_name_1"] = pv.PvTextInput(container=window, x=658, y=103, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_gk_name"] = pv.PvTextInput(container=window, x=758, y=103, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_gk....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_name_1"] = pv.PvTextInput(container=window, x=758, y=143, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_def....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_name_1"] = pv.PvTextInput(container=window, x=758, y=303, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_mid....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_fwd_name_1"] = pv.PvTextInput(container=window, x=758, y=463, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_fwd....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_coach_name"] = pv.PvTextInput(container=window, x=583, y=560, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='a_coach....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_name_11"] = pv.PvTextInput(container=window, x=658, y=503, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_name_10"] = pv.PvTextInput(container=window, x=658, y=463, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_name_9"] = pv.PvTextInput(container=window, x=658, y=423, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_name_8"] = pv.PvTextInput(container=window, x=658, y=383, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_name_7"] = pv.PvTextInput(container=window, x=658, y=343, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_name_6"] = pv.PvTextInput(container=window, x=658, y=303, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_name_5"] = pv.PvTextInput(container=window, x=658, y=263, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_name_4"] = pv.PvTextInput(container=window, x=658, y=223, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_name_3"] = pv.PvTextInput(container=window, x=658, y=183, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_name_2"] = pv.PvTextInput(container=window, x=658, y=143, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_sub....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_fwd_name_2"] = pv.PvTextInput(container=window, x=758, y=503, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_fwd....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_name_2"] = pv.PvTextInput(container=window, x=758, y=343, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_mid....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_name_3"] = pv.PvTextInput(container=window, x=758, y=383, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_mid....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_name_4"] = pv.PvTextInput(container=window, x=758, y=423, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_mid....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_name_2"] = pv.PvTextInput(container=window, x=758, y=183, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_def....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_name_3"] = pv.PvTextInput(container=window, x=758, y=223, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_def....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_name_4"] = pv.PvTextInput(container=window, x=758, y=263, width=100,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='away_def....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=12, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_j_num_1"] = pv.PvTextInput(container=window, x=583, y=103, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_gk_j_num"] = pv.PvTextInput(container=window, x=858, y=103, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_j_num_1"] = pv.PvTextInput(container=window, x=858, y=143, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_j_num_2"] = pv.PvTextInput(container=window, x=858, y=183, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_j_num_3"] = pv.PvTextInput(container=window, x=858, y=223, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_def_j_num_4"] = pv.PvTextInput(container=window, x=858, y=263, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_j_num_1"] = pv.PvTextInput(container=window, x=858, y=303, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_j_num_2"] = pv.PvTextInput(container=window, x=858, y=343, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_j_num_3"] = pv.PvTextInput(container=window, x=858, y=383, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_mid_j_num_4"] = pv.PvTextInput(container=window, x=858, y=423, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_fwd_j_num_1"] = pv.PvTextInput(container=window, x=858, y=463, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_fwd_j_num_2"] = pv.PvTextInput(container=window, x=858, y=503, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_gk_j_num"] = pv.PvTextInput(container=window, x=495, y=103, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_j_num_1"] = pv.PvTextInput(container=window, x=495, y=143, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_j_num_2"] = pv.PvTextInput(container=window, x=495, y=183, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_j_num_3"] = pv.PvTextInput(container=window, x=495, y=223, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_def_j_num_4"] = pv.PvTextInput(container=window, x=495, y=263, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_j_num_1"] = pv.PvTextInput(container=window, x=495, y=303, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_j_num_2"] = pv.PvTextInput(container=window, x=495, y=343, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_j_num_3"] = pv.PvTextInput(container=window, x=495, y=383, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_mid_j_num_4"] = pv.PvTextInput(container=window, x=495, y=423, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_fwd_j_num_1"] = pv.PvTextInput(container=window, x=495, y=463, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_fwd_j_num_2"] = pv.PvTextInput(container=window, x=495, y=503, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_j_num_1"] = pv.PvTextInput(container=window, x=220, y=103, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_j_num_2"] = pv.PvTextInput(container=window, x=220, y=143, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_j_num_3"] = pv.PvTextInput(container=window, x=220, y=183, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_j_num_4"] = pv.PvTextInput(container=window, x=220, y=223, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_j_num_5"] = pv.PvTextInput(container=window, x=220, y=263, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_j_num_6"] = pv.PvTextInput(container=window, x=220, y=303, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num...',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_j_num_7"] = pv.PvTextInput(container=window, x=220, y=343, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_j_num_8"] = pv.PvTextInput(container=window, x=220, y=383, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_j_num_9"] = pv.PvTextInput(container=window, x=220, y=423, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_j_num_10"] = pv.PvTextInput(container=window, x=220, y=463, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["h_sub_j_num_11"] = pv.PvTextInput(container=window, x=220, y=503, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_j_num_2"] = pv.PvTextInput(container=window, x=583, y=143, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_j_num_3"] = pv.PvTextInput(container=window, x=583, y=183, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_j_num_4"] = pv.PvTextInput(container=window, x=583, y=223, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_j_num_5"] = pv.PvTextInput(container=window, x=583, y=263, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_j_num_6"] = pv.PvTextInput(container=window, x=583, y=303, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_j_num_7"] = pv.PvTextInput(container=window, x=583, y=343, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_j_num_8"] = pv.PvTextInput(container=window, x=583, y=383, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_j_num_9"] = pv.PvTextInput(container=window, x=583, y=423, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_j_num_10"] = pv.PvTextInput(container=window, x=583, y=463, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["a_sub_j_num_11"] = pv.PvTextInput(container=window, x=583, y=503, width=75,
        height=40, background_color=(245, 245, 245, 1), is_visible=True, placeholder='j_num....',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(220, 220, 220, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    return ui_page