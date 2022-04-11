import os
import azure.cognitiveservices.speech as speechsdk
import json
import hashlib
from dotenv import load_dotenv
from .modify_audio import adjust_speed

load_dotenv()


class AzureTTSConfig:
    def __init__(
        self,
        voice="en-US-AriaNeural",
        # style="newscast-casual",
        style=None,
        output_format="Audio48Khz192KBitRateMonoMp3",
        global_speed=1.00,
    ):
        self.voice = voice
        self.style = style
        self.output_format = output_format
        self.global_speed = global_speed


def azure_synthesize_text(text, config: AzureTTSConfig, output_dir, path=None):
    inner = text
    if config.style is not None:
        inner = r"""<mstts:express-as style="%s">
                %s
            </mstts:express-as>""" % (
            config.style,
            inner,
        )

    ssml = r"""<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
        xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
        <voice name="%s">
            %s
        </voice>
    </speak>
    """ % (
        config.voice,
        inner,
    )
    data = {"ssml": ssml, "config": config.__dict__}
    dumped_data = json.dumps(data)
    data_hash = hashlib.sha256(dumped_data.encode("utf-8")).hexdigest()

    # Get the file extension from output_format
    if config.output_format[-3:] == "Mp3":
        file_extension = ".mp3"
    else:
        raise Exception("Unrecognized output format")

    if path is None:
        path = os.path.join(output_dir, data_hash + file_extension)

        if os.path.exists(path):
            return path

    speech_config = speechsdk.SpeechConfig(
        subscription=os.environ["AZURE_SUBSCRIPTION_KEY"],
        region=os.environ["AZURE_SERVICE_REGION"],
    )
    speech_config.set_speech_synthesis_output_format(
        speechsdk.SpeechSynthesisOutputFormat[config.output_format]
    )
    audio_config = speechsdk.audio.AudioOutputConfig(filename=path)

    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config
    )
    speech_synthesis_result = speech_synthesizer.speak_ssml(ssml)

    if (
        speech_synthesis_result.reason
        == speechsdk.ResultReason.SynthesizingAudioCompleted
    ):
        pass
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        raise Exception("Speech synthesis failed")

    if config.global_speed != 1:
        # target = os.path.splitext(path)[0]
        adjust_speed(path, path, config.global_speed)

    return path
