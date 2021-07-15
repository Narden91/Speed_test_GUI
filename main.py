from typing import Text
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class ConverterApp(MDApp):
    def flip(self):
        """[summary]
        """
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.text = "Enter a Decimal number"
            self.converted.text = "" 
            self.label.text = "" 
        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.text = "Enter a Binary number"
            self.converted.text = "" 
            self.label.text = ""   
        
    
    def convert(self, args):
        """[summary]
        Args:
            args ([type]): [description]
        """
        
        # Conversione bin -> dec
        if self.state == 0:   
            # Prelevo il numero immesso nella finestra 
            usr_input = self.input.text
            
            # Check se non è stato inserito un valore valido
            if usr_input == '' or usr_input == 'Enter a Binary Number':
                self.label.text = "Enter a valid number "
                self.converted.text = ""
            else:
                # Converto in binario
                val = int(usr_input, 2)
                
                # Aggiorna il testo di "converted" con il risultato della conversione 
                self.converted.text = str(val)
                
                self.label.text = "In decimal is: "
        
        # Conversione dec -> bin
        else:
            # Prelevo il numero immesso nella finestra 
            usr_input = self.input.text
            
            # Check se non è stato inserito un valore valido
            if usr_input == '' or usr_input == 'Enter a Decimal number' :
                self.label.text = "Enter a valid number "
                self.converted.text = ""
            else:
                # Converto in Decimale: le stringhe una volta convertite in
                # binario sono nella forma 0b1000 con [2:] elimino 0b
                val = bin(int(usr_input))[2:]
                
                # Aggiorna il testo di "converted" con il risultato della conversione 
                self.converted.text = str(val)
                
                self.label.text = "In binary is: "
    
    def build(self):
        """[summary]
        Returns:
            [type]: [description]
        """
        self.state = 0
        
        self.theme_cls.primary_palette = "Teal"
        
        # Display della schermata
        screen = MDScreen()
        
        # Dichiaro l'oggetto toolbar
        self.toolbar = MDToolbar(title="Binary To Decimal")
        
        # Decido la posizione della toolbar
        self.toolbar.pos_hint = {"top":1}
        
        # Aggiunge una icona nella toolbar  e premendola si attiva la funzione flip()
        self.toolbar.right_action_items = [
        ["rotate-3d-variant", lambda x:self.flip()]]
        
        # Aggiunge la Toolbar alla finestra
        screen.add_widget(self.toolbar)
        
        # Logo
        screen.add_widget(Image(
            source="logo.png", 
            pos_hint = {"center_x": 0.5, "center_y": 0.69 }
            ))
        
        # Widget per collezionare l'input dell'utente
        self.input = MDTextField(
            text = "Enter a Binary Number",
            halign = "center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y": 0.45 },
            font_size = 22
        )
        
        screen.add_widget(self.input)
        
        # Label primaria e secondaria
        self.label = MDLabel(
            halign = "center",
            pos_hint = {"center_x": 0.5, "center_y": 0.35 },
            theme_text_color = "Secondary" 
        )
        
        self.converted = MDLabel(
            halign = "center",
            pos_hint = {"center_x": 0.5, "center_y": 0.3 },
            theme_text_color = "Primary",
            font_style ="H5"
        )
        
        screen.add_widget(self.label)
        screen.add_widget(self.converted)
        
        # Pulsante Conversione
        screen.add_widget(MDFillRoundFlatButton(
            text= "CONVERT",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y": 0.15 },
            on_press = self.convert
            ))
        
        
        return screen

if __name__ == '__main__':
    ConverterApp().run()
