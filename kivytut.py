import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
 
# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy
class CalcPageLayout(PageLayout):
    
    def calc(self, text):
        self.display.text += "ergebnis"

class HelloKivyApp(App):
 
    # This returns the content we want in the window
    def build(self):
        return CalcPageLayout()
 
    
    
helloKivy = HelloKivyApp()
helloKivy.run()