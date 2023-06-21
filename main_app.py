# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.uix.popup import Popup
import instructions
import ruffier
import seconds
import sits
import runner
age = 6
name = 'None'
puls1 = 1
puls2 = 1
puls3 = 1
def check_int(num):
    try:
        return int(num)
    except:
        return False
class UserData(Screen):
    def __init__(self,name='userdata'):
        self.rect = Rectangle(size=self.size,pos=self.pos)
        backgroundcolour = [50, 50, 50]
        super().__init__(name=name)
        self.popup = Popup(title='Ошибка',content=Label(text=''),size_hint=(None,None),width=500,height=500)
        vl = BoxLayout(orientation='vertical')
        age_hl= BoxLayout(size_hint=(1,0.3))
        name_hl= BoxLayout(size_hint=(1,0.3))
        btn_continue = Button(text='Начать',size_hint=(0.3,0.2),pos_hint={'center_x':0.5})
        btn_continue.on_press = self.next
        self.Info_Label = Label(text=instructions.txt_instruction,size_hint=(0.5,0.5),pos_hint={'center_x':0.5,'center_y':0.5})
        label_age = Label(text='Ваш возраст:',size_hint=(None,None),width=200,height=30,pos_hint={'center_y':0.5})
        label_name = Label(text='Ваше имя:',size_hint=(None,None),width=200,height=30,pos_hint={'center_y':0.5})
        self.age_input = TextInput(multiline=False,focus=False,size_hint=(None,None),width=200,height=30,pos_hint={'center_y':0.5})
        self.name_input= TextInput(multiline=False,focus=False,size_hint=(None,None),width=200,height=30,pos_hint={'center_y':0.5})
        age_hl.add_widget(label_age)
        age_hl.add_widget(self.age_input)
        name_hl.add_widget(label_name)
        name_hl.add_widget(self.name_input)
        vl.add_widget(self.Info_Label)
        vl.add_widget(name_hl)
        vl.add_widget(age_hl)
        vl.add_widget(btn_continue)
        self.add_widget(vl)
    def next(self):
        global age,name
        age = self.age_input.text
        check_age = check_int(age)
        if not check_age or check_age <=0:
            self.popup.content = Label(text='Введите\nкорректный возраст')
            self.popup.open()
            self.age_input.text = ''
        else:
            age = check_age
            name = self.name_input.text
            self.manager.transition.direction = 'left'
            self.manager.current = 'userpuls'
class UserPuls(Screen):
    def __init__(self,name='userpuls'):
        super().__init__(name=name)
        self.timer = seconds.Seconds(15)
        self.timer.bind(done=self.sec_finished)
        self.next_screen = False
        self.popup = Popup(title='Ошибка',content=Label(text=''),size_hint=(None,None),width=500,height=500)
        vl = BoxLayout(orientation='vertical')
        self.btn_continue = Button(text='Начать',size_hint=(0.3,None),height=100,pos_hint={'center_x':0.5})
        self.btn_continue.on_press = self.next
        self.puls_label = Label(text=instructions.txt_test1,size_hint=(0.2,None),height=200,pos_hint={'center_x':0.5})
        self.puls_input = TextInput(multiline=False,focus=False,size_hint=(0.5,None),height=30,pos_hint={'center_y':0.5})
        self.puls_input.set_disabled(True)
        res_label = Label(text='Введите результат',size_hint=(0.5,None),height= 30,pos_hint={'center_y':0.5})
        input_hl = BoxLayout(size_hint=(0.5,None),height=200)
        input_hl.add_widget(res_label)
        input_hl.add_widget(self.puls_input)
        vl.add_widget(self.puls_label)
        vl.add_widget(self.timer)
        vl.add_widget(input_hl)
        vl.add_widget(self.btn_continue)
        self.add_widget(vl)
    def sec_finished(self,*args):
        self.next_screen = True
        self.timer.text = 'Время вышло!'
        self.btn_continue.text = 'Продолжить'
        self.btn_continue.set_disabled(False)
        self.puls_input.set_disabled(False)
    def next(self):
        if not self.next_screen:
            self.btn_continue.set_disabled(True)
            self.timer.start()
            
        else:
            global puls1
            check_puls1 = check_int(self.puls_input.text)
            if not check_puls1 or check_puls1 <= 0:
                self.popup.content = Label(text='Ошибка! Введите\nкорректный пульс')
                self.puls_input.text = ''
            else:
                self.manager.transition.direction = 'left'
                self.manager.current = 'usersits'
