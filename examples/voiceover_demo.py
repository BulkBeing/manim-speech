from manim import *
import pygments.styles as code_styles
from manim_speech import SpeechSynthesizer, VoiceoverScene
from manim_speech.azure import AzureTTSConfig

code_style = code_styles.get_style_by_name("monokai")


class VoiceoverDemo(VoiceoverScene):
    def construct(self):
        # Initialize speech synthesis using Azure's TTS API
        self.init_voiceover(AzureTTSConfig(style="newscast-casual", global_speed=1.15))
        banner = ManimBanner().scale(0.5)

        tracker = self.add_voiceover_text("Hey Manim Community!")
        self.play(
            banner.create(),
        )
        self.wait_for_voiceover()
        tracker = self.add_voiceover_text(
            "Today, I want to show you how you can generate voiceovers directly in your Python code."
        )

        self.play(
            banner.expand(),
        )
        self.wait(tracker.get_remaining_duration(buff=-1))
        self.play(FadeOut(banner))

        demo_code = Code(
            code='''tracker = self.add_voiceover_text(
    """AI generated voices have become realistic
        enough for use in most content. Using neural
        text-to-speech frees you from the painstaking
        process of recording and manually syncing
        audio to your video."""
)
self.play(Write(demo_code), run_time=tracker.duration)''',
            insert_line_no=False,
            style=code_style,
            background="window",
            font="Consolas",
            language="python",
        ).rescale_to_fit(12, 0)

        tracker = self.add_voiceover_text(
            """AI generated voices have become realistic
                enough for use in most content. Using neural
                text-to-speech frees you from the painstaking
                process of recording and manually syncing
                audio to your video."""
        )
        self.play(Write(demo_code), run_time=tracker.duration)

        self.add_voiceover_text(
            """As you can see, Manim started playing this voiceover,
                right as the code object started to be drawn.
                Let's see some more examples."""
        )
        self.wait_for_voiceover()
        self.play(FadeOut(demo_code))

        circle = Circle()
        square = Square().shift(2 * RIGHT)

        self.add_voiceover_text("This circle is drawn as I speak.")
        self.play(Create(circle))
        self.wait_for_voiceover()

        self.add_voiceover_text("Let's shift it to the left 2 units.")
        self.play(circle.animate.shift(2 * LEFT))
        self.wait_for_voiceover()

        self.add_voiceover_text("Now, let's transform it into a square.")
        self.play(Transform(circle, square))
        self.wait_for_voiceover()

        self.add_voiceover_text("""I would go on, but you get the idea.""")
        self.play(FadeOut(circle))
        self.wait_for_voiceover()

        self.add_voiceover_text(
            """You can find this demo in the GitHub repo shown on your screen."""
        )
        self.play(FadeIn(Tex("https://github.com/MathBlocks/manim-speech")))
        self.wait_for_voiceover()

        self.wait(5)
