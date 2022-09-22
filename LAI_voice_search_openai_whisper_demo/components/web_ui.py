import lightning as L
from lightning_app.components.serve import ServeGradio
import gradio as gr
from .ddg_search_component import Search
# import logging


class LitGradio(ServeGradio):

    inputs = gr.components.Audio(source="microphone",  type="filepath", label='Record your voice here in English, Spanish or French for best results-')
    # inpits = gt.Audio()
    # inputs = gr.components.Textbox(label='Keyword Entry')
    outputs = gr.components.HTML(label='output')
    enable_queue = True
    # examples = [['Is 42 the answer to everything?']]

    def __init__(self):
        super().__init__(parallel=True)

    def predict(self, input_text='Is 42 the answer to everything'):
        return self.model.search('Is 42 the answer to everything')

    def build_model(self):
        duck_duck_search = Search()
        return duck_duck_search