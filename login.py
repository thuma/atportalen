import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.graphics import *
from kivy.graphics import Color, Rectangle
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage


class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
	
	
	#Prepare widgets needed for the login window
        super(LoginScreen, self).__init__(**kwargs)
        
        self.orientation='vertical'
        self.padding=10
        self.spacing=5
		
		#Add the logo
        self.add_widget(
            AsyncImage(
                source="https://www.sahlgrenska.se/Areas/SU/Static/images/vgregion-wave.png",
                size_hint= (1, .8),
                pos_hint={'center_x':.46, 'center_y':.5}))
		
		#Add welcome text
        self.add_widget(Label(text="Välkommen AT läkare"))
        self.add_widget(Label(text="Skriv in dina initialer"))
		
		#Define Username widget
        self.add_widget(Label(text='Användarnamn'))
        self.username = TextInput(multiline=False)
		#self.username = TextInput(multiline=False, size=(200, 50), size_hint=(None, None))
        self.add_widget(self.username)
		
        #Define password widget
        self.add_widget(Label(text='Lösenord'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
		
		#define the login widget
        self.login = Button(text='Logga in', background_color = (0,1,1,1))
        self.add_widget(self.login)
 


class AtPortal(App):

    def build(self):
	#Adding our main layout
        login_screen = LoginScreen()
        return login_screen


if __name__ == '__main__':
    AtPortal().run()
