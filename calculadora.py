from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import math 

Window.size = (350,580)

class First(App):
    def build(self):
        container = BoxLayout(orientation='vertical')

        self.top = Label(text='result', font_size=50)

        header = BoxLayout(orientation ='horizontal')
        self.bot1 = Button(text='1',on_press=lambda x:self.click('1'))
        self.bot2 = Button(text='2',on_press=lambda x:self.click('2'))
        self.bot3 = Button(text='3',on_press=lambda x:self.click('3'))
        self.botmais = Button(text='+',on_press=lambda x:self.click('+'))
        self.botapaga = Button(text='<<',on_press=self.apaga)

        header.add_widget(self.bot1)
        header.add_widget(self.bot2)
        header.add_widget(self.bot3)
        header.add_widget(self.botmais)
        header.add_widget(self.botapaga)

        main = BoxLayout(orientation ='horizontal')
        self.bot4 = Button (text='4',on_press=lambda x:self.click('4'))
        self.bot5 = Button (text='5',on_press=lambda x:self.click('5'))
        self.bot6 = Button (text='6',on_press=lambda x:self.click('6'))
        self.botmenos = Button(text='-',on_press=lambda x:self.click('-'))
        self.botpotencia = Button(text='^',on_press=lambda x:self.click('^'))
        
        main.add_widget(self.bot4)
        main.add_widget(self.bot5)
        main.add_widget(self.bot6)
        main.add_widget(self.botmenos)
        main.add_widget(self.botpotencia)

        footer = BoxLayout(orientation ='horizontal')
        self.bot7 = Button (text='7',on_press=lambda x:self.click('7'))
        self.bot8 = Button (text='8',on_press=lambda x:self.click('8'))
        self.bot9 = Button (text='9',on_press=lambda x:self.click('9'))
        self.botdividir = Button(text='*',on_press=lambda x:self.click('*'))
        self.botraiz = Button(text='√',on_press=self.raiz)

        
        footer.add_widget(self.bot7)
        footer.add_widget(self.bot8)
        footer.add_widget(self.bot9)
        footer.add_widget(self.botdividir)
        footer.add_widget(self.botraiz)


        bot = BoxLayout(orientation='horizontal')
        self.bot10 = Button(text='C',on_press=self.reset)
        self.bot11 = Button(text='0',on_press=lambda x:self.click('0'))
        self.bot12 = Button(text='.',on_press=lambda x:self.click('.'))
        self.bot13 = Button(text='/',on_press=lambda x:self.click('/'))
        self.bot14 = Button(text='=',on_press=self.calcular)

        bot.add_widget(self.bot10)
        bot.add_widget(self.bot11)
        bot.add_widget(self.bot12)
        bot.add_widget(self.bot13)
        bot.add_widget(self.bot14)



        container.add_widget(self.top)
        container.add_widget(header)
        container.add_widget(main)
        container.add_widget(footer)
        container.add_widget(bot)
        
        return container
    
    def reset(self,lbl):
        self.top.text = ""

    def apaga(self,text):
        self.top.text = self.top.text[:-1]


    def click(self,text):
        self.top.text += text

    def raiz(self,text):
        resulta = math.sqrt(int(self.top.text))
        self.top.text =str(resulta)
    



    def calcular(self,text):
        if '*' in self.top.text:
            valor =self.top.text.split("*")
            self.top.text = str(int(valor[0])*int(valor[1]))
        if '-' in self.top.text:
            valor =self.top.text.split("-")
            self.top.text = str(int(valor[0])-int(valor[1]))
        if '/' in self.top.text:
            valor =self.top.text.split("/")
            self.top.text = str((int(valor[0])/int(valor[1])))
        if '+' in self.top.text:
            valor =self.top.text.split("+")
            self.top.text = str((int(valor[0])+int(valor[1])))


        
        



First().run()