class UserSits(Screen):
    def __init__(self,name='usersits'):
        super().__init__(name=name)
        self.valueSits = sits.Sits(30)
        self.anim = runner.Runner(30,1.5,size_hint=(0.3,1))
        self.anim.bind(value=self.valueSits.next)
        self.anim.bind(finished=self.sits_finished)
        self.next_screen = False
        hl = BoxLayout()
        self.lb = Label(text=instructions.txt_sits)
        self.btn_continue = Button(text='Начать',size_hint=(0.3,0.2),pos_hint={'center_x':0.5})
        self.btn_continue.on_press = self.next
        hl.add_widget(self.lb)
        hl.add_widget(self.anim)
        vl = BoxLayout(orientation='vertical')
        vl.add_widget(hl)
        vl.add_widget(self.valueSits)
        vl.add_widget(self.btn_continue)
        self.add_widget(vl)
    def sits_finished(self,*args):
        self.next_screen = True
        self.lb.text = 'Отлично\nПроходите дальше!'
        self.btn_continue.text = 'Продолжить'
        self.btn_continue.set_disabled(False)
    def next(self):
        if not self.next_screen:
            self.anim.start()
            self.btn_continue.set_disabled(True)
        else:
            self.manager.transition.direction = 'left'
            self.manager.current = 'userpuls2'
class UserPuls2(Screen):
    def __init__(self,name='userpuls2'):
        super().__init__(name=name)
        self.timer = seconds.Seconds(15)
        self.timer.bind(done=self.sec_finished)
        self.stage = 0
        self.next_screen = False
        self.popup = Popup(title='Ошибка',content=Label(text=''),size_hint=(None,None),width=500,height=500)
        self.btn_continue = Button(text='Начать',size_hint=(0.3,0.5),pos_hint={'center_x':0.5})
        self.btn_continue.on_press = self.next
        vl = BoxLayout(orientation='vertical')
        self.text = Label(text=instructions.txt_test3)
        res_label = Label(text='Результат',size_hint=(None,None),height=30,width=250,pos_hint={'center_y':0.5})
        res2_label = Label(text='Результат после отдыха',size_hint=(None,None),height=30,width=250,pos_hint={'center_y':0.5})
        self.res_input = TextInput(multiline=False,focus=False,size_hint=(0.2,None),height=30,pos_hint={'center_y':0.5})
        self.res2_input = TextInput(multiline=False,focus=False,size_hint=(0.2,None),height=30,pos_hint={'center_y':0.5})
        self.res_input.set_disabled(True)
        self.res2_input.set_disabled(True)
        res_l = BoxLayout(size_hint=(0.6,1))
        res2_l = BoxLayout(size_hint=(0.6,1))
        res_l.add_widget(res_label)
        res_l.add_widget(self.res_input)
        res2_l.add_widget(res2_label)
        res2_l.add_widget(self.res2_input)
        vl.add_widget(self.text)
        vl.add_widget(self.timer)
        vl.add_widget(res_l)
        vl.add_widget(res2_l)
        vl.add_widget(self.btn_continue)
        self.add_widget(vl)
    def sec_finished(self,*args):
        if self.timer.done:
            if self.stage == 0:
                self.stage = 1
                self.timer.restart(30)
                self.res_input.set_disabled(False)
                self.timer.changeText = 'Отдыхайте '
            elif self.stage == 1:
                self.timer.restart(15)
                self.timer.changeText = 'Прошло секунд '
                self.stage = 2
            elif self.stage == 2:
                self.res2_input.set_disabled(False)
                self.btn_continue.text = 'Закончить\nтест'
                self.btn_continue.set_disabled(False)
                self.next_screen = True
    def next(self):
        if not self.next_screen:
            self.btn_continue.set_disabled(True)
            self.timer.start()
        else:
            global puls2,puls3
            check_puls2 = check_int(self.res_input.text)
            if not check_puls2 or check_puls2 <= 0:
                self.popup.content = Label(text='Ошибка! Введите\nкорректный пульс 1')
                self.popup.open()
                self.res_input.text = ''
            else:
                puls2 = check_puls2
                check_puls3 = check_int(self.res2_input.text)
                if not check_puls2 or check_puls2 <= 0:
                    self.popup.content = Label(text='Ошибка! Введите\nкорректный пульс 2')
                    self.popup.open()
                    self.res2_input.text = ''
                else:
                    puls3 = check_puls3
                    self.manager.transition.direction = 'left'
                    self.manager.current = 'result'
class Result(Screen):
    def __init__(self,name='result'):
        super().__init__(name=name)
        self.lb = Label(text='')
        self.add_widget(self.lb)
        self.printResult()
    def printResult(self):
        self.lb.text = str(ruffier.test(puls1,puls2,puls3,age))      
class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(UserData())
        sm.add_widget(UserPuls())
        sm.add_widget(UserSits())
        sm.add_widget(UserPuls2())
        sm.add_widget(Result())
        return sm
TestApp().run()