# -*- coding: utf-8 -*-
#!/usr/bin/env python

from kivy.app import App
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.graphics import Color
from kivy.config import Config
Config.set('graphics', 'width', '403')
Config.set('graphics', 'height', '768')

def hexToKivyColor(hex):
  if hex[0] == "#":
    hex = hex[1:]
  r = float(int(hex[0:2],16))/255.0
  g = float(int(hex[2:4],16))/255.0
  b = float(int(hex[4:6],16))/255.0
  return [ r,g,b ]

print hexToKivyColor("#a3c7e3")

atintro = """
Bra att veta som nyanställd.

OBS! Kolla alltid HR-portalen för aktuell information

Adressändring – du ändrar själv din adress i Självservice
När det gäller extra jourer som du gör utöver de som ingår i AT – då ska särskild timlista skrivas som attesteras av verksamheten. OBS! Du får inte göra mer än 200 ATL-timmar/år.
Fri sjukvård – arbetstagare får som anställningsförmån fri sjukvård inom öppenvården upp till högkostnadsskydd (f.n. 1100 kr). Särskild blankett ska fyllas i (se HR-portalen)  samt originalkvitto bifogas och skickas till din AT-läkarchef för påskrift.
Friskvård; I dagsläget är det ett belopp på 1300 kr. Se HR-portalen för gällande regler
http://intra.sahlgrenska.se/sv/SU/HR-portalen/

Du fyller i en särskild blankett
http://intra.sahlgrenska.se/sv/SU/HR-portalen/Arbetsmiljo-och-halsa/Friskvard-och-halsa/ och bifogar originalkvitto som du sedan skickar till din AT-läkarchef för påskrift.
Företagshälsovård; Du har möjlighet att kontakta företagshälsovården som vi anlitar inom VGR och du kan göra ett besök där. Behövs fler kontakter med företagshälsovården ska du kontakta din AT-läkarchef för godkännande av detta. Adress till Hälsan & Arbetslivet, Lilla Bommen 2, 411 04 Göteborg, tfn 031-708 32 00.
http://intra.vgregion.se/halsan
Försäkring – du är som anställd försäkrad via arbetsgivaren. Vill du läsa mer om vad som gäller, se
http://intra.sahlgrenska.se/sv/SU/HR-portalen/Arbetsmiljo-och-halsa/Arbetsskador-och-tillbud/
Föräldraledighet – du ska anmäla föräldraledighet minst 3 månader innan aktuell ledighetsperiod.
Ledigheter – tänk på att lämna in önskemål om ledigheter i god tid till schemaläggare samt även AT-kansliet.
Lönen utbetalas den 25:e, men infaller den 25:e en lördag eller söndag så kommer pengarna på fredagen i samma månad.
Lönen utbetalas via Swedbank. Om du vill få lönen insatt på en annan bank måste du vända dig till ”din” bank och begära överföring.
Närmast anhörig – tänk på att lägga in adress och tfn.nr till närmast anhörig i självservice
Om något inte fungerar på kliniken – tag kontakt med handledare eller klinik-SR, sedan verksamhetschef och därefter AT-kansliet.
Parkeringstillstånd – se information via
http://vastfast.vgregion.se/sv/Vastfastigheter/Kundtjanst/Parkering/Personalparkering-/Salhgrenska-sjukhuset-personalparkering/
Semester – du har rätt till betald semester fr och med det år som du påbörjar din anställning. Du ska under året plocka ut minst 20 semesterdagar, under förutsättning att du har 20 semesterdagar att ta ut. Planera din semester i god tid så att du tar ut rätt antal dagar. Vid frågor – kontakta AT-kansliet.
Sjukanmälan görs dels till berörd klinik (schemaläggare och sekr) och läggs sedan in i Heroma Självservice. OBS! Om du är sjuk längre än 7 dagar ska läkarintyg skickas in till AT-kansliet och information lämnas även till din AT-läkarchef.
"""

