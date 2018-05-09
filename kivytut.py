from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file("hellokivy.kv")
   




 
<<<<<<< HEAD
class MenuScreen(Screen):
    pass
 



       
class SettingsScreen(Screen):
    pass





class CreateScreen(Screen):
    pass











# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(CreateScreen(name='create'))

=======
# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy
class CalcPageLayout(PageLayout):
    
    def calc(self, text):
        self.display.text += "ergebnis"
>>>>>>> 382e238f37d0b1fb8337fd1c74d20dd69db60db9

class HelloKivyApp(App):
 
    # This returns the content we want in the window
    def build(self):
        return sm
 
    
    
helloKivy = HelloKivyApp()
helloKivy.run()