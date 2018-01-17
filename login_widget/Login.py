# simple login widget
# @ belal-bh
# 18.01.18
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup


Builder.load_string('''
<CustBoxLayout>:
    usr_pswrd: usr_pswrd
    usr_name: usr_name
    display: lbl_otpt
    orientation :  "vertical"
    spacing: 10
    padding: 10

    BoxLayout : 
        # 1 horizontal box that creates a line 
        size_hint_y :  6
        Label :
            id: lbl_otpt
            markup: True
            font_size: 26
            #align: 'middle'
            valign: 'middle'
            halign: 'center'
            padding_x: 10
            text :  "Login info" 
            size_hint_x :  4
            size: self.texture_size
            #text_size: cm(15), cm(4)
            text_size: self.size
    
    BoxLayout : 
        # 1 horizontal box that creates a line 
        size_hint_y :  1 
        Label : 
            text :  "User Name:" 
            size_hint_x :  2 
        TextInput :
            id: usr_name
            font_size: 32
            multiline: False
            size_hint_x :  4
            # limit to 20 chars
            input_filter: lambda text, from_undo: text[:20 - len(self.text)]
            hint_text: "Between 3 to 20 characters"
            hint_text_color: [0.5, 0.5, 0.5, 0.5] #gray

    BoxLayout : 
        # 2 horizontal box that creates the line 
        size_hint_y :  1 
        Label :
            size_hint_x :  2
            text :  " Password: "
            
        TextInput :
            id: usr_pswrd
            font_size: 32
            multiline: False
            password: True
            size_hint_x :  4
            hint_text: "Between 8 to 32 characters"
            input_filter: lambda text, from_undo: text[:32 - len(self.text)]
            hint_text_color: [0.5, 0.5, 0.5, 0.5] #gray
            
            
    BoxLayout : 
        # 3 horizontal box that creates the line 
        size_hint_y :  1
        size_hint_x: .5
        halign: 'middle'
        Button : 
            text :  "Submit"
            on_press: root.submit_action(root.usr_name,root.usr_pswrd)
''')

class CustBoxLayout(BoxLayout):
    usr_name = ObjectProperty(None)
    usr_pswrd = ObjectProperty(None)
    display = ObjectProperty(None)
    
    

    def submit_action(self, usr_name,usr_pswrd):
        if len(usr_pswrd.text)<8 or len(usr_name.text)<3:
            popup = Popup(title='Invalid user input', \
                         title_color = [1,0,0,1], \
                         title_size = '20sp', \
                         title_align = 'center', \
                         content=Label(text='[b][i][color=46AE34]User name[/color][/i][b] or  [b][i][color=46AE34]passowrd[/color][/i][/b] is invalid. \n Please give valid input.',markup=True),\
                         auto_dismiss=True, \
                         size_hint=(.6, .4))
            popup.open()
        else:
            text='Hello [color=46AE34] %s [/color]!  Login successful! \n Here you go...' %usr_name.text
            self.display.text = text

class LoginApp(App):

    def build(self):
        return CustBoxLayout()

if __name__ == '__main__':
    LoginApp().run()

    
