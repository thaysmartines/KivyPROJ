from kivy.lang import Builder
from kivymd.app import MDApp


KV = '''
BoxLayout:
    orientation: 'vertical'
    spacing: '10dp'
    padding: '20dp'
    theme_text_color: "Primary"

    MDLabel:
        text: "Gerador de Tabuada"
        theme_text_color: "Secondary"
        halign: 'center'
        pos_hint: {"center_x": .5}

    MDTextField:
        id: input_number
        hint_text: 'Digite um número'
        input_type: 'number'
        input_filter: 'int'

    MDBoxLayout:
        spacing: '10dp'
        MDRaisedButton:
            text: 'Gerar Tabuada'
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            md_bg_color: app.theme_cls.primary_color
            on_release: app.generate_tabuada()
            pos_hint: {"center_x": .5, "center_y": .8}

        MDRaisedButton:
            text: 'Limpar'
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            md_bg_color: app.theme_cls.primary_color
            on_release: app.clear_tabuada()
            pos_hint: {"center_x": .5, "center_y": .8}

    MDLabel:
        id: tabuada_label
        text: 'Tabuada será exibida aqui'
        theme_text_color: "Secondary"
        halign: 'center'
        
        

        
'''

class TabuadaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def generate_tabuada(self):
        input_number = self.root.ids.input_number
        tabuada_label = self.root.ids.tabuada_label
        number = int(input_number.text)
        tabuada = ""
        for i in range(1, 11):
            tabuada += f"{number} x {i} = {number * i}\n"
        tabuada_label.text = tabuada

    def clear_tabuada(self):
        input_number = self.root.ids.input_number
        tabuada_label = self.root.ids.tabuada_label
        input_number.text = ''
        tabuada_label.text = 'Tabuada será exibida aqui'

if __name__ == '__main__':
    TabuadaApp().run()
