from dataclasses import dataclass
from functools import partial

import gradio
import gradio as gr
import lightning as L
import torch
from lightning.app.components.serve import ServeGradio


@dataclass
class CustomBuildConfig(L.BuildConfig):
    """
    Custom build config defined for ServeGradio work component.
    Used to install the FFMPEG dependency which is used for audio processing by Whisper
    """
    def build_commands(self):
        return ["sudo apt-get update", "sudo apt-get install -y ffmpeg"]


class LitGradio(ServeGradio):
    # With a gradio bug fix, this input shall be changed from "upload" to "microphone" soon.
    # inputs = gr.components.Audio(
    #     source="upload", type="filepath", label="Record your audio"
    # )

    inputs = gr.components.Audio(
        source="microphone", type="filepath", label="Record your audio"
    )


    outputs = [gr.components.Textbox(label="Transcribed text"), gr.components.HTML(label="Transcribed output")]
    enable_queue = True
    examples = [["./resources/meaning_of_life.wav"], 
                ["./resources/42_ans_to_everything_english.wav"]]

    def __init__(self):
        # Use the custom build config
        super().__init__(
            parallel=True,
            cloud_compute=L.CloudCompute("cpu"),
            cloud_build_config=CustomBuildConfig(
                requirements=[
                    "whisper@ git+https://github.com/openai/whisper",
                    "duckduckgo-search==2.1.3",
                ]
            ),
        )

    @torch.inference_mode()
    def predict(self, audio_file):
        """
        Prediction method which run the speech-to-text prediction and returns 
        the web search results in HTML string format for rendering.
        """
        if audio_file is None:
            return ["You must upload an audio first", "<p style='color: red'>You must upload an audio first!</p>"]
        return self.model.get_search_results_from_speech(audio_file)

    def build_model(self):
        from .openai_whisper_demo import WhisperSearch

        voice_to_search = WhisperSearch()
        return voice_to_search

    def run(self, *args, **kwargs):
        if self._model is None:
            self._model = self.build_model()
        fn = partial(self.predict, *args, **kwargs)
        fn.__name__ = self.predict.__name__
        gradio.Interface(
            fn=fn,
            inputs=self.inputs,
            outputs=self.outputs,
            examples=self.examples,
            title="Speech Search Engine",
            description="""Make search on DuckDuckGo by uploading your audio.
            <br>It is deployed on small CPU so might run slow 🐢. 
            For faster inference clone the app and run on a GPU.""",
            article="""Powered by OpenAI's <a href="https://openai.com/blog/whisper/">Whisper</a>, 
            it approaches human level robustness and accuracy on English speech recognition.""",
            cache_examples=True,
        ).launch(
            server_name=self.host,
            server_port=self.port,
            enable_queue=self.enable_queue,
        )
