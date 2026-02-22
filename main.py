import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.core.audio import SoundLoader

# تصميم الواجهة الاحترافي (KV)
KV = '''
MDScreen:
    md_bg_color: [0.02, 0.1, 0.05, 1]
    BoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "مصحف المرحوم عايد شلالدة"
            elevation: 4
            md_bg_color: [0.05, 0.25, 0.15, 1]
            specific_text_color: [0.9, 0.8, 0.2, 1]

        MDCard:
            size_hint: (0.9, 0.2)
            pos_hint: {"center_x": .5}
            elevation: 2
            padding: "10dp"
            md_bg_color: [0.08, 0.3, 0.18, 1]
            radius: [15,]
            MDLabel:
                text: "صدقة جارية عن روح والدي عايد شلالدة\\nاللهم اجعل القرآن نوراً لقبره"
                halign: "center"
                theme_text_color: "Custom"
                text_color: [1, 1, 1, 1]
                font_style: "Subtitle1"

        MDScrollView:
            MDList:
                id: container
'''

class QuranApp(MDApp):
    sound = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

    def on_start(self):
        # قائمة كاملة مصغرة (كمثال لـ 114 سورة)
        surahs = [
            ("الفاتحة", "001"), ("البقرة", "002"), ("آل عمران", "003"), 
            ("النساء", "004"), ("المائدة", "005"), ("الأنعام", "006")
            # يمكن إضافة البقية بنفس النمط حتى 114
        ]
        
        for name, num in surahs:
            item = OneLineIconListItem(
                text=f"سورة {name}",
                on_release=lambda x, n=num: self.play_quran(n)
            )
            item.add_widget(IconLeftWidget(icon="play-circle-outline", icon_color=[0.9, 0.8, 0.2, 1]))
            self.root.ids.container.add_widget(item)

    def play_quran(self, surah_num):
        # رابط مباشر لصوت القارئ (مشاري العفاسي كمثال)
        url = f"https://server8.mp3quran.net/afs/{surah_num}.mp3"
        
        if self.sound:
            self.sound.stop()
        
        self.sound = SoundLoader.load(url)
        if self.sound:
            self.sound.play()

if __name__ == '__main__':
    QuranApp().run()
