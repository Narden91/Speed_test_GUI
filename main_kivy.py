from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton


class MyLayout(BoxLayout):

    scr_mngr = ObjectProperty(None)

    def check_data_login(self):
        username = self.scr_mngr.screen1.username.text
        password = self.scr_mngr.screen1.password.text

        print(username)
        print(password)

        if username == "" and password == "":
            self.change_screen("screen2")


    def change_screen(self, screen, *args):
        self.scr_mngr.current = screen
        
        
    def flip(self):
        print("Button pressed")

# Costruzione del layout dell'app
KV = """
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem

#:import partial functools.partial

MyLayout:
    scr_mngr: scr_mngr
    orientation: 'vertical'

    ScreenManager:
        id: scr_mngr
        screen1: screen1

        Screen:
            id: screen1
            name: 'screen1'
            username: username
            password: password

            MDCard:
                size_hint: None, None
                size: dp(520), dp(340)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                BoxLayout:
                    orientation:'vertical'
                    padding: dp(20)
                    spacing:20

                    MDLabel:
                        text: 'Connection'
                        theme_text_color: 'Secondary'
                        font_style:"Title"
                        size_hint_y: None
                        height: dp(36)

                    MDSeparator:
                        height: dp(1)

                    MDTextField:
                        id: username
                        hint_text: "Username "
                        helper_text_mode: "on_focus"

                    MDTextField:
                        id: password
                        hint_text: "Password "
                        helper_text_mode: "on_focus"
                        password: True

                    MDFlatButton:
                        text: "Connection"
                        pos_hint: {'center_x': 0.5}
                        on_release: root.check_data_login()
        Screen:
            name: 'screen2'

            Toolbar:
                id: toolbar
                title: "Welcome ! "
                pos_hint: {'top':1}
                md_bg_color: app.theme_cls.primary_color
                background_palette: 'DeepPurple'
                background_hue: 'A400'
                left_action_items: [['arrow-left', partial(root.change_screen, 'screen1') ]]
                right_action_items: [['animation', lambda x: root.flip()]]

            Image:
                source: 'logo.png'
                size: self.texture_size
                pos_hint: {"center_x": 0.5, "center_y": 0.69 }
                size_hint: (0.3,0.3)
            
            MDFillRoundFlatButton:
                text: "Start"
                pos_hint: {'center_x': 0.5, 'center_y': 0.50}
                on_release: root.check_data_login()
            
            MDLabel:
                font_style: 'Title'
                text: "Download Speed"
                theme_text_color: "Custom"
                text_color: 1.2, 0.6, 0.5, 1
                height: self.texture_size[1] + dp(3)
                halign: 'center'
                pos_hint: {'center_x': 0.5, 'center_y': 0.30}
                
            MDLabel:
                font_style: 'Title'
                text: "-"
                theme_text_color: "Custom"
                text_color: 1.2, 0.6, 0.5, 1
                height: self.texture_size[1] + dp(3)
                halign: 'center'
                pos_hint: {'center_x': 0.5, 'center_y': 0.25}
                
            MDLabel:
                font_style: 'Title'
                text: "Upload Speed"
                theme_text_color: "Custom"
                text_color: 1, 0, 0.2, 1
                height: self.texture_size[1] + dp(3)
                halign: 'center'
                pos_hint: {'center_x': 0.5, 'center_y': 0.20}
                
            MDLabel:
                font_style: 'Title'
                text: "-"
                theme_text_color: "Custom"
                text_color: 1, 0, 0.2, 1
                height: self.texture_size[1] + dp(3)
                halign: 'center'
                pos_hint: {'center_x': 0.5, 'center_y': 0.15}
"""

#Available vanilla font_style are: ‘'Body1', 'Body2', 'Caption', 'Subhead', 'Title', 'Headline', 'Display1', 'Display2', 'Display3', 'Display4', 'Button', 'Icon'.


class SpeedtestApp(App):
    title = "Speedtest App"
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    theme_cls.accent_palette = 'Blue'
    # theme_cls.theme_style = 'Dark'
    
    def build(self):
        return Builder.load_string(KV)


SpeedtestApp().run()
