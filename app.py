import lightning as L

from LAI_voice_search_openai_whisper_demo import LitGradio


class RootFlow(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.lit_gradio = LitGradio()

    def run(self):
        self.lit_gradio.run()

    def configure_layout(self):
        return [{"name": "home", "content": self.lit_gradio}]


app = L.LightningApp(RootFlow())
