from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file("hellokivy.kv")
   




 
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


class HelloKivyApp(App):
 
    # This returns the content we want in the window
    def build(self):
        return sm
 
    
    
helloKivy = HelloKivyApp()
helloKivy.run()