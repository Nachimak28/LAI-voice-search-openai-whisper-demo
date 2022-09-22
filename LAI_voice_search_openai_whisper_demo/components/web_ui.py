import lightning as L
from lightning_app.components.serve import ServeGradio
import gradio as gr
# from .ddg_search_component import Search
from .openai_whisper_demo import WhisperSearch
# import logging


class LitGradio(ServeGradio):

    inputs = gr.components.Audio(source="upload",  type="filepath", label='Record your voice here in English, Spanish or French for best results-')
    # inpits = gt.Audio()
    # inputs = gr.components.Textbox(label='Keyword Entry')
    outputs = gr.components.HTML(label='output')
    enable_queue = True
    # examples = [['Is 42 the answer to everything?']]

    def __init__(self):
        super().__init__(parallel=True)

    def predict(self, audio_file):
        return self.model.get_search_results_from_speech(audio_file)

    def build_model(self):
        # duck_duck_search = Search()
        voice_to_search = WhisperSearch()
        return voice_to_search