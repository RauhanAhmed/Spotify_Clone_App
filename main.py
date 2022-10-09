from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.audio import SoundLoader
import os
import random

os.environ["KIVY_AUDIO"] = "ffpyplayer"


helper_string = """
Screen:
    BoxLayout:
        orientation:'vertical'

        MDScrollView:
            size_hint_y:1000

            MDList:
            
                TwoLineAvatarListItem:
                    on_release:app.playaudio("Imspiderman")
                    text:"I'm Spider Man"
                    secondary_text:'Hans Zimmer, The Magnificent Six, Pharell Williams, Johnny Marr'
                    ImageLeftWidget:
                        source:r"song_8.jpg"

                TwoLineAvatarListItem:
                    on_release:app.playaudio("countingstars")
                    text:"Counting Stars"
                    secondary_text:'OneRepublic'
                    ImageLeftWidget:
                        source:r"song_4.jpg"
                        
                TwoLineAvatarListItem:
                    on_release:app.playaudio("harleysinhawaii")
                    text:'Harleys In Hawaii'
                    secondary_text:'Katy Perry'
                    ImageLeftWidget:
                        source:r"song_1.png"

                TwoLineAvatarListItem:
                    on_release:app.playaudio("tightrope")                
                    text:"Tightrope"
                    secondary_text:'ZAYN'
                    ImageLeftWidget:
                        source:r"song_10.jpg"
                        
                TwoLineAvatarListItem:
                    on_release:app.playaudio("watermelonsugar")
                    text:"Watermelon Sugar"
                    secondary_text:'Harry Styles'
                    ImageLeftWidget:
                        source:r"song_9.jpg"
                        
                TwoLineAvatarListItem:
                    on_release:app.playaudio("wedonttalkanymore")
                    text:"We Don't Talk Anymore"
                    secondary_text:'Charlie Puth, Selena Gomez'
                    ImageLeftWidget:
                        source:r"song_2.jpg"

                TwoLineAvatarListItem:
                    on_release:app.playaudio("gonegonegone")
                    text:"Gone, Gone, Gone"
                    secondary_text:'Philip Philips'
                    ImageLeftWidget:
                        source:r"song_6.jpg"

                TwoLineAvatarListItem:
                    on_release:app.playaudio("backtoyou")
                    text:"Back To You"
                    secondary_text:'Selena Gomez'
                    ImageLeftWidget:
                        source:r"song_3.jpg"


                TwoLineAvatarListItem:
                    on_release:app.playaudio("shootout")
                    text:"Shootout"
                    secondary_text:'Izzamuzzic, Julien Marchal'
                    ImageLeftWidget:
                        source:r"song_7.jpg"                        

                TwoLineAvatarListItem:
                    on_release:app.playaudio("thankyounext")
                    text:"thank you, next"
                    secondary_text:'Ariana Grande'
                    ImageLeftWidget:
                        source:r"song_5.jpg"

                TwoLineAvatarListItem:
                    on_release:app.playaudio("nightchanges")
                    text:"Night Changes"
                    secondary_text:'One Direction'
                    ImageLeftWidget:
                        source:r"song_11.png"

                TwoLineAvatarListItem:
                    on_release:app.playaudio("minefields")
                    text:"Minefields"
                    secondary_text:'Faouzia, John Legend'
                    ImageLeftWidget:
                        source:r"song_12.png"

        MDBottomAppBar:
            MDTopAppBar:
                id:toolbar
                title:'Spotify'
                icon:'spotify'
                type:'bottom'
                mode:'center'
                on_action_button:app.play_random(0)
                right_action_items:[['skip-previous', app.previous],['play', app.play_random],['skip-next', app.play_random]]        

"""

class App(MDApp):
    def build(self):
        self.current = None
        self.state = 0
        self.songs = ['minefields', 'nightchanges', 'thankyounext', 'shootout', 'backtoyou', 'gonegonegone',\
                 'wedonttalkanymore', 'watermelonsugar', 'tightrope', 'harleysinhawaii',\
                 'countingstars', 'Imspiderman']
        self.icon = r'logo.jpg'
        self.title = 'Spotify Clone'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Green'
        return Builder.load_string(helper_string)

    def playaudio(self, title):
        if self.state == 0:
            self.current = title
            self.state = 1
            self.sound = SoundLoader.load(title + ".ogg")
            self.root.ids.toolbar.right_action_items = [['skip-previous', self.previous],['pause', self.stopaudio],['skip-next', self.forward]]
            self.sound.play()
        else:
            self.stopaudio(0)
            self.current = title
            self.state = 1
            self.sound = SoundLoader.load(title + ".ogg")
            self.root.ids.toolbar.right_action_items = [['skip-previous', self.previous],['pause', self.stopaudio],['skip-next', self.forward]]
            self.sound.play()
            
    def stopaudio(self, instance):
        self.state = 0
        self.sound.stop()
        self.current = None
        self.root.ids.toolbar.right_action_items = [['skip-previous', self.previous],['play', self.play_random],['skip-next', self.forward]]

    def play_random(self, instance):
        choice = random.choice(self.songs)
        self.playaudio(choice)

    def previous(self, instance):
        if self.current == None:
            self.play_random(0)
        elif self.songs.index(self.current) == 11:
            self.playaudio(self.songs[0])
        else:
            current_index = self.songs.index(self.current)
            prev_index = current_index + 1
            self.playaudio(self.songs[prev_index])

    def forward(self, instance):
        if self.current == None:
            self.play_random(0)
        elif self.songs.index(self.current) == 0:
            self.playaudio(self.songs[-1])
        else:
            current_index = self.songs.index(self.current)
            forward_index = current_index - 1
            self.playaudio(self.songs[forward_index])
        
App().run()
