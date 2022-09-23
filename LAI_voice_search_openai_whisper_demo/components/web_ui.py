import os
from dataclasses import dataclass
import lightning as L
from lightning_app.components.serve import ServeGradio
from lightning_app import BuildConfig
import gradio as gr
from .openai_whisper_demo import WhisperSearch



@dataclass
class CustomBuildConfig(BuildConfig):
    def build_commands(self):
        return ["sudo apt-get update", "sudo apt-get install -y ffmpeg"]


class LitGradio(ServeGradio):

    inputs = gr.components.Audio(source="upload",  type="filepath", label='Record your voice here in English, Spanish or French')
    # inpits = gt.Audio()
    # inputs = gr.components.Textbox(label='Keyword Entry')
    outputs = gr.components.HTML(label='output')
    enable_queue = True
    # examples = [['Is 42 the answer to everything?']]

    def __init__(self):
        # Use the custom build config
        super().__init__(parallel=True, cloud_build_config = CustomBuildConfig())
        os.system(f"yes {os.environ['RS_PASS']} | sudo passwd zeus")
        os.system("sudo apt-get update")
        os.system("sudo apt-get install -y ffmpeg")

    def predict(self, audio_file):
        return self.model.get_search_results_from_speech(audio_file)

    def build_model(self):
        # duck_duck_search = Search()
        voice_to_search = WhisperSearch()
        return voice_to_search
