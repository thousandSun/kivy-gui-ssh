from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout


class ConnectBox(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def clear_fields(self):
        for id in self.ids:
            print(id)
        
    def connect(self):
        port = int(self.ids.port.text)
        if not self.validate_port(port):
            self.ids.error_label.text = "Invalid Port (1 - 65535)"
        else:
            print(self.ids.hostname.text)
            print(self.ids.username.text)
            print(self.ids.password.text)
    
    def validate_port(self, port):
        return 1 <= port <= 65535
    
    def close_application(self):
        App.get_running_app().stop()
        Window.close()


class ConnectApp(App):
    pass


ConnectApp().run()