Builder.load_string("""
<AtPortal>:
  Screen:
    name: 'loggain'
    FloatLayout:
      canvas.before:
        Color:
          rgba: 1, 1, 1, 1
        BorderImage:
          size: self.size
          pos: self.pos
          source: 'bilder/bakgrund.png'
      #spacing: 2
      Label:
        text:'Välkommen AT Läkare'
		pos_hint: {'x':0.25, 'y':.6}
		size_hint: 0.5, 0.3
		font_size: '20sp'
      	#spacing_horizontal: 1
      Label:
        text: 'Skriv in dina initialer'
		pos_hint: {'x':0.25, 'y':0.46}
		size_hint: 0.5, 0.3
		font_size: '17sp'
      #Define username widget
	  Label:
	    text:'Användarnamn'
	    pos_hint: {'x':0.25, 'y':0.39}
		size_hint: 0.5, 0.3
      TextInput:
	    pos_hint: {'x':0.25, 'y':0.47}
		size_hint: 0.5, 0.05
		multiline:False
      Label:
	    pos_hint: {'x':0.25, 'y':0.36}
		size_hint: 0.5, 0.1
	    text:'Lösenord'
	  TextInput:
	    pos_hint: {'x':0.25, 'y':0.34}
		size_hint: 0.5, 0.05
        multiline:False
	    password:True
      #Define login widget
      Button:
        #pos_hint: {'None':None}
		#pos: 40, 40
        size_hint: 0.5, 0.1
        pos_hint: {'x':0.25, 'y':.2}
        text: 'Logga in'
    #color: [0,0,0]
        background_color: [1.0, 1.0, 1.0, 1.0]
        on_press: root.current = 'mainmenu'
  Screen:
    name: 'mainmenu'
    manager: 'manager'
    BoxLayout:
      canvas.before:
        Color:
          rgba: 1, 1, 1, 1
        BorderImage:
          size: self.size
          pos: self.pos
          source: 'bilder/bakgrund.png'
      spacing: 5
      orientation: "vertical"
      cols: 1
      Button:
	    size_hint: 0.5, 0.1
        pos_hint: {'center_x': 0.5}
        text: 'Anställning - Ledighet'
        background_color: [ 68, 44, 44, 0.5 ]
        on_press: root.current = 'textscreen'
      Button:
	    size_hint: 0.5, 0.1
        pos_hint: {'center_x': 0.5}
        text: 'Tjänstgöring - Schema - Legitimation'
        background_color: [ 68, 44, 44, 0.5 ]
      Button:
	    size_hint: 0.5, 0.1
        pos_hint: {'center_x': 0.5}
        text: 'Utbildning - Kurser'
        background_color: [ 68, 44, 44, 0.5 ]
      Button:
	    size_hint: 0.5, 0.1
        pos_hint: {'center_x': 0.5}
        text: 'Forskning - Förbättring'
        background_color: [ 68, 44, 44, 0.5 ]
      Button:
	    size_hint: 0.5, 0.1
        pos_hint: {'center_x': 0.5}
        text: 'Handledning'
        background_color: [ 68, 44, 44, 0.5 ]
      Button:
	    size_hint: 0.5, 0.1
        pos_hint: {'center_x': 0.5}
        text: 'AT-råd - AT-rum'
        background_color: [ 68, 44, 44, 0.5 ]
      Button:
	    size_hint: 0.5, 0.1
        pos_hint: {'center_x': 0.5}
        text: 'Kontakt'
        background_color: [ 68, 44, 44, 0.5 ]
      Button: 
	    size_hint: 0.5, 0.3
        pos_hint: {'center_x': 0.5}
        background_normal: ""
        text: 'Logga ut'
        background_color: [ 0, 0, 1, 1 ]
        on_press: root.current = 'loggain'
  Screen:
    name: 'textscreen'
    manager: 'manager'
    BoxLayout:
      canvas.before:
        Color:
          rgba: 0.6392156862745098, 0.7803921568627451, 0.8901960784313725, 1
        Rectangle:
          pos: self.pos
          size: self.size
      orientation: "vertical"
      cols: 1
      spacing: 5
      Label:
        size: (403, 50)
        size_hint: (None, None)
        text:'Anställning - Ledighet'
      ScrollView:
        do_scroll_x: False
        size: (403, 800)
        Label:
          color: 0,0,0,1
          text_size: root.width, None
          size: self.texture_size
          halign: 'left'
          valign: 'top'
          id: 'text'
          size_hint_y: None
          text: root.text_data
      Button:
        text: 'Tillbaka'
        background_normal: ""
        color: 0,0,0,1
        background_color: [1,0,0, 1]
        on_press: root.current = 'mainmenu'
        size_hint: (None, None)
        size: (403, 50)
""")

class AtPortal(ScreenManager):
    text_data = atintro

class ATApp(App):
    def build(self):
        self.icon = 'bilder/icon.png'
        return AtPortal()

if __name__ == '__main__':
     atp = ATApp()
     atp.run()
