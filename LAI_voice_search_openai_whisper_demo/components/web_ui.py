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

    inputs = gr.components.Audio(
            source="upload", type="filepath", label="Upload your audio"
        )

    outputs = gr.components.HTML(label="Transcribed output")
    enable_queue = True

    def __init__(self):
        # Use the custom build config
        super().__init__(parallel=True, cloud_build_config=CustomBuildConfig())

    def predict(self, audio_file):
        return self.model.get_search_results_from_speech(audio_file)

    def build_model(self):
        voice_to_search = WhisperSearch()
        return voice_to_search
