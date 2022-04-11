import manim_speech as ms

from manim_speech.modify_audio import adjust_speed

ss = ms.SpeechSynthesizer(ms.azure.AzureTTSConfig())

path = ss.synthesize_from_text("This is a test", path="azure-test.mp3")

adjust_speed(path, path+"adjusted.mp3", 1.15)