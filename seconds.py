# напиши модуль для реализации секундомера
from kivy.properties import BooleanProperty
from kivy.clock import Clock
from kivy.uix.label import Label
class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self,total,**kwargs):
        self.done = False
        self.current = 0
        self.changeText = 'Прошло секунд '
        self.text = self.changeText+str(self.current)
        self.total = total
        super().__init__(text=self.text)
    def restart(self, total, **kwargs):
        self.done = False
        self.total = total
        self.text = self.changeText+str(self.current)
        self.current = 0
        self.start()
    def start(self):
        Clock.schedule_interval(self.change,1)
    def change(self, dt):
        self.current += 1
        self.text = self.changeText+str(self.current)
        if self.current >= self.total:
            self.done = True
            return False
            