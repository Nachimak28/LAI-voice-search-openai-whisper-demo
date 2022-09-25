import os
from dataclasses import dataclass

import gradio as gr
import lightning as L
from lightning.app.components.serve import ServeGradio


@dataclass
class CustomBuildConfig(L.BuildConfig):
    def build_commands(self):
        return ["sudo apt-get update", "sudo apt-get install -y ffmpeg"]


class LitGradio(ServeGradio):

    inputs = gr.components.Audio(
        source="upload", type="filepath", label="Upload your audio"
    )

    outputs = gr.components.HTML(label="Transcribed output")
    enable_queue = True
    examples = [["./resources/42_ans_to_everything_english.wav"]]

    def __init__(self):
        # Use the custom build config
        super().__init__(
            parallel=True,
            cloud_compute=L.CloudCompute("cpu-small"),
            cloud_build_config=CustomBuildConfig(
                requirements=[
                    "whisper@ git+https://github.com/openai/whisper",
                    "duckduckgo-search==2.1.3",
                ]
            ),
        )

    def predict(self, audio_file):
        return self.model.get_search_results_from_speech(audio_file)

    def build_model(self):
        from .openai_whisper_demo import WhisperSearch

        voice_to_search = WhisperSearch()
        return voice_to_search
