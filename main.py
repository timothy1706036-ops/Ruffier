from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

from instructions import *
from ruffier import *

from seconds import Seconds

age = 7
name = ""
p1, p2, p3 = 0, 0, 0

def check_int(str_num):
    try:
        return int(str_num)
    except ValueError:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)

        lbl1 = Label(text="Enter your name:", halign = 'right')
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text="Enter your age:", halign = 'right')
        self.in_age = TextInput(text='', multiline=False)
        self.btn = Button(text='start', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8,None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8,None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def next(self):
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = 'pulse1'


class Pulse1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test1)

        lbl = Label(text="Pulse (15 sec):", halign='right')
        self.in_pulse = TextInput(multiline=False)
        self.btn = Button(text='Next', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        line.add_widget(lbl)
        line.add_widget(self.in_pulse)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def next(self):
        global p1
        val = check_int(self.in_pulse.text)
        if val is False or val < 0:
            p1 = 0
            self.in_pulse.text = '0'
        else:
            p1 = val
        # go back to instructions for now (other screens not implemented)
        try:
            self.manager.current = 'squats'
        except Exception:
            pass

class CheckSquats(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test2)

        self.btn = Button(text='Start squats', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.start_squats

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def start_squats(self):
        self.btn.disabled = True
        self.seconds = Seconds(30, self.end_squats)
        self.add_widget(self.seconds)

    def end_squats(self):
        self.btn.disabled = False
        self.remove_widget(self.seconds)

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(Pulse1(name='pulse1'))
        sm.add_widget(CheckSquats(name='squats'))
        return sm

app = HeartCheck()
app.run()
