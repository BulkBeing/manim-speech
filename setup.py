#!/usr/bin/env python

from distutils.core import setup

setup(
    name="manim-speech",
    version="0.0.1",
    description="Module for play.ht API",
    author="prism0x",
    author_email="",
    url="",
    install_requires=[
        "manim",
        "sox",
        "azure-cognitiveservices-speech",
        "python-dotenv",
        "pygments",
    ],
    packages=["manim_speech"],
)
