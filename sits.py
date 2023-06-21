# напиши модуль для подсчета количества приседаний
from kivy.uix.label import Label
class Sits(Label):
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        self.text = f'Приседаний осталось {self.total - self.current}'
        super().__init__(text=self.text)
    def next(self, *args):
        self.current += 1
        self.text = f'Приседаний осталось {self.total - self.current}'