from kivy.app import App
from kivy.uix.button import Button
from plyer import audio

class RecorderApp(App):
    def build(self):
        btn = Button(text="Start Recording")
        btn.bind(on_press=self.record_audio)
        return btn

    def record_audio(self, instance):
        audio.start()
        # TODO: Add stop logic and save path

RecorderApp().run()