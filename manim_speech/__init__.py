from . import azure
import os


class SpeechSynthesizer:
    def __init__(self, tts_config, output_dir="media/tts"):
        self.tts_config = tts_config
        self.output_dir = output_dir

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def synthesize_from_text(self, text, path=None):
        if "\n" in text:
            text = text.replace("\n", " ")

        if isinstance(self.tts_config, azure.AzureTTSConfig):
            return azure.azure_synthesize_text(text, self.tts_config, self.output_dir, path=path)
