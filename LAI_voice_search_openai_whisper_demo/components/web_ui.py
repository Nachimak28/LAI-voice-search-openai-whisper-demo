from dataclasses import dataclass
import lightning as L
from lightning_app.components.serve import ServeGradio
from lightning_app import BuildConfig
import gradio as gr
from .openai_whisper_demo import WhisperSearch



@dataclass
class CustomBuildConfig(BuildConfig):
    def build_commands(self):
        return ["sudo apt-get update", "sudo apt-get install ffmpeg"]


class LitGradio(ServeGradio):

    inputs = gr.components.Audio(source="upload",  type="filepath", label='Record your voice here in English, Spanish or French')
    # inpits = gt.Audio()
    # inputs = gr.components.Textbox(label='Keyword Entry')
    outputs = gr.components.HTML(label='output')
    enable_queue = True
    # examples = [['Is 42 the answer to everything?']]

    def __init__(self):
        super().__init__(parallel=True)

        # Use the custom build config
        self.cloud_build_config = CustomBuildConfig()
        # self._cloud_build_config = CustomBuildConfig(requirements=["ffmpeg-python"])
        # super().__init__(parallel=True, host='0.0.0.0', port=8888)

    def predict(self, audio_file):
        return self.model.get_search_results_from_speech(audio_file)

    def build_model(self):
        # duck_duck_search = Search()
        voice_to_search = WhisperSearch()
        return voice_to